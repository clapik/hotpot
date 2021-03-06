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