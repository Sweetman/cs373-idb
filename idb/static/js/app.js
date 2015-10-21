angular.module('tbsaApp', [
    'ngRoute',
    'tbsaApp.home',
    'tbsaApp.champion',
    'tbsaApp.ability',
    'tbsaApp.item'
    ])

.config(['$routeProvider', '$locationProvider', function($routeProvider, $locationProvider){
    $routeProvider
        .when('/', {
            templateUrl: '/static/partials/home.html',
            controller: 'homeCtrl',
            controllerAs: 'home',
            activeTab: 'Home'
        })
        .when('/champions', {
            templateUrl: '/static/partials/champion.html',
            controller: 'championCtrl',
            controllerAs: 'champion',
            activeTab: "Champions"
        })
        .when('/abilities', {
            templateUrl: '/static/partials/ability.html',
            controller: 'abilityCtrl',
            controllerAs: 'ability',
            activeTab: 'Abilities'
        })
        .when('/items', {
            templateUrl: '/static/partials/item.html',
            controller: 'itemCtrl',
            controllerAs: 'item',
            activeTab: 'Items'
        })
        .otherwise({redirectTo: '/'});
        
    $locationProvider.html5Mode(true);
}])

.controller('indexCtrl', ['$scope', '$route', function($scope, $route){
    $scope.$route = $route;
}]);