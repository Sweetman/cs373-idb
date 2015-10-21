angular.module('tbsaApp.investor', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
    $routeProvider.when('/investors', {
        templateUrl: 'partials/investor.html',
        controller: 'investorCtrl',
        controllerAs: 'investor'
    });
}])

.controller('investorCtrl', [function(){
    
}]);
