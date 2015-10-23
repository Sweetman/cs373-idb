angular.module('tbsaApp.about', ['ngRoute'])

.controller('aboutCtrl', [function(){
    this.teamMembers = [{id: 1, name: "Kevin Lin"},
                        {id: 2, name: "James Sweetman"},
                        {id: 3, name: "Hanah Luong"},
                        {id: 4, name: "Jeffrey Li"},
                        {id: 5, name: "Clinton Burgos"}];
}]);
