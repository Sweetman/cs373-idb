angular.module('hardcarryApp.tests', ['ngRoute'])

.controller('testsCtrl', function ($http, $scope, $location) {
	$scope.results = "Click button to run tests (please have patience)";

	$scope.runTests = function() {
		$http.get('/tests/runTests').then(function(response) {
					$scope.results = response.data.results;
                }, function(response){
                	console.log("failed to run tests");
                	$scope.results = "Failed to run tests. Uh oh";
                });
	};
});