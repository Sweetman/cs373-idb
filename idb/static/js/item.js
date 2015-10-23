angular.module('tbsaApp.item', ['ngRoute'])

.controller('itemCtrl', ['$scope', function($scope){
    this.tableData = [{name: "Lich Bane",         id: 1, cost: 3000, base: "200", name_id: "212"},
                      {name: "The Bloodthirster", id: 2, cost: 3500, base: "200", name_id: "123"},
                      {name: "Frozen Heart",      id: 3, cost: 2450, base: "600", name_id: "234"}];
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
