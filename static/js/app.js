angular.module('hardcarryApp', [
    'ngRoute',
    'ngSanitize',
    'hardcarryApp.home',
    'hardcarryApp.championTable',
    'hardcarryApp.summonerTable',
    'hardcarryApp.featuredGameTable',
    'hardcarryApp.champion',
    'hardcarryApp.summoner',
    'hardcarryApp.featuredGame',
    'hardcarryApp.about'
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
        .when('/tests/runTests', {
            templateUrl: '/tests/runTests'
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
            templateUrl: '/static/partials/champion.html',
            controller: "championCtrl",
            controllerAs: 'champion',
            activeTab: "Champions"
        })
        .when('/summoners/:id', {
            templateUrl: '/static/partials/summoner.html',
            controller: "summonerCtrl",
            controllerAs: 'summoner',
            activeTab: 'Summoners'
        })
        .when('/featuredGames/:id', {
            templateUrl: '/static/partials/featuredGame.html',
            controller: "featuredGameCtrl",
            controllerAs: 'featuredGame',
            activeTab: 'Featured Games'
        })
        .when('/api/:api*', {
        })
  
        .otherwise({redirectTo: '/'});
        
    $locationProvider.html5Mode(true);
}])

.controller('indexCtrl', ['$scope', '$route', function($scope, $route){
    $scope.$route = $route;
    $scope.range = function(n){
        var ans = [];
        for(var i = 0; i < n; i += 1){
            ans.push(i);
        }
        return ans;
    };
}])

.filter('trusted', ['$sce', function ($sce) {
    return function(url) {
        return $sce.trustAsResourceUrl(url);
    };
}]);
