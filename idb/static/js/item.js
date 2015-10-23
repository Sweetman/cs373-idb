angular.module('tbsaApp.item', ['ngRoute'])

.controller('itemCtrl', ['$scope', function($scope){
    this.tableData = [{name: "Lich Bane",         id: 1, cost: 3000},
                      {name: "The Bloodthirster", id: 2, cost: 3500},
                      {name: "Frozen Heart",      id: 3, cost: 2450}];
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
