angular.module('hardcarryApp.search', ['ngRoute'])

.controller('searchCtrl', ["$scope", "$routeParams", "$http", "$location", function($scope, $routeParams, $http, $location){
    this.query = $routeParams.query;
    $http.get("/api/search/" + this.query)
        .success(function(response){
            $scope.results = response;
        });
}]);
