angular.module('tbsaApp.company', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
    $routeProvider.when('/companies', {
        templateUrl: '/static/partials/company.html',
        controller: 'companyCtrl',
        controllerAs: 'company'
    });
}])

.controller('companyCtrl', [function(){
    
}]);
