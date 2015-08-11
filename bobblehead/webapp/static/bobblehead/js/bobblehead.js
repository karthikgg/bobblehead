(function(){
	var app = angular.module('bobblehead', []);

  app.controller('ProjectsController', ['$http', function($http) {
		var data = this;
		this.data = [];
		$http.get('/webapp/projects_JSON/').then(function(response){
			this.data = JSON.parse(response.data);
			console.log(this.data);

    });

  }]);

})();
