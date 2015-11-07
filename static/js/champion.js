angular.module('hardcarryApp.champion', ['ngRoute'])

.controller('championCtrl', ["$scope", "$routeParams", "$http", function($scope, $routeParams, $http){
    this.id = $routeParams.id;
    $http.get("/api/champions/" + this.id)
        .success(function(response){
            $scope.champion.data = response;
        });
    $http.get("/api/champions/" + this.id + "/featured-games")
        .success(function(response){
            $scope.champion.featuredGames = response;
        });
    $http.get("/api/champions/" + this.id + "/summoners")
        .success(function(response){
            $scope.champion.summoners= response;
        });
}]);
