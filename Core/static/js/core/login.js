$(function() {

    // Initialisation de Milkshake en mode non-connecté
    MilkShake.init({
        isUserLoggedIn: false
    });

    // Gestion du submit du formulaire de login pour le rendre AJAX
    $("#core-login").on("submit", function(e) {
        e.preventDefault();

        MilkShake.ajaxFormValidation({
            url: "doLogin",
            form: $(this),
            success: function() { document.location.reload(); }
        })
    });

});