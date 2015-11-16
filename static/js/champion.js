angular.module('hardcarryApp.champion', ['ngRoute'])

.controller('championCtrl', ["$scope", "$routeParams", "$http", "$location", function($scope, $routeParams, $http, $location){
    this.id = $routeParams.id;
    $http.get("/api/champions/" + this.id)
        .success(function(response){
            $scope.champion.data = response;
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
