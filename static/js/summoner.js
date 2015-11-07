angular.module('hardcarryApp.summoner', ['ngRoute'])

.controller('summonerCtrl', ["$scope", "$routeParams", "$http", "$location", function($scope, $routeParams, $http, $location){
    this.id = $routeParams.id;
    $http.get("/api/summoners/" + this.id)
        .success(function(response){
            $scope.summoner.data = response;
        });
    $http.get("/api/summoners/" + this.id + "/champions")
        .success(function(response){
            $scope.summoner.champions = response;
        });
    $http.get("/api/summoners/" + this.id + "/featured-games")
        .success(function(response){
            $scope.summoner.featuredGames = response;
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
