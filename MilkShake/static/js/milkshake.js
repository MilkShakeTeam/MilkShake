/**
 * Gestion des widgets de la page d'accueil
 */
var MilkShake = (function() {

    /**
     * URL de récupération des propriétés des plugins et widgets
     */
    var URL_PLUGINS_WIDGETS = "/pluginsAndWidgets";

    /**
     * Initialise les options en fonction des paramètres d'entrée
     *
     * @param object params Paramètres à initialiser
     * @private
     */
    var _initOptions = function(params) {
        params = params || {};

        self.isUserLoggedIn = typeof params.isUserLoggedIn  !== 'undefined' ? params.isUserLoggedIn : true;
        self.afterInit      = typeof params.afterInit  === 'function' ? params.afterInit : true;
    }

    /**
     * Setup jQuery
     *
     * @private
     */
    var _initJquery = function() {
        // Setup Ajax par défaut
        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                // Gestion de l'application du token CSRF lors des requêtes qui en valent la peine
                if ( !(/^(GET|HEAD|OPTIONS|TRACE)$/.test(settings.type)) && !this.crossDomain ) {
                    xhr.setRequestHeader("X-CSRFToken", $.cookie("csrftoken"));
                }
            }
        });
    };

    var self = {

        /**
         * Metadonnées des plugins et widgets de l'application
         */
        pluginsAndWidgetsData: null,

        /**
         * Initialisation principale de MilkShake
         */
        init: function(params) {
            // Initialisation des paramètres par défaut
            _initOptions(params);

            // Initialisation des setups/fonctions custom jQuery
            _initJquery();

            if ( this.isUserLoggedIn ) {
                // Récupération des données des plugins et widgets
                this.updatePluginsAndWidgetsData(function() {
                    // Initialisation de la SideBar
                    SideBar.init();

                    // Mise à jour des plugins de la SideBar
                    SideBar.updateUserPlugins();

                    // Appel du callback si celui-ci est défini
                    if ( MilkShake.afterInit && typeof MilkShake.afterInit === 'function' ) {
                        MilkShake.afterInit();
                    }
                });
            } else {
                // Appel du callback si celui-ci est défini
                if ( this.afterInit && typeof this.afterInit === 'function' ) {
                    this.afterInit();
                }
            }
        },

        /**
         * Récupère et met à jour la liste de l'intégralité des plugins et widgets de l'application
         *
         * @param function afterSuccess (optionnel) Callback après la mise à jour des plugins et widgets
         */
        updatePluginsAndWidgetsData: function(afterSuccess) {
            $.get(URL_PLUGINS_WIDGETS, function(response) {
                // Mise à jour des plugins et widgets locaux
                self.pluginsAndWidgetsData = response;

                // Appel du callback si celui-ci est défini
                if ( afterSuccess && typeof afterSuccess === 'function' ) {
                    afterSuccess();
                }
            });
        },

        /**
         * Gestion ajax de la validation des formulaires avec styles bootstrap
         */
        ajaxFormValidation: function(params) {
            // C'est facile c'est que du mapping
            params = params || {};
            params.url = params.url || "";
            params.data = (params.form && params.form.serialize()) || null;
            params.success = params.success || null;
            params.error = params.error || null;

            // Réinitialisation des classes du formulaire
            $(".form-group", params.form).removeClass("has-error");
            $(".error-container", params.form).addClass("hidden");
            $(".error-container > ul").empty();

            $.ajax({
                url: params.url,
                method: "POST",
                dataType: "json",
                data: params.data,
                beforeSend: function(xhr, settings) {
                    // Gestion de l'application du token CSRF lors des requêtes qui en valent la peine
                    if ( !(/^(GET|HEAD|OPTIONS|TRACE)$/.test(settings.type)) && !this.crossDomain ) {
                        xhr.setRequestHeader("X-CSRFToken", $.cookie("csrftoken"));
                    }
                },
                success: function(response) {
                    if ( params.success ) {
                        params.success(response);
                    }
                },
                error: function(jqXhr) {
                    // Bootstrap
                    if ( jqXhr.responseJSON.errors ) {
                        $.each(jqXhr.responseJSON.errors, function(index, element) {
                            if ( $('[name="' + index + '"]').length == 1 ) {
                                $('[name="' + index + '"]', params.form).closest("div.form-group").addClass("has-error");
                            } else {
                                if ( $(".error-container", params.form).length === 1 ) {
                                    $(".error-container").removeClass("hidden");
                                    $(".error-container > ul").append("<li>" + element + "</li>");
                                }
                            }
                        });
                    }

                    if ( params.error ) {
                        params.error(jqXhr);
                    }
                }
            });
        }
    };

    return self;
})();