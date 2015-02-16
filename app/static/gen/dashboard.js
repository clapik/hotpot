/**
 * Created by toanngo on 2/12/15.
 */
var app = angular.module('hotpot-dashboard',
    [
        'ngRoute',
        'dashboard_controller',
        'postingsServices',
        'appointmentsServices'
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
        when('/appointments', {
            templateUrl: 'static/js/dashboard/partials/appointments.html',
            controller: 'get_appointments_controller'
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
        result.push([value.description, value.cook_username,
            "<button type=\"button\" class=\"btn btn-default\" data-toggle=\"modal\" " +
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
                console.log(data);
            });
        }
    }
]);

dashboard_controller.controller('make_appointment_controller', ['$scope', 'Appointments_Create',
    function ($scope, Appointments_Create) {
        $scope.reserve = function (posting_id) {
            var json_data = {
                id: posting_id
            };
            Appointments_Create.save(json_data, function (data) {
                console.log(data);
            });

        }
    }
]);

dashboard_controller.controller('get_appointments_controller', ['$scope', 'Appointments_Get',
    function ($scope, Appointments_Get) {
        Appointments_Get.get({}, function (data) {
            $scope.appointments = data;
            var appointments = data.result;

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

dashboard_controller.controller('delete_appointments_controller', ['$scope', 'Appointments_Delete',
    function ($scope, Appointments_Delete) {
        $scope.delete_appointment = function (appointment_id) {
            var json_data = {
                id: appointment_id
            };
            console.log(json_data)
            Appointments_Delete.save(json_data, function (data) {
                console.log(data);
                location.reload(true);
            });

        };
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
/**
 * Created by toanngo on 2/12/15.
 */
var postingsServices = angular.module('postingsServices', ['ngResource']);

postingsServices.factory('Postings', ['$resource', function ($resource) {
    return $resource("/api/posting/get_postings", {}, {
        get: {method: 'GET', cache: true},
        save: {method: 'POST', cache: true}
    });
}]);

postingsServices.factory('Postings_Edit', ['$resource', function ($resource) {
    return $resource("/api/posting/edit_posting", {}, {
        save: {method: 'POST', cache: true}
    });
}]);


var appointmentsServices = angular.module('appointmentsServices', ['ngResource']);

appointmentsServices.factory('Appointments_Get', ['$resource', function ($resource) {
    return $resource("/api/appointment/get_appointments", {}, {
        get: {method: 'GET', cache: true},
        save: {method: 'POST', cache: true}
    });
}]);

appointmentsServices.factory('Appointments_Create', ['$resource', function ($resource) {
    return $resource("/api/appointment/create", {}, {
        get: {method: 'GET', cache: true},
        save: {method: 'POST', cache: true}
    });
}]);


appointmentsServices.factory('Appointments_Delete', ['$resource', function ($resource) {
    return $resource("/api/appointment/delete", {}, {
        get: {method: 'GET', cache: true},
        save: {method: 'POST', cache: true}
    });
}]);