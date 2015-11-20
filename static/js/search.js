angular.module('hardcarryApp.search', ['ngRoute'])

.controller('searchCtrl', ["$scope", "$routeParams", "$http", "$location", function($scope, $routeParams, $http, $location){
    $scope.searchData = [];

    function contextOfObject(obj, query){
        var ans = [];
        var contextOfObjectHelper = function(object){
            if(typeof object === 'object'){
                angular.forEach(object, function(value){
                    contextOfObjectHelper(value);
                });
            } else if(typeof object === 'string' || typeof object === 'boolean' ||
                      typeof object === 'number'){
                stringRep = String(object);
                if(stringRep.toLowerCase().indexOf(query.toLowerCase()) !== -1){
                    ans.push(stringRep);
                }
            }
        };
        contextOfObjectHelper(obj);
        return ans.join('\n');
    }

    $http.get("/api/search/" + $routeParams.query)
        .success(function(response){
            angular.forEach(response.champions, function(value){
                var row = {id: {type: 'champions', id: value.championId},
                           type: "Champion",
                           name: value.name,
                           context: contextOfObject(value, $routeParams.query)};
                $scope.searchData.push(row);
            });
            angular.forEach(response["featured-games"], function(value){
                var row = {id: {type: 'featuredGames', id: value.id},
                           type: "Featured Game",
                           name: value.game_type,
                           context: contextOfObject(value, $routeParams.query)};
                $scope.searchData.push(row);
            });
            angular.forEach(response.summoners, function(value){
                var row = {id: {type: 'summoners', id: value.id},
                           type: "Summoner",
                           name: value.name,
                           context: contextOfObject(value, $routeParams.query)};
                $scope.searchData.push(row);
            });
        });
}]);
