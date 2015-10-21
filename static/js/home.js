angular.module('tbsaApp.home', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
    $routeProvider.when('/', {
        templateUrl: 'partials/home.html',
        controller: 'homeCtrl',
        controllerAs: 'home'
    });
}])

.controller('homeCtrl', [function(){
    this.greeting = "konichiwa";
}]);
