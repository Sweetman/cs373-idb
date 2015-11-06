angular.module('hardcarryApp.featuredGame', ['ngRoute'])

.controller('featuredGameCtrl', ["$scope", "$routeParams", "$http", function($scope, $routeParams, $http){
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
}]);
