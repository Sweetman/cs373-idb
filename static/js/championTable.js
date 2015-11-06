angular.module('hardcarryApp.championTable', [])

.controller('championTableCtrl', ["$scope", "$http", function($scope, $http){
    $http.get("/api/champions")
        .success(function(response){
            $scope.championTable.tableData = response;
        });
    this.order = "championId";
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
