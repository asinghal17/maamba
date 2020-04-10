$(document).ready(function() {
  $('#headerVideoLink').magnificPopup({
    type:'inline',
    midClick: true // Allow opening popup on middle mouse click. Always set it to true if you don't provide alternative source in href.
  });         
});


$("#headerPopup").on('hidden.bs.modal', function (e) {
    $("#headerPopup iframe").attr("src", $("#headerPopup iframe").attr("src"));
});