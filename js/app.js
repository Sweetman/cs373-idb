angular.module('tbsaApp', ['ngRoute', 'tbsaApp.home'])

.config(['$routeProvider', function($routeProvider){
    $routeProvider.otherwise({redirectTo: '/'});
}])

.controller('indexCtrl', ['$scope', function($scope){
    
}]);