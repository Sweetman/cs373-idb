angular.module('hardcarryApp.search', ['ngRoute'])

.controller('searchCtrl', ["$scope", "$routeParams", "$http", "$location", function($scope, $routeParams, $http, $location){
    $scope.searchData = [];

    function getImmediateContext(string, query){
        var leftI = string.toLowerCase().indexOf(query.toLowerCase());
        var rightI = leftI;
        for(var i = 0; i < 5; i += 1){
            rightI = string.indexOf(' ', rightI + 1);
            leftI = string.lastIndexOf(' ', leftI - 1);
        }
        leftI = 0 <= leftI && leftI <= string.length ? leftI : 0;
        rightI = 0 <= rightI && rightI <= string.length ? rightI : string.length;
        console.log(string.substr(leftI, rightI));
        return string.substr(leftI, rightI-leftI);
    }

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
                    ans.push(getImmediateContext(stringRep, query));
                }
            }
        };
        contextOfObjectHelper(obj);
        if(ans.length === 0)
            return "";
        var returnString = "<ul>";
        for(var i = 0; i < ans.length; i += 1){
            if(ans[i].length === 0)
                continue;
            returnString += '<li>' + ans[i] + '</li>';
        }
        returnString += "</ul>";
        return returnString;
    }

    $http.get("/api/search/" + $routeParams.query)
        .success(function(response){
            angular.forEach(response.champions, function(value){
                var row = {id: {type: 'champions', id: value.championId},
                           type: "Champion",
                           name: value.name,
                           context: contextOfObject(value, $routeParams.query)};
                if(row.context !== '')
                    $scope.searchData.push(row);
            });
            angular.forEach(response["featured-games"], function(value){
                var row = {id: {type: 'featuredGames', id: value.id},
                           type: "Featured Game",
                           name: value.game_type,
                           context: contextOfObject(value, $routeParams.query)};
                if(row.context !== '')
                    $scope.searchData.push(row);
            });
            angular.forEach(response.summoners, function(value){
                var row = {id: {type: 'summoners', id: value.id},
                           type: "Summoner",
                           name: value.name,
                           context: contextOfObject(value, $routeParams.query)};
                if(row.context !== '')
                    $scope.searchData.push(row);
            });
        });
}]);
