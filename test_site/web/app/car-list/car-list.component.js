'use strict';

// Register `carList` component, along with it's associated controller and template
angular.
  module('carList').
  component('carList', {
    templateUrl: 'car-list/car-list.template.html',
    controller: ['Car',
      function CarListController(Car) {
        this.cars = Car.query();
      }
    ]
  });