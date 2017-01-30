'use strict';

angular.
  module('dstoreApp').
  config(['$locationProvider' ,'$routeProvider',
    function config($locationProvider, $routeProvider) {
      $locationProvider.hashPrefix('!');

      $routeProvider.
        when('/cars', {
          template: '<car-list></car-list>'
        }).
        when('/cars/:carId', {
          template: '<car-detail></car-detail>'
        }).
        otherwise('/cars');
    }
