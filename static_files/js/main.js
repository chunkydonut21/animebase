$(function () {
    $("#id-input").autocomplete({
        source: function (request, response) {
            $.ajax({
                url: "/anime/search/",
                data: {q: request.term},
                dataType: "json",
                success: response,
                error: function () {
                    response([]);
                }
            })
        },
        minLength: 2,

        select: function (e, ui) {

            location.href = `/anime/${ui.item.value}`
        },

        change: function (e, ui) {

            alert("changed!");
        }
    })
});

