angular.module('tbsaApp', [
    'ngRoute',
    'tbsaApp.home',
    'tbsaApp.company',
    'tbsaApp.founder',
    'tbsaApp.investor'
    ])

.config(['$routeProvider', '$locationProvider', function($routeProvider, $locationProvider){
    $routeProvider
        .when('/', {
            templateUrl: '/static/partials/home.html',
            controller: 'homeCtrl',
            controllerAs: 'home'
        })
        .when('/companies', {
            templateUrl: '/static/partials/company.html',
            controller: 'companyCtrl',
            controllerAs: 'company'
        })
        .when('/founders', {
            templateUrl: '/static/partials/founder.html',
            controller: 'founderCtrl',
            controllerAs: 'founder'
        })
        .when('/investors', {
            templateUrl: '/static/partials/investor.html',
            controller: 'investorCtrl',
            controllerAs: 'investor'
        })
        .otherwise({redirectTo: '/'});
        
    $locationProvider.html5Mode(true);
}])

.controller('indexCtrl', ['$scope', function($scope){

}]);