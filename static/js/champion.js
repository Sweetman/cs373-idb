angular.module('hardcarryApp.champion', ['ngRoute'])

.controller('championCtrl', ["$scope", "$routeParams", "$http", function($scope, $routeParams, $http){
    this.id = $routeParams.id;
    $http.get("/api/champions/" + this.id)
        .success(function(response){
            $scope.champion.data = response;
        });
}]);
