angular.module('hardcarryApp.featuredGame', ['ngRoute'])

.controller('featuredGameCtrl', ["$scope", "$routeParams", "$http", function($scope, $routeParams, $http){
    this.id = $routeParams.id;
    $http.get("/api/featured-games/" + this.id)
        .success(function(response){
            $scope.featuredGame.data = response;
        });
}]);
