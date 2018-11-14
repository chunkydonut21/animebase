$(function() {
  $("#drugs").autocomplete({
    source: "/anime/search/",
    minLength: 2,
  });
});