angular.module('tbsaApp.about', ['ngRoute'])

.controller('aboutCtrl', [function(){
    this.teamMembers = [{id: 1, name: "Kevin Lin", commits: 0, issues: 0, unitTests: 0, bio: "lorem ipsum"},
                        {id: 2, name: "James Sweetman", commits: 0, issues: 0, unitTests: 0, bio: "lorem ipsum"},
                        {id: 3, name: "Hanah Luong", commits: 0, issues: 0, unitTests: 0, bio: "lorem ipsum"},
                        {id: 4, name: "Jeffrey Li", commits: 0, issues: 0, unitTests: 0, bio: "lorem ipsum"},
                        {id: 5, name: "Clinton Burgos", commits: 0, issues: 0, unitTests: 0, bio: "lorem ipsum"}];
}]);
