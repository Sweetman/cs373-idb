angular.module('hardcarryApp.summoner', ['ngRoute'])

.controller('summonerCtrl', ["$scope", "$routeParams", "$http", function($scope, $routeParams, $http){
    this.id = $routeParams.id;
    $http.get("/api/summoners/" + this.id)
        .success(function(response){
            $scope.summoner.data = response;
        });
}]);
