angular.module('hardcarryApp.nobelPrizes', ['ngRoute'])

.controller('nobelPrizesCtrl', [function() {

}])

.directive('stuff', function() {

	return {
		restrict: "E",    

		link: function(scope, elem, attrs) {

			var refresh = $('#refresh'),
				slider = $('#slider')[0],
				lowerValue = $('#lower-value')[0],
				upperValue = $('#upper-value')[0],
				categoryElem = $('#category')[0],
				worldMap = $('#world-map'),
				display = $('#display');

			var drawMap = function() {

				worldMap.empty();

				// Construct request
				var requestURL = 'http://104.130.226.110:5000/api/prize?q={%22filters%22:[{%22name%22:%22year%22,%22op%22:%22>=%22,%22val%22:'
				        + lowerValue.innerHTML + '},{%22name%22:%22year%22,%22op%22:%22<=%22,%22val%22:' + upperValue.innerHTML + '}';
				
				// console.log(categoryElem[0].options);
				var selectedCategory = categoryElem.options[categoryElem.selectedIndex].value;
				if (selectedCategory !== 'all') {
				  requestURL += ',{"name":"category","op":"==","val":"' + selectedCategory + '"}';
				}
				requestURL += ']}';

				// Execute request
				$.ajax({
					url: requestURL, 
					type: 'GET',
					crossDomain: true,
					dataType: 'jsonp',
					success: function( results ) {
						var prizeGeoData = [];

						$.each(results.data.objects, function(key, val) {
							$.each(val.laureates, function(key, val) {
								if (val.country_id in prizeGeoData) {
									prizeGeoData[val.country_id] += 1;
								} else {
									prizeGeoData[val.country_id] = 1;
								}
							});
						});

					    worldMap.vectorMap({
							map: 'world_mill_en',
							series: {
								regions: [{
									values: prizeGeoData,
									scale: ['#C8EEFF', '#0071A4'],
									normalizeFunction: 'polynomial'
								}]
							},
							onRegionTipShow: function(e, el, code){
								if (!(code in prizeGeoData)) {
									prizeGeoData[code] = 0;
								}
								el.html(el.html()+' (# Prize Winners - '+prizeGeoData[code]+')');
							}
						});
			  		}
				});
			}

			drawMap();

			// Refresh button
			refresh.bind('mouseup', drawMap);

			// Init year slider
			noUiSlider.create(slider, {
				start: [1901, 2015],
				step: 1,
				behavior: 'drag-tap',
				connect: true,
				range: {
				  'min': 1901,
				  'max': 2015
				}
			});

			slider.noUiSlider.on('update', function ( values, handle ) {
				if ( !handle ) {
				  lowerValue.innerHTML = parseInt(values[handle]);
				} else {
				  upperValue.innerHTML = parseInt(values[handle]);
				}
			});
		}
	};
});
