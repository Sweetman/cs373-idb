angular.module('tbsaApp.about', ['ngRoute'])

.controller('aboutCtrl', [function(){
    this.teamMembers = [{id: 1, name: "Kevin Lin", commits: 24, issues: 0, responsibility: "Front-End", unitTests: 0, bio: "Kevin enjoys biking and having fun in the sun!"},
                        {id: 2, name: "James Sweetman", commits: 23, issues: 0, responsibility: "Back-End", unitTests: 0, bio: "James is an aesthetic god who puts the sweet in Sweetman."},
                        {id: 3, name: "Hanah Luong", commits: 20, issues: 2, responsibility: "Front-End", unitTests: 0, bio: "Hanah hates long walks in the park, flowers, and ugly cats."},
                        {id: 4, name: "Jeffrey Li", commits: 17, issues: 13, responsibility: "Full-Stack", unitTests: 0, bio: "Jeffrey enjoys long walks in the park, flowers, and cute dogs."},
                        {id: 5, name: "Clinton Burgos", commits: 20, issues: 3, responsibility: "Full-Stack", unitTests: 9, bio: "Clint Burgos is just this guy, you know? He’s from Boston, likes to write music, and likes to code, obviously. He is currently studying CS at UT Austin."}];
}]);
