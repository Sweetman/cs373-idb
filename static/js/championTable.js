angular.module('hardcarryApp.championTable', [])

.controller('championTableCtrl', ['$scope', 'hcData', function($scope, hcData){
    hcData.getChampions()
        .success(function(response){
            $scope.championTable.tableData = response;
        });
}]);
