angular.module('hardcarryApp.champion', ['ngRoute'])

.controller('championCtrl', ["$scope", "$routeParams", "$http", "$location", function($scope, $routeParams, $http, $location){
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
    this.goToSummoner = function(id){
        $location.path("/summoners/" + id); // path not hash
    };
    this.goToFeaturedGame = function(id){
        $location.path("/featuredGames/" + id); // path not hash
    };
    this.goToChampion = function(id){
        $location.path("/champions/" + id); // path not hash
    };
}]);
