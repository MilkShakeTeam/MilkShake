/**
 * Gestion de la sidebar
 */
var Sidebar = (function() {

    var self = {

        /**
         * Etat du pinnage de la sidebar
         *
         * @type boolean
         * @private
         */
        _isPinned: false,

        /**
         * Initialisation de la vue
         *
         * @public
         */
        init: function() {
            // Gestion des évènements
            $(window).on('mousemove', self._onWindowMouseMove);
            $(".sidebar-pinner").on("click", self._onClickSidebarPinner);

            // Si le cookie d'épinglement est présent, affichage direct de la sidebar
            if ( typeof $.cookie('sidebar-pinned') !== undefined && $.cookie('sidebar-pinned') ) {
                $(".main-container").css("padding-right", 250);
                $(".sidebar").css("display", "block");
                $(".sidebar-circle").css("display", "none");
                $(".sidebar-pinner").addClass("active");
                self._isPinned = true;
            }
        },

        /**
         * Masque la sidebar
         *
         * @public
         */
        fadeIn: function() {
            $(".sidebar-circle").fadeIn();
            $(".main-container").css("padding-right", 0);
            $(".sidebar").fadeOut();
        },

        /**
         * Affiche la sidebar
         *
         * @public
         */
        fadeOut: function() {
            $(".sidebar-circle").fadeOut();
            $(".main-container").css("padding-right", 250);
            $(".sidebar").fadeIn();
        },

        /**
         * Gère l'affichage/la disparition de la sidebar
         *
         * @param object e Evènement
         * @private
         */
        _toggleSidebar: function(e) {
            if ( !$(".sidebar").is(":visible") ) {
                if ( $(e.currentTarget).width() - e.pageX < 25 && e.pageY < 25 ) { // @TODO Magic number
                    self.fadeOut();
                }
            } else if (!self._isPinned) {
                if ( $(e.currentTarget).width() - e.pageX > 270 ) { // @TODO Magic number
                    self.fadeIn();
                }
            }
        },

        /**
         * Gère l'agrandissement/rétressissement du cercle de la sidebar
         *
         * @param object e Evènement
         * @private
         */
        _updateSidebarCircle: function(e) {
            if ( $(e.currentTarget).width() - e.pageX < 100 && e.pageY < 100 ) {
                var radius = Math.max(100 - ($(e.currentTarget).width() - e.pageX ), 100 - e.pageY, 15);
                $(".sidebar-circle").width(radius).height(radius);
            } else {
                $(".sidebar-circle").width(15).height(15);
            }
        },

        /**
         * Gère la sauvegarde de l'épinglement de la sidebar
         *
         * @param object e Evènement
         * @private
         */
        _toggleSidebarPinned: function(e) {
            // Mise à jour de l'état de l'épinglement de la sidebar
            if ( self._isPinned = !$(e.currentTarget).hasClass("active") ) {
                // Enregistrement du cookie pour le scope du site
                $.cookie('sidebar-pinned', true, { expires: 30, path: '/' });
            } else {
                // Suppression du cookie
                $.removeCookie('sidebar-pinned', { path: '/' });
            }
        },

        /**
         * Callback de l'évènement mousemove de la fenêtre
         *
         * @param object e Evènement
         * @private
         */
        _onWindowMouseMove: function(e) {
            self._toggleSidebar(e);
            self._updateSidebarCircle(e);
        },

        /**
         * Callback de l'evènement click du pinner de la barre latérale
         *
         * @param object e Evènement
         * @private
         */
        _onClickSidebarPinner: function(e) {
            self._toggleSidebarPinned(e);
        }
    };

    return {
        init: self.init,
        hide: self.fadeIn,
        show: self.fadeOut
    };
})();