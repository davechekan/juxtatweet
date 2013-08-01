'use strict';

var juxtatweet = angular.module('juxtatweet', ['ngResource']);

juxtatweet.config(function($routeProvider) {

  $routeProvider.
      when('/', {
        controller: 'HomeCtrl',
        templateUrl: 'views/home.html'
      }).
      when('/mix/:id', {
      	templateUrl: 'views/mix.html',
      	controller: 'MixCtrl'
      })
      ;
});
