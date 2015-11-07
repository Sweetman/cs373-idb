angular.module('hardcarryApp.featuredGame', ['ngRoute'])

.controller('featuredGameCtrl', ["$scope", "$routeParams", "$http", "$location", function($scope, $routeParams, $http, $location){
    this.id = $routeParams.id;
    $http.get("/api/featured-games/" + this.id)
        .success(function(response){
            $scope.featuredGame.data = response;
        });
    $http.get("/api/featured-games/" + this.id + "/summoners")
        .success(function(response){
            $scope.featuredGame.summoners = response;
        });
    $http.get("/api/featured-games/" + this.id + "/champions")
        .success(function(response){
            $scope.featuredGame.champions = response;
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
