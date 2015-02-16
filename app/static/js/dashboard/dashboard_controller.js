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
    var result = []
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
        });
    }
]);

dashboard_controller.controller('nav-sidebar_controller', ['$scope',
    function ($scope) {
        $scope.items = [
            {name: "What's near you", url: "#/"},
            {name: "Your Postings", url: "#/my_postings"},
            {name: "Your Appointments", url: "#/appointments"}
        ];
        $scope.selectedIndex = -1
        $scope.active_function = function ($index) {
            $scope.selectedIndex = $index
        };
    }
]);


dashboard_controller.controller('edit_posting_controller', ['$scope', 'Postings_Edit',
    function ($scope, Postings_Edit) {
        $scope.edit = function (index, posting_id) {
            console.log(index)
            var json_data = {
                id: posting_id,
                description: $('#inputDescription' + index).val(),
                price: parseFloat($('#inputPrice' + index).val()),
                date: $('#inputDate' + index).val()
            };
            Postings_Edit.save(json_data, function (data) {
                console.log(data)
            })
        }
    }
]);

dashboard_controller.controller('get_appointments_controller', ['$scope', 'Appointments',
    function ($scope, Appointments) {
        Appointments.get({}, function (data) {
            $scope.appointments = data
            var appointments = data.result

            var dataTable = $('#appointments-table').DataTable({
                'aaData': processAppointments(appointments),
                'aoColumns': [
                    {'sTitle': 'Appointment ID'},
                    {'sTitle': 'Posting ID'},
                    {'sTitle': 'Description'},
                    {'sTitle': 'Price'},
                    {'sTitle': 'Date'},
                    {'sTitle': 'Prepared By'},
                    {'sTitle': 'Customer'},
                    {'sTitle': ''}
                ]
            });
        });
    }
]);

processAppointments = function (appointments) {
    var result = [];
    $.each(appointments, function (index, value) {
        result.push([value.appointment_id, value.posting_id, value.description, value.price, value.date, value.cook_username, value.customer_username,
            "<button type=\"button\" class=\"btn btn-default\" data-toggle=\"modal\" " +
            "data-target=\"#myModal" + index + "\"><span class=\"glyphicon glyphicon-search\" aria-hidden=\"true\"></span></button>"])
    });
    return result;
};