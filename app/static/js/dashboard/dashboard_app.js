/**
 * Created by toanngo on 2/12/15.
 */
var app = angular.module('hotpot-dashboard',
    [
        'ngRoute',
        'dashboard_controller',
        'postingsServices'
    ]);

app.config(['$interpolateProvider', function ($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
}]);

app.config(['$routeProvider', function ($routeProvider) {
    $routeProvider.
        when('/', {
            templateUrl: 'static/js/dashboard/partials/postings.html',
            controller: 'get_postings_controller'
        }).
        when('/my_postings', {
            templateUrl: 'static/js/dashboard/partials/my_postings.html',
            controller: 'get_my_postings_controller'
        }).
        otherwise({
            redirectTo: '/'
        })
}])