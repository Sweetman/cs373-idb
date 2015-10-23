angular.module('tbsaApp.ability', ['ngRoute'])

.controller('abilityCtrl', [function(){
    this.tableData = [{name: "Tempest",       id: 1, champion: "Lee Sin"},
                      {name: "Blinding Dart", id: 2, champion: "Teemo"},
                      {name: "Cull the Meek", id: 3, champion: "Renekton"}];
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
