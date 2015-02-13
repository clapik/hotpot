/**
 * Created by toanngo on 2/12/15.
 */
dashboard_controller = angular.module('dashboard_controller', [])

dashboard_controller.controller('get_postings_controller', ['$scope', 'Postings',
    function ($scope, Postings) {
        Postings.get({}, function (data) {
            $scope.postings = data
            var postings = data.result

            var dataTable = $('#postings-table').DataTable({
                'aaData': processPostings(postings),
                'aoColumns': [

                    {'sTitle': 'Description'},
                    {'sTitle': 'Prepared by'},
                    {'sTitle': ''}
                ]
            });
        });
    }
]);

processPostings = function (postings) {
    result = []
    $.each(postings, function (index, value) {
        result.push([value.description, value.cook_username, "<button type=\"button\" class=\"btn btn-default\" data-toggle=\"modal\" " +
        "data-target=\"#myModal" + index + "\"><span class=\"glyphicon glyphicon-search\" aria-hidden=\"true\"></span></button>"])
    });
    return result;
};

dashboard_controller.controller('get_my_postings_controller', ['$scope', 'Postings',
    function ($scope, Postings) {
        Postings.save({username: window.username}, function (data) {
            $scope.postings = data
            var postings = data.result

            var dataTable = $('#postings-table').DataTable({
                'aaData': processPostings(postings),
                'aoColumns': [

                    {'sTitle': 'Description'},
                    {'sTitle': 'Prepared by'},
                    {'sTitle': ''}
                ]
            });
        });
    }
]);

dashboard_controller.controller('nav-sidebar_controller', ['$scope',
    function ($scope) {
        $scope.items = [
            {name: "What's near you", url: "#/"},
            {name: "Your Postings", url: "#/my_postings"},
            {name: "Your Appointments", url: "#/my_appointments"}
        ];
        $scope.selectedIndex = -1
        $scope.active_function = function ($index) {
            $scope.selectedIndex = $index
        };
    }
]);
