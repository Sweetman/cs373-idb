angular.module('hardcarryApp.championTable', [])

.controller('championTableCtrl', ["$scope", "$http", function($scope, $http){
    $http.get("/api/champions")
        .success(function(response){
            $scope.championTable.tableData = response;
        });
}]);
