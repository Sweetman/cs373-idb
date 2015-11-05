angular.module('hardcarryApp.featuredGameTable', ['ngRoute'])

.controller('featuredGameTableCtrl', ['$scope', function($scope){
    this.tableData = [{name: "Lich Bane",         id: 1, cost: 3000, baseCost: 200, nameId: 212},
                      {name: "The Bloodthirster", id: 2, cost: 3500, baseCost: 200, nameId: 123},
                      {name: "Frozen Heart",      id: 3, cost: 2450, baseCost: 600, nameId: 234}];
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
