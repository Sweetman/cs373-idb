angular.module('hardcarryApp.featuredGameTable', [])

.controller('featuredGameTableCtrl', ['$scope', 'hcData', function($scope, hcData){
    hcData.getFeaturedGames()
        .success(function(response){
            $scope.featuredGameTable.tableData = response;
        });
}]);
