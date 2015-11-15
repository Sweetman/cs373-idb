angular.module('hardcarryApp.championTable', [])

.controller('championTableCtrl', ['$scope', 'tbsaData' , function($scope, tbsaData){
    tbsaData.getChampions()
        .success(function(response){
            $scope.championTable.tableData = response;
        });
}]);
