$(document).ready(function() {

var deleteBtn = $('.delete-btn');
$(deleteBtn).on('click', function(e) {

  e.preventDefault();

  var delLink = $(this).attr('href');
  var result = confirm('Você realmente quer deletar essa tarefa?');

  if(result){
    window.location.href = delLink;
  }


});

});