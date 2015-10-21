angular.module('tbsaApp.investor', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
    $routeProvider.when('/investors', {
        templateUrl: '/static/partials/investor.html',
        controller: 'investorCtrl',
        controllerAs: 'investor'
    });
}])

.controller('investorCtrl', [function(){
    
}]);
