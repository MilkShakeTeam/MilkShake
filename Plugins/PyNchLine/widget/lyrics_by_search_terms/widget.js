$("#random-punchline-by-artist-form").on("submit", function(e) {
    e.preventDefault();
    $("#random-punchline-by-artist-form input[type=submit]").attr("disabled", "disabled");

    $.get("/plugin/pynchline/getRandomPunchlineByArtist?", {
        artist: $("#random-punchline-by-artist-artist").val()
    }, function(response) {
        if ( response.success ) {
            $("#random-punchline-by-artist-song").text("[" + response.data.song_name + "]");
            $("#random-punchline-by-artist-punchline").text(response.data.punchline);
        }

        $("#random-punchline-by-artist-form input[type=submit]").removeAttr("disabled");
    });
})