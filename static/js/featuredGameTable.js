angular.module('hardcarryApp.featuredGameTable', [])

.controller('featuredGameTableCtrl', ['$scope', "$http", "$location", function($scope, $http, $location){
    $http.get("/api/featured-games")
        .success(function(response){
            $scope.featuredGameTable.tableData = response;
        });
    this.order = "id";
    this.orderReverse = false;
    this.changeOrderTo = function(newOrder) {
        if(this.order === newOrder){
            this.orderReverse = ! this.orderReverse;
        }
        else {
            this.orderReverse = false;
        }
        this.order = newOrder;
    };
    this.goToFeaturedGame = function(id){
        $location.path("/featuredGames/" + id); // path not hash
    };
}]);
