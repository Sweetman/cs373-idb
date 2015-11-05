angular.module('hardcarryApp.summonerTable', [])

.controller('summonerTableCtrl', [function(){
    this.tableData = [{name: "Tempest",       id: 1, champion: "Lee Sin",  cooldownBurn: "10", costBurn: "50", costType: "Energy", maxRank: "18", rangeBurn: "425"},
                      {name: "Blinding Dart", id: 2, champion: "Teemo",    cooldownBurn: "8", costBurn: "70/80/90/100/110", costType: "Mana", maxRank: "18", rangeBurn: "680"},
                      {name: "Cull the Meek", id: 3, champion: "Renekton", cooldownBurn: "8", costBurn: "60/90/120/150/180", costType: "Fury", maxRank: "5", rangeBurn: "225"}];
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
