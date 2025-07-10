$('#some-element').popover({
  html: true,
  content: function(){
    return $(this).data('content');
  }
});