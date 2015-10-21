angular.module('tbsaApp.founder', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
    $routeProvider.when('/founders', {
        templateUrl: '/static/partials/founder.html',
        controller: 'founderCtrl',
        controllerAs: 'founder'
    });
}])

.controller('founderCtrl', [function(){
    
}]);
