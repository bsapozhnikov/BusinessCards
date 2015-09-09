$(document).ready(function(){
    $('#new-card-form').hide();
    $('#open-new-card-form').on('click',function(){
	$('#new-card-form').slideToggle();
	$('.new-card-form').hide();
	$('#new-card-form-person').show();
    });
    $('.new-card-type').on('click',function(){
	$('.new-card-type').css('border','none');
	$(this).css('border','solid 1px #48f');
	var formType = $(this).attr('id');
	$('.new-card-form').hide();
	$('#new-card-form-'+formType).show();
    });
});
