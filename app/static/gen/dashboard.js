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
/**
 * Created by toanngo on 2/12/15.
 */
dashboard_controller = angular.module('dashboard_controller', [])

dashboard_controller.controller('get_postings_controller', ['$scope', 'Postings',
    function ($scope, Postings) {
        $scope.postings = Postings.get();
    }
]);

dashboard_controller.controller('get_my_postings_controller', ['$scope', 'Postings',
    function ($scope, Postings) {
        $scope.postings = Postings.save({username: window.username}, function(data){

        });
    }
]);

dashboard_controller.controller('nav-sidebar_controller', ['$scope',
    function ($scope) {
        $scope.items = [
            {name: "What's near you", url: "/"},
            {name: "Your Postings", url: "#/my_postings"},
            {name: "Your Appointments", url: "#/my_appointments"}
        ];
        $scope.selectedIndex = 0
        $scope.active_function = function ($index) {
            $scope.selectedIndex = $index
        };
    }
]);

/**
 * Created by toanngo on 2/12/15.
 */
var postingsServices = angular.module('postingsServices', ['ngResource']);

postingsServices.factory('Postings', ['$resource', function ($resource) {
    return $resource("/api/posting/get_postings");
}]);