/**
 * Gestion de la sidebar
 */
var SideBar = (function() {

    /**
     * Largeur de la sidebar, en pixels
     */
    var SIDEBAR_WIDTH = 250;

    /**
     * Conteneur principal de l'application
     */
    var _$mainContainer = "#main-container";

    /**
     * Conteneur de la sidebar
     */
    var _$sidebar =       "#milkshake-sidebar";

    /**
     * Conteneur du cercle de la sidebar
     */
    var _$sidebarCircle = "#milkshake-sidebar-circle";

    /**
     * Conteneur de l'épingleur de sidebar
     */
    var _$sidebarPinner = "#milkshake-sidebar-pinner";

    /**
     * Conteneur de la liste des éléments
     */
    var _$sidebarList =   "#milkshake-sidebar-list";


    /**
     * Etat du pinnage de la sidebar
     */
    var _isPinned = false;

    /**
     * Initialisation des objets jQuery
     */
    var _init$Objects = function() {
        _$mainContainer = $(_$mainContainer);
        _$sidebar       = $(_$sidebar);
        _$sidebarCircle = $(_$sidebarCircle);
        _$sidebarPinner = $(_$sidebarPinner);
        _$sidebarList   = $(_$sidebarList);
    };

    /**
     * Initialisation des évènements
     */
    var _initEvents = function() {
        $(window).on('mousemove', _onWindowMouseMove);
        _$sidebarPinner.on("click", _onClickSidebarPinner);
    };

    /**
     * Gestion de l'affichage de la sidebar au démarrage
     */
    var _initDraw = function() {
        // Si le cookie d'épinglement est présent, affichage direct de la sidebar
        if ( typeof $.cookie('sidebar-pinned') !== "undefined" && $.cookie('sidebar-pinned') ) {
            _$mainContainer.css("padding-right", SIDEBAR_WIDTH);
            _$sidebar.css("display", "block");
            _$sidebarCircle.css("display", "none");
            _$sidebarPinner.addClass("active");
            _isPinned = true;
        }
    };

    /**
     * Gère l'affichage/la disparition de la sidebar
     *
     * @param object e Evènement associé
     */
    var _toggleSidebar = function(e) {
        if ( !_$sidebar.is(":visible") ) {
            if ( $(e.currentTarget).width() - e.pageX < 25 && e.pageY < 25 ) {
                self.fadeOut();
            }
        } else if (!_isPinned) {
            if ( $(e.currentTarget).width() - e.pageX > 270 ) {
                self.fadeIn();
            }
        }
    };

    /**
     * Gère l'agrandissement/rétressissement du cercle de la sidebar
     *
     * @param object e Evènement associé
     */
    var _updateSidebarCircle = function(e) {
        if ( $(e.currentTarget).width() - e.pageX < 100 && e.pageY < 100 ) {
            var radius = Math.max(100 - ($(e.currentTarget).width() - e.pageX ), 100 - e.pageY, 15);
            _$sidebarCircle.width(radius).height(radius);
        } else {
            _$sidebarCircle.width(15).height(15);
        }
    };

    /**
     * Gère la sauvegarde de l'épinglement de la sidebar
     *
     * @param object e Evènement associé
     */
    var _toggleSidebarPinned = function(e) {
        // Mise à jour de l'état de l'épinglement de la sidebar
        if ( _isPinned = !$(e.currentTarget).hasClass("active") ) {
            // Enregistrement du cookie pour le scope du site
            $.cookie('sidebar-pinned', true, { expires: 30, path: '/' });
            _$sidebarPinner.addClass("active");
        } else {
            // Suppression du cookie
            $.removeCookie('sidebar-pinned', { path: '/' });
            _$sidebarPinner.removeClass("active");
        }
    };

    /**
     * Callback de l'évènement mousemove de la fenêtre
     *
     * @param object e Evènement associé
     */
    var _onWindowMouseMove = function(e) {
        _toggleSidebar(e);
        _updateSidebarCircle(e);
    };

    /**
     * Callback de l'evènement click du pinner de la barre latérale
     *
     * @param object e Evènement associé
     */
    var _onClickSidebarPinner = function(e) {
        _toggleSidebarPinned(e);
    }

    var self = {

        /**
         * Initialisation de la sidebar
         */
        init: function() {
            _init$Objects();
            _initEvents();
            _initDraw();
        },

        /**
         * Masque la sidebar
         */
        fadeIn: function() {
            _$mainContainer.css("padding-right", 0);
            _$sidebarCircle.fadeIn();
            _$sidebar.fadeOut();

            // Si a la classe packery : accueil donc réajustement des widgets
            if (_$mainContainer.hasClass("packery"))
                _$mainContainer.packery();
        },

        /**
         * Affiche la sidebar
         */
        fadeOut: function() {
            _$mainContainer.css("padding-right", SIDEBAR_WIDTH);
            _$sidebarCircle.fadeOut();
            _$sidebar.fadeIn();

            // Si a la classe packery : accueil donc réajustement des widgets
            if (_$mainContainer.hasClass("packery"))
                _$mainContainer.packery();
        },

        /**
         * Initialisation des plugins à placer dans la sidebar
         */
        updateUserPlugins: function() {
            // Réinitialisation des éventuels anciens plugins
            $("#milkshake-sidebar-list > li.plugin").remove();

            // Ajout de chaque plugin
            $.each(MilkShake.pluginsAndWidgetsData.plugins, function(name, url) {
                $("#milkshake-sidebar-list").append('<li class="plugin"><a href="' + url + '">' + name + '</a></li>');
            });
        }
    };

    return self;
})();