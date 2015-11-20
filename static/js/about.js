angular.module('hardcarryApp.about', ['ngRoute'])

.controller('aboutCtrl', [function(){
    this.teamMembers = [{id: 1, name: "Kevin Lin", commits: 60, issues: 68, responsibility: "Javascript", unitTests: 2, bio: "Kevin enjoys biking and having fun in the sun!"},
                        {id: 2, name: "James Sweetman", commits: 29, issues: 37, responsibility: "Back-End", unitTests: 2, bio: "James is an aesthetic god who puts the sweet in Sweetman."},
                        {id: 3, name: "Hanah Luong", commits: 44, issues: 54, responsibility: "Front-End", unitTests: 2, bio: "Hanah hates long walks in the park, flowers, and ugly cats."},
                        {id: 4, name: "Jeffrey Li", commits: 63, issues: 70, responsibility: "Full-Stack", unitTests: 2, bio: "Jeffrey enjoys long walks in the park, flowers, and cute dogs."},
                        {id: 5, name: "Clinton Burgos", commits: 28, issues: 34, responsibility: "Full-Stack", unitTests: 4, bio: "Clint Burgos is just this guy, you know? He’s from Boston, likes to write music, and likes to code, obviously. He is currently studying CS at UT Austin."}];
}]);
