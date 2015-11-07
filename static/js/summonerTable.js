angular.module('hardcarryApp.summonerTable', [])

.controller('summonerTableCtrl', ["$scope", "$http", "$location", function($scope, $http, $location){
    $http.get("/api/summoners")
        .success(function(response){
            $scope.summonerTable.tableData = response;
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
    this.goToSummoner = function(id){
        $location.path("/summoners/" + id); // path not hash
    };
}]);
