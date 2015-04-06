/**
 * Gestion des widgets de la page d'accueil
 */
var HomeWidgets = (function() {

    /**
     * Conteneur principal de l'application
     */
    var _$mainContainer = "#main-container";


    /**
     * Initialisation des objets jQuery
     *
     * @private
     */
    var _init$Objects = function() {
        _$mainContainer = $(_$mainContainer);
    };

    /**
     * Gestion de packery
     *
     * @private
     */
    var _initPackery = function() {
        var container = $('#main-container');
        container.packery({
            columnWidth: 200,
            rowHeight: 200,
            itemSelector: '.item',
            gutter: 10
        });

        var itemElems = container.packery('getItemElements');
        // for each item element
        for ( var i=0, len = itemElems.length; i < len; i++ ) {
            var elem = itemElems[i];
            // make element draggable with Draggabilly
            var draggie = new Draggabilly( elem, {
                handle: '.handle'
            } );
            // bind Draggabilly events to Packery
            container.packery( 'bindDraggabillyEvents', draggie );
        }
    }


    var self = {

        /**
         * Initialisation générale des widgets de la page d'accueil
         */
        init: function() {
            // Initialisation des objets jQuery
            _init$Objects();

            // Rafraichissement des widgets de la page
            this.updateWidgets();
        },

        /**
         * Chargement des widgets
         */
        updateWidgets: function() {
            // Fichiers à charger
            var deferreds = [];

            // Récupération de l'intégralité des paths des ressources à charger
            $.each(MilkShake.pluginsAndWidgetsData.widgets, function(pluginName, pluginsWidgets) {

                // Récupération de chaque widget du plugin
                $.each(pluginsWidgets, function(index, widgetData) {

                    // Récupération du contenu HTML du widget
                    deferreds.push( $.get(widgetData.resources.html + "?" + $.now()) );

                    // Récupération de son JS associé
                    deferreds.push( $.ajax({
                        url: widgetData.resources.js + "?" + $.now(),
                        // Hack pour ne pas que le script soit executé directement, mais à la suite
                        dataType: 'html'
                    }) );
                });
            });

            // Execution de chaque appel asynchrone
            $.when.apply($, deferreds).then(function() {
                // On boucle sur chaque appel effectué pour traiter le résultat
                $.each(arguments, function(index, deferred) {
                    // Mapping des éléments modulo 2 : 0 = HTML, 1 = JS
                    if ( index % 2 === 0 ) {
                        // L'élement est un HTML ; ajout de celui-ci à la vue
                        $('#main-container').append(deferred[0]);
                    } else {
                        // L'élément est un JS ; exécution de celui-ci
                        eval(deferred[0]);
                    }
                });

                // Initialisation de packery
                _initPackery();
            });
        }
    };

    return self;
})();