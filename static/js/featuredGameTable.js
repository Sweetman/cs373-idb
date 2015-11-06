angular.module('hardcarryApp.featuredGameTable', [])

.controller('featuredGameTableCtrl', ['$scope', "$http", function($scope, $http){
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
}]);
