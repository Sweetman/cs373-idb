angular.module('tbsaApp', [
    'ngRoute',
    'tbsaApp.home',
    'tbsaApp.champion',
    'tbsaApp.ability',
    'tbsaApp.item',
    'tbsaApp.about'
    ])

.config(['$routeProvider', '$locationProvider', function($routeProvider, $locationProvider){
    $routeProvider
        .when('/', {
            templateUrl: '/static/partials/home.html',
            controller: 'homeCtrl',
            controllerAs: 'home',
            activeTab: ''
        })
        .when('/champions', {
            templateUrl: '/static/partials/championsTable.html',
            controller: 'championCtrl',
            controllerAs: 'champion',
            activeTab: "Champions"
        })
        .when('/abilities', {
            templateUrl: '/static/partials/abilitiesTable.html',
            controller: 'abilityCtrl',
            controllerAs: 'ability',
            activeTab: 'Abilities'
        })
        .when('/items', {
            templateUrl: '/static/partials/itemsTable.html',
            controller: 'itemCtrl',
            controllerAs: 'item',
            activeTab: 'Items'
        })
        .when('/about', {
            templateUrl: '/static/partials/about.html',
            controller: 'aboutCtrl',
            controllerAs: 'about',
            activeTab: 'About'
        })
        .when('/champions/:id', {
            templateUrl: function(params){
                return '/static/partials/champion' + params.id + '.html';
            },
            activeTab: "Champions"
        })
        .when('/abilities/:id', {
            templateUrl: function(params){
                return '/static/partials/ability' + params.id + '.html';
            },
            activeTab: 'Abilities'
        })
        .when('/items/:id', {
            templateUrl: function(params){
                return '/static/partials/item' + params.id + '.html';
            },
            activeTab: 'Items'
        })
  
        .otherwise({redirectTo: '/'});
        
    $locationProvider.html5Mode(true);
}])

.controller('indexCtrl', ['$scope', '$route', function($scope, $route){
    $scope.$route = $route;
}]);