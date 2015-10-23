angular.module('tbsaApp.ability', ['ngRoute'])

.controller('abilityCtrl', [function(){
    this.tableData = [{name: "Tempest",       id: 1, champion: "Lee Sin", cooldown_burn: "10", cost_burn: "50", cost_type: "Energy", max_rank: "18", range_burn: "425"},
                      {name: "Blinding Dart", id: 2, champion: "Teemo", cooldown_burn: "8", cost_burn: "70/80/90/100/110", cost_type: "Mana", max_rank: "18", range_burn: "680"},
                      {name: "Cull the Meek", id: 3, champion: "Renekton", cooldown_burn: "8", cost_burn: "60/90/120/150/180", cost_type: "Fury", max_rank: "5", range_burn: "225"}];
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
