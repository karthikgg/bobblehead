(function(){
	var app = angular.module('projectData', []);

  app.controller('ProjectsController', ['$http', function($http) {
    var data = this;
		$http.get('/webapp/projects_JSON/').then(function(response){
			data.data = JSON.parse(JSON.parse(response.data));
			sessionStorage.setItem('projects', JSON.stringify(data.data));
      console.log(JSON.stringify(data.data, null, 2));
    });
  }]);
})();
