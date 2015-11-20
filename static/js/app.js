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
    'hardcarryApp.search',
    'hardcarryApp.tests',
    'hardcarryApp.nobelPrizes',
    // 'hardcarryApp.httpServices',
    'angularUtils.directives.dirPagination'
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
        .when('/tests', {
            templateUrl: '/static/partials/tests.html',
            controller: 'testsCtrl',
            controllerAs: 'tests',
            activeTab: 'Unit Tests'
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
        .when('/search/:query', {
            templateUrl: '/static/partials/search.html',
            controller: 'searchCtrl',
            controllerAs: 'search',
            activeTab: 'Search'
        })
        .when('/api/:api*', {
        })
        .when('/tests/runTests', {
            templateUrl: '/tests/runTests'
        })
        .otherwise({redirectTo: '/'});
        
    $locationProvider.html5Mode(true);
}])

.controller('indexCtrl', ['$scope', '$route', '$location', function($scope, $route, $location){
    $scope.$route = $route;
    $scope.range = function(n){
        var ans = [];
        for(var i = 0; i < n; i += 1){
            ans.push(i);
        }
        return ans;
    };
    $scope.submitQuery = function(){
        $location.path("/search/" + $scope.query); // path not hash
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
    service.goToFeaturedGame = function(id){
        $location.path("/featuredGames/" + id); // path not hash
    };
    service.goToSearchRow = function(idTuple){
        $location.path("/" + idTuple.type + "/" + idTuple.id);
    };

    return service;
}])

.factory('hcData', ['$http', function($http){
    var service = {};
    service.getChampions = function(){
        return $http.get("/api/champions", {cache: true});
    };
    service.getSummoners = function(){
        return $http.get("/api/summoners", {cache: true});
    };
    service.getFeaturedGames = function(){
        return $http.get("/api/featured-games", {cache: true});
    };
    service.getSearchResults = function(query){
        return $http.get("/api/search" + query, {cache: true});
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
            $scope.itemId = $scope.initialOrder;
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
            $scope.goToItem = hcLocation.goToChampion;
            $scope.atts = [{id: 'championId', name: 'ID'},
                           {id: 'name', name: 'Name'},
                           {id: 'attack', name: 'Attack'},
                           {id: 'defense', name: 'Defense'},
                           {id: 'difficulty', name: 'Difficulty'},
                           {id: 'magic', name: 'Magic'}];
        }],
        template: '<hc-table hc-data="data" hc-order="order" hc-atts="atts" hc-go-to-item="goToItem(id)"></hc-table>'
    };
}])

.directive('hcSummonerTable', [function(){
    return {
        restrict: 'E',
        scope: {
            data: '=hcData',
        },
        controller: ['$scope', 'hcLocation', function($scope, hcLocation){
            $scope.order = "id";
            $scope.goToItem = hcLocation.goToSummoner;
            $scope.atts = [{id: 'id', name: 'ID'},
                           {id: 'name', name: 'Name'},
                           {id: 'bot', name: 'Bot'},
                           {id: 'summonerLevel', name: 'Summoner Level'},
                           {id: 'summoner_id', name: 'Summoner ID'}];
        }],
        template: '<hc-table hc-data="data" hc-order="order" hc-atts="atts" hc-go-to-item="goToItem(id)"></hc-table>'
    };
}])

.directive('hcFeaturedGameTable', [function(){
    return {
        restrict: 'E',
        scope: {
            data: '=hcData',
        },
        controller: ['$scope', 'hcLocation', function($scope, hcLocation){
            $scope.order = "id";
            $scope.goToItem = hcLocation.goToFeaturedGame;
            $scope.atts = [{id: 'id', name: 'ID'},
                           {id: 'game_mode', name: 'Game Mode'},
                           {id: 'gameLength', name: 'Game Length'},
                           {id: 'game_type', name: 'Game Type'},
                           {id: 'mapId', name: 'Map ID'}];
        }],
        template: '<hc-table hc-data="data" hc-order="order" hc-atts="atts" hc-go-to-item="goToItem(id)"></hc-table>'
    };
}])

.directive('hcSearchTable', [function(){
    return {
        restrict: 'E',
        scope: {
            data: '=hcData',
        },
        controller: ['$scope', 'hcLocation', function($scope, hcLocation){
            $scope.order = "id";
            $scope.goToItem = hcLocation.goToSearchRow;
            $scope.atts = [{id: 'type', name: 'Type'},
                           {id: 'name', name: 'Name'},
                           {id: 'context', name: 'Context'}];
        }],
        template: '<hc-table hc-data="data" hc-order="order" hc-atts="atts" hc-go-to-item="goToItem(id)"></hc-table>'
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
