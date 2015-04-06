$("#lyrics-by-search-terms-form").on("submit", function(e) {
    e.preventDefault();
    $("#lyrics-by-search-terms-form input[type=submit]").attr("disabled", "disabled");

    $.get("/plugin/pynchline/getLyricsBySearchTerms", {
        search: $("#lyrics-by-search-terms-search").val()
    }, function(response) {
        if ( response.success ) {
            $("#lyrics-by-search-terms-lyrics").empty();
            $.each(response.data.lyrics, function(index, line) {
                $("#lyrics-by-search-terms-lyrics").append("<p>" + line + "</p>");
            })
        }

        $("#lyrics-by-search-terms-form input[type=submit]").removeAttr("disabled");
    });
})