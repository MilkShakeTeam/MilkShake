// AjaxSetup global a l'application
$(function() {
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            // Gestion de l'application du token CSRF lors des requêtes qui en valent la peine
            if ( !(/^(GET|HEAD|OPTIONS|TRACE)$/.test(settings.type)) && !this.crossDomain ) {
                xhr.setRequestHeader("X-CSRFToken", $.cookie("csrftoken"));
            }
        }
    });
});