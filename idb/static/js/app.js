angular.module('tbsaApp', [
    'ngRoute',
    'tbsaApp.home',
    'tbsaApp.company',
    'tbsaApp.founder',
    'tbsaApp.investor'
    ])

.config(['$routeProvider', function($routeProvider){
    $routeProvider.otherwise({redirectTo: '/'});
}])

.controller('indexCtrl', ['$scope', function($scope){

}]);