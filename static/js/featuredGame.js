angular.module('hardcarryApp.featuredGame', ['ngRoute'])

.controller('featuredGameCtrl', ["$scope", "$routeParams", "$http", function($scope, $routeParams, $http){
    this.id = $routeParams.id;
    $http.get("/api/featuredGames/" + id)
        .success(function(response){
            $scope.champion.data = response;
        });
}]);
