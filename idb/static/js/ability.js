angular.module('tbsaApp.ability', ['ngRoute'])

.controller('abilityCtrl', [function(){
    this.tableData = [{name: "Tempest",       id: 1, champion: "Lee Sin"},
                      {name: "Blinding Dart", id: 2, champion: "Teemo"},
                      {name: "Cull the Meek", id: 3, champion: "Renekton"}];
    this.order = "id";
}]);
