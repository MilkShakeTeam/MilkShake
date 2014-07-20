$(function() {
    $("#core-login").on("submit", function(e) {
        e.preventDefault();

        formValidation({
            url: "doLogin",
            form: $(this),
            success: function() {
                document.location.reload();
            }
        })
    });
});


// A placer dans une classe utilitaire
formValidation = function(params) {
    // C'est facile c'est que du mapping
    params = params || {};
    params.url = params.url || "";
    params.data = (params.form && params.form.serialize()) || null;
    params.success = params.success || null;
    params.error = params.error || null;

    $(".form-group", params.form).removeClass("has-error");
    $(".error-container", params.form).addClass("hidden");
    $(".error-container > ul").empty();

    $.ajax({
        url: params.url,
        method: "POST",
        dataType: "json",
        data: params.data,
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
    })
};