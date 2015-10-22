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
            activeTab: ''
        })
        .when('/champions', {
            templateUrl: '/static/partials/championsTable.html',
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
        .when('/champions/1', {
            templateUrl: '/static/partials/champion.html',
            activeTab: "Champions"
        })
  
        .otherwise({redirectTo: '/'});
        
    $locationProvider.html5Mode(true);
}])

.controller('indexCtrl', ['$scope', '$route', function($scope, $route){
    $scope.$route = $route;
}]);