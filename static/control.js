$(document).ready(function(){
    $('#new-card-form').hide();
    $('#open-new-card-form').on('click',function(){
	$('#new-card-form').slideToggle();
    });
});
