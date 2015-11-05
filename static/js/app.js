angular.module('tbsaApp', [
    'ngRoute',
    'tbsaApp.home',
    'tbsaApp.championTable',
    'tbsaApp.summonerTable',
    'tbsaApp.featuredGameTable',
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
            templateUrl: '/static/partials/championTable.html',
            controller: 'championTableCtrl',
            controllerAs: 'championTable',
            activeTab: "Champions"
        })
        .when('/summoners', {
            templateUrl: '/static/partials/summonerTable.html',
            controller: 'summonerTableCtrl',
            controllerAs: 'summonerTable',
            activeTab: 'Summoners'
        })
        .when('/featuredGames', {
            templateUrl: '/static/partials/featuredGameTable.html',
            controller: 'featuredGameTableCtrl',
            controllerAs: 'featuredGameTable',
            activeTab: 'Featured Games'
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
            controller: "championCtrl",
            activeTab: "Champions"
        })
        .when('/summoners/:id', {
            templateUrl: function(params){
                return '/static/partials/summoner' + params.id + '.html';
            },
            controller: "summonerCtrl",
            activeTab: 'Summoners'
        })
        .when('/featuredGames/:id', {
            templateUrl: function(params){
                return '/static/partials/featuredGame' + params.id + '.html';
            },
            controller: "featuredGameCtrl",
            activeTab: 'Featured Games'
        })
  
        .otherwise({redirectTo: '/'});
        
    $locationProvider.html5Mode(true);
}])

.controller('indexCtrl', ['$scope', '$route', function($scope, $route){
    $scope.$route = $route;
}]);