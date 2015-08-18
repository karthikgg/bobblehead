(function(){
	var app = angular.module('bobblehead', []);

  app.controller('ProjectsController', ['$http', function($http) {
		var data = this;
		data.data = [];
		$http.get('/webapp/projects_JSON/').then(function(response){
			data.data = JSON.parse(JSON.parse(response.data));
    });
  }]);
})();
