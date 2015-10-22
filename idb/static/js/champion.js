angular.module('tbsaApp.champion', ['ngRoute'])

.controller('championCtrl', [function(){
    this.tableData = [{name: "Lee Sin",  id: 1, description: "The Blind Monk"},
                      {name: "Teemo",    id: 2, description: "The Swift Scout"},
                      {name: "Renekton", id: 3, description: "The Butcher of the Sands"}];
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
