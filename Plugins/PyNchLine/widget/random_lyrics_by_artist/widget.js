$("#random-lyrics-by-artist-form").on("submit", function(e) {
    e.preventDefault();
    $("#random-lyrics-by-artist-form input[type=submit]").attr("disabled", "disabled");

    $.get("/plugin/pynchline/getRandomLyricsByArtist", {
        artist: $("#random-lyrics-by-artist-artist").val()
    }, function(response) {
        if ( response.success ) {
            $("#random-lyrics-by-artist-lyrics").empty();
            $.each(response.data.lyrics, function(index, line) {
                $("#random-lyrics-by-artist-lyrics").append("<p>" + line + "</p>");
            })
        }

        $("#random-lyrics-by-artist-form input[type=submit]").removeAttr("disabled");
    });
})