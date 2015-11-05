angular.module('hardcarryApp.championTable', ['ngRoute'])

.controller('championTableCtrl', [function(){
    this.tableData = [{name: "Lee Sin",  id: 1, description: "The Blind Monk", attack: "8", defense: "5", difficulty: "6", magic: "3"},
                      {name: "Teemo",    id: 2, description: "The Swift Scout", attack: "5", defense: "3", difficulty: "6", magic: "7"},
                      {name: "Renekton", id: 3, description: "The Butcher of the Sands", attack: "8", defense: "5", difficulty: "3", magic: "2"}];
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
