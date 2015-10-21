angular.module('tbsaApp.founder', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
    $routeProvider.when('/founders', {
        templateUrl: 'partials/founder.html',
        controller: 'founderCtrl',
        controllerAs: 'founder'
    });
}])

.controller('founderCtrl', [function(){
    
}]);
