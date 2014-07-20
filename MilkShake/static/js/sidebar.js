/**
 * Gestion de la sidebar
 */
var Sidebar = (function() {

    var self = {

        /**
         * Conteneur principal de l'application
         */
        _$mainContainer: "#main-container",

        /**
         * Conteneur de la sidebar
         */
        _$sidebar:       "#milkshake-sidebar",

        /**
         * Conteneur du cercle de la sidebar
         */
        _$sidebarCircle: "#milkshake-sidebar-circle",

        /**
         * Conteneur de l'épingleur de sidebar
         */
        _$sidebarPinner: "#milkshake-sidebar-pinner",

        /**
         * Conteneur de la liste des éléments
         */
        _$sidebarList: "#milkshake-sidebar-list",


        /**
         * Etat du pinnage de la sidebar
         */
        _isPinned: false,

        
        /**
         * Largeur de la sidebar, en pixels
         */
        SIDEBAR_WIDTH: 250,

        /**
         * URL de récupération des plugins disponibles pour l'utilisateur
         */
        URL_LIST_PLUGINS: "/listUserPlugins",


        /**
         * Initialisation de la sidebar
         */
        init: function() {
            self._initProperties();
            self.loadUserPlugins();
            self._initEvents();
            self._initDraw();
        },

        /**
         * Masque la sidebar
         */
        fadeIn: function() {
            self._$mainContainer.css("padding-right", 0);
            self._$sidebarCircle.fadeIn();
            self._$sidebar.fadeOut();

            // Si a la classe packery : accueil donc réajustement des widgets
            if (self._$mainContainer.hasClass("packery"))
                self._$mainContainer.packery();
        },

        /**
         * Affiche la sidebar
         */
        fadeOut: function() {
            self._$mainContainer.css("padding-right", self.SIDEBAR_WIDTH);
            self._$sidebarCircle.fadeOut();
            self._$sidebar.fadeIn();

            // Si a la classe packery : accueil donc réajustement des widgets
            if (self._$mainContainer.hasClass("packery"))
                self._$mainContainer.packery();
        },

        /**
         * Initialisation des plugins à placer dans la sidebar
         */
        loadUserPlugins: function() {
            $.ajax({
                url: self.URL_LIST_PLUGINS,
                method: "POST",
                dataType: "html",
                success: function(elements) {
                    // Mise à jour des plugins dans la liste de la sidebar
                    $(".nav-plugin", self._$sidebarList).remove();
                    self._$sidebarList.append(elements);
                }
            })
        },


        /**
         * Gestion des propriétés
         */
        _initProperties: function() {
            self._$mainContainer = $(self._$mainContainer);
            self._$sidebar       = $(self._$sidebar);
            self._$sidebarCircle = $(self._$sidebarCircle);
            self._$sidebarPinner = $(self._$sidebarPinner);
            self._$sidebarList   = $(self._$sidebarList);
        },

        /**
         * Initialisation des évènements
         */
        _initEvents: function() {
            $(window).on('mousemove', self._onWindowMouseMove);
            self._$sidebarPinner.on("click", self._onClickSidebarPinner);
        },

        /**
         * Gestion de l'affichage de la sidebar au démarrage
         */
        _initDraw: function() {
            // Si le cookie d'épinglement est présent, affichage direct de la sidebar
            if ( typeof $.cookie('sidebar-pinned') !== "undefined" && $.cookie('sidebar-pinned') ) {
                self._$mainContainer.css("padding-right", self.SIDEBAR_WIDTH);
                self._$sidebar.css("display", "block");
                self._$sidebarCircle.css("display", "none");
                self._$sidebarPinner.addClass("active");
                self._isPinned = true;
            }
        },

        /**
         * Gère l'affichage/la disparition de la sidebar
         *
         * @param object e Evènement associé
         */
        _toggleSidebar: function(e) {
            if ( !self._$sidebar.is(":visible") ) {
                if ( $(e.currentTarget).width() - e.pageX < 25 && e.pageY < 25 ) {
                    self.fadeOut();
                }
            } else if (!self._isPinned) {
                if ( $(e.currentTarget).width() - e.pageX > 270 ) {
                    self.fadeIn();
                }
            }
        },

        /**
         * Gère l'agrandissement/rétressissement du cercle de la sidebar
         *
         * @param object e Evènement associé
         */
        _updateSidebarCircle: function(e) {
            if ( $(e.currentTarget).width() - e.pageX < 100 && e.pageY < 100 ) {
                var radius = Math.max(100 - ($(e.currentTarget).width() - e.pageX ), 100 - e.pageY, 15);
                self._$sidebarCircle.width(radius).height(radius);
            } else {
                self._$sidebarCircle.width(15).height(15);
            }
        },

        /**
         * Gère la sauvegarde de l'épinglement de la sidebar
         *
         * @param object e Evènement associé
         */
        _toggleSidebarPinned: function(e) {
            // Mise à jour de l'état de l'épinglement de la sidebar
            if ( self._isPinned = !$(e.currentTarget).hasClass("active") ) {
                // Enregistrement du cookie pour le scope du site
                $.cookie('sidebar-pinned', true, { expires: 30, path: '/' });
                self._$sidebarPinner.addClass("active");
            } else {
                // Suppression du cookie
                $.removeCookie('sidebar-pinned', { path: '/' });
                self._$sidebarPinner.removeClass("active");
            }
        },

        /**
         * Callback de l'évènement mousemove de la fenêtre
         *
         * @param object e Evènement associé
         */
        _onWindowMouseMove: function(e) {
            self._toggleSidebar(e);
            self._updateSidebarCircle(e);
        },

        /**
         * Callback de l'evènement click du pinner de la barre latérale
         *
         * @param object e Evènement associé
         */
        _onClickSidebarPinner: function(e) {
            self._toggleSidebarPinned(e);
        }
    };

    return {
        init: self.init,
        hide: self.fadeIn,
        show: self.fadeOut,
        refreshPlugins: self.loadUserPlugins
    };
})();