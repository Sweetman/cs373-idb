angular.module('tbsaApp.home', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
    $routeProvider.when('/', {
        templateUrl: '/static/partials/home.html',
        controller: 'homeCtrl',
        controllerAs: 'home'
    });
}])

.controller('homeCtrl', [function(){
    this.greeting = "konichiwa";
}]);
