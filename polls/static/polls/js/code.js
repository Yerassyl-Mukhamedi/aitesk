$(document).ready(function() {
	$('.nav').click(function() {
		$('#nav-icon1,#nav-icon2,#nav-icon3,#nav-icon4').toggleClass('open');
		$('.slide-titan').toggleClass('active');
	});
	$('.slide-closer').click(function() {
		$('#nav-icon3').toggleClass('open');
		$('.slide-titan').toggleClass('active');
	});
	$('.closer').click(function() {
		$('#nav-icon3').toggleClass('open');
		$('.slide-titan').toggleClass('active');
	});
	// var total_period = 246;
	// var current_period = 0;
	// var txt = 0;
	// var cash = 52346;
	// for (i = 0; i < total_period; i++) {
	// 	txt = txt + cash * (1 / Math.pow(1.138, current_period));
	// 	current_period = current_period + 1;
	// 	console.log('Year ' + i + ' amount ' + txt);
	// }
	$('.katalog-definer').click(function() {
		localStorage.setItem('katalog-id', this.id);
		document.getElementById('result').innerHTML = localStorage.getItem('katalog-id');
		console.log(localStorage.getItem('katalog-id'));
	});

	$('.katalog').removeClass('active');
	var current = localStorage.getItem('katalog-id');
	$('.katalog' + current).addClass('active');
});
