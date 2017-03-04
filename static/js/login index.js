$("button[type='submit']").click(function(e) {
  e.preventDefault();
  $(".login").parent().addClass("animate");
  
  setTimeout(function(){ 
    $(".loader").addClass("done");
      setTimeout(function(){ 
        $(".checkmark").addClass("show");
      }, 500);
  }, 5000);
});

$("button.remove").click(function(e) {
  e.preventDefault();
  $(".login").parent().removeClass("animate");
  $(".loader").removeClass("done");
  $(".checkmark").removeClass("show");
});