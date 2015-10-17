angular.module('tbsaApp', ['ngRoute'])
.controller('indexCtrl', ['$scope', function($scope){
    $scope.greeting = "konichiwa";
}]);