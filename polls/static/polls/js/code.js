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

	var map;

	DG.then(function() {
		map = DG.map('map', {
			center: [ 43.25, 76.86 ],
			zoom: 14
		});

		DG.marker([ 43.25, 76.86 ]).addTo(map);
	});

	$('.modal-open-call').click(function() {
		$('.modals').addClass('open');
		$('.call-modal').addClass('active');
		document.body.style.overflowY = 'hidden';
	});
	$('.modal-open-order').click(function() {
		$('.modals').addClass('open');
		$('.order-modal').addClass('active');
		document.body.style.overflowY = 'hidden';
	});
	$('.modal-close').click(function() {
		$('.custom-modal').removeClass('active');
		$('.modals').removeClass('open');
		document.body.style.overflowY = 'auto';
	});

	var node = document.getElementById('product-name');
	htmlContent = node.innerHTML;
	document.getElementById('id_name1').value = htmlContent;
});
