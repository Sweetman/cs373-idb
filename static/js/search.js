angular.module('hardcarryApp.search', ['ngRoute'])

.controller('searchCtrl', ["$scope", "$routeParams", "$http", "$location", function($scope, $routeParams, $http, $location){
    this.query = $routeParams.query;
    $http.get("/api/search/" + this.query)
        .success(function(response){
            $scope.results = response;
            console.log(response);
        });
    console.log($routeParams.query);
    // console.log($scope.results);
    // console.log($scope.results.champions);
    // console.log($scope.champion.data);
    // this.goToSummoner = function(id){
    //     $location.path("/summoners/" + id); // path not hash
    // };
    // this.goToFeaturedGame = function(id){
    //     $location.path("/featuredGames/" + id); // path not hash
    // };
    // this.goToChampion = function(id){
    //     $location.path("/champions/" + id); // path not hash
    // };
}]);
