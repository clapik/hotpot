/**
 * Created by toanngo on 2/12/15.
 */
var app = angular.module('hotpot-dashboard', []);

app.config(['$interpolateProvider', function ($interpolateProvider) {
    $interpolateProvider.startSymbol('{[');
    $interpolateProvider.endSymbol(']}');
}]);