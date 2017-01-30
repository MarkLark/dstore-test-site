'use strict';

angular.
  module('core.car').
    factory('Car', ['$resource',
      function($resource) {
        return $resource('/api/cars/make/:carId', {}, {});
      }
    ]);
