angular.module('hardcarryApp.summonerTable', [])

.controller('summonerTableCtrl', ['$scope', 'hcData', function($scope, hcData){
    hcData.getSummoners()
        .success(function(response){
            $scope.summonerTable.tableData = response;
        });
}]);
