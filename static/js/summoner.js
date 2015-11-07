angular.module('hardcarryApp.summoner', ['ngRoute'])

.controller('summonerCtrl', ["$scope", "$routeParams", "$http", function($scope, $routeParams, $http){
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
}]);
