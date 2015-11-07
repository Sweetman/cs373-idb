angular.module('hardcarryApp.championTable', [])

.controller('championTableCtrl', ["$scope", "$http", "$location", function($scope, $http, $location){
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
    this.goToChampion = function(id){
        $location.path("/champions/" + id); // path not hash
    };
}]);
