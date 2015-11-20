angular.module('hardcarryApp.search', ['ngRoute'])

.controller('searchCtrl', ["$scope", "$routeParams", "$http", "$location", function($scope, $routeParams, $http, $location){
    this.query = $routeParams.query;
    $http.get("/api/search/" + this.query)
        .success(function(response){
            console.log(response);
            $.each(response, function(i, type) {
            	$.each(type, function(j, item) {
            		if (i === 'champions') {
            			item.context = item.lore;
            			console.log("yes");
            		}
            	});
            });
            console.log(response);
            $scope.results = response;
        });
}]);
