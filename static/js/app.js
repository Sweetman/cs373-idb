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
    'hardcarryApp.about',
    'hardcarryApp.nobelPrizes'
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
        .when('/nobelPrizes', {
            templateUrl: '/static/partials/nobelPrizes.html',
            controller: 'nobelPrizesCtrl',
            controllerAs: 'nobelPrizes',
            activeTab: 'Nobel Prizes Map'
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
        .when('/tests/runTests', {
            templateUrl: '/tests/runTests'
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

.factory('hcLocation', ['$location', function($location){
    var service = {};

    service.goToChampion = function(id){
        $location.path("/champions/" + id); // path not hash
    };
    service.goToSummoner = function(id){
        $location.path("/summoners/" + id); // path not hash
    };
    service.goToSummoner = function(id){
        $location.path("/featuredGames/" + id); // path not hash
    };

    return service;
}])

.factory('hcData', ['$http', function($http){
    var service = {};
    service.getChampions = function(){
        return $http.get("/api/champions", {cache: true});
    };
    return service;
}])

.directive('hcTable', [function(){
    return {
        restrict: 'E',
        scope: {
            data: '=hcData',
            initialOrder: '=hcOrder',
            atts: '=hcAtts',
            goToItem: '&hcGoToItem'
        },
        controller: ['$scope', 'hcLocation', function($scope, hcLocation){
            $scope.order = $scope.initialOrder;
            $scope.orderReverse = false;
            $scope.itemId = $scope.atts[0].id;
            $scope.changeOrderTo = function(newOrder){
                if(this.order === newOrder){
                    this.orderReverse = ! this.orderReverse;
                }
                else {
                    this.order = newOrder;
                    this.orderReverse = false;
                }
            };
        }],
        templateUrl: '/static/directiveTemplates/tableTemplate.html'
    };
}])

.directive('hcChampionTable', [function(){
    return {
        restrict: 'E',
        scope: {
            data: '=hcData',
        },
        controller: ['$scope', 'hcLocation', function($scope, hcLocation){
            $scope.order = "championId";
            $scope.goToChampion = hcLocation.goToChampion;
            $scope.atts = [{id: 'championId', name: 'ID'},
                           {id: 'name', name: 'Name'},
                           {id: 'attack', name: 'Attack'},
                           {id: 'defense', name: 'Defense'},
                           {id: 'difficulty', name: 'Difficulty'},
                           {id: 'magic', name: 'Magic'}];
        }],
        template: '<hc-table hc-data="data" hc-order="\'championId\'" hc-atts="atts" hc-go-to-item="goToChampion(id)"></hc-table>'
    };
}])

.directive('summonerTable', [function(){
    return {
        restrict: 'E',
        scope: {
            data: '=hcData',
        },
        templateUrl: '/static/directiveTemplates/championTableTemplate.html'
    };
}])

.directive('featuredGameTable', [function(){
    return {
        restrict: 'E',
        scope: {
            data: '=hcData',
        },
        templateUrl: '/static/directiveTemplates/championTableTemplate.html'
    };
}])

.filter('trusted', ['$sce', function ($sce) {
    return function(url) {
        return $sce.trustAsResourceUrl(url);
    };
}])

.filter('objectToArray', function() {
    return function(input) {
      var ans = []; 
      for(var key in input){
        if(input.hasOwnProperty(key)){
            ans.push(input[key]);
        }
      }
      return ans;
    };
});
