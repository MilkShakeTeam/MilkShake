var formValidator = new Parsley("#core-login");

$("#core-login").on("submit", function(e) {
    e.preventDefault();

    $(".message-container").removeClass("hidden alert-danger").addClass("alert-warning").html("<strong>Connexion en cours</strong><br/>Veuillez patienter...");
    if ( formValidator.validate() ) {
        $.ajax({
            url: "/login",
            method: "POST",
            dataType: "json",
            data: {
                csrfmiddlewaretoken: $.cookie('csrftoken'),
                username:  $("#username").val(),
                password:  $("#password").val()
            },
            success: function(response) {
                $(".message-container").removeClass("alert-warning").addClass("alert-success").html("<strong>Connexion reussie</strong><br/>Redirection en cours");
                document.location.reload();
            },
            error: function(jqXhr) {
                $(".message-container").removeClass("alert-warning").addClass("alert-danger").html("<strong>Impossible de se connecter</strong><br/>" + jqXhr.responseJSON.message);
            }
        })
    } else {
        $(".message-container").removeClass("alert-warning").addClass("alert-danger").html("<strong>Attention</strong><br/>Des erreurs sont survenues lors de la validation du formulaire.");
    }
});