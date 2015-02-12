/**
 * Created by toanngo on 2/12/15.
 */
var app = angular.module('hotpot-dashboard', []);

app.config(['$interpolateProvider', function ($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
}]);

app.controller('postings-controller', function ($scope) {
    $scope.postings = {
        "result": [
            {
                "cook_id": 5,
                "cook_username": "toanngo",
                "description": "asdf",
                "id": 1
            },
            {
                "cook_id": 5,
                "cook_username": "toanngo",
                "description": "Traditional Vietnamese Dish",
                "id": 2
            },
            {
                "cook_id": 5,
                "cook_username": "toanngo",
                "description": "Traditional Vietnamese Dish 2",
                "id": 3
            },
            {
                "cook_id": 5,
                "cook_username": "toanngo",
                "description": "Traditional Vietnamese Dish 2",
                "id": 4
            },
            {
                "cook_id": 5,
                "cook_username": "toanngo",
                "description": "Traditional Vietnamese Dish 3",
                "id": 5
            }
        ]
    }
})