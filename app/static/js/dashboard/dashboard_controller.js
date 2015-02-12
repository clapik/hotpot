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
