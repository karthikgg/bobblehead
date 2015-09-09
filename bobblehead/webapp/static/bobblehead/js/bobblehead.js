(function(){
	var app = angular.module('bobblehead', []);

	app.config(['$httpProvider', function($httpProvider) {
		$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
		$httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
  }]);

  app.controller('ProjectsController', ['$http', function($http) {
		var data = this;
		data.data = [];
		$http.get('/webapp/projects_JSON/').then(function(response){
			data.data = JSON.parse(JSON.parse(response.data));
    });
  }]);

// http://www.htmlxprs.com/post/32/creating-an-angularjs-autocomplete-tag-input-widget
	app.controller('FormController', ['$http', function($http){
		// Need to get this.tages from server
		this.tags = ['python', 'javascript', 'java', 'css', 'django', 'j', 'jello'];
		this.tags = this.tags.sort();
		this.searchText = ''
		this.suggestions = [];
		this.selectedTags = [];
		this.selectedIndex = 0;

		this.search = function() {
			searchText = this.searchText;
			suggestions = this.suggestions;
			suggestions.length = 0;
			var suggest = function(value) {
				if (value.indexOf(this.searchText) === 0 && this.searchText.length > 0 && this.suggestions.indexOf(value) === -1) {
					this.suggestions.push(value);
				}
			}
			this.tags.forEach(suggest);
			this.selectedIndex = 0;
		}

		this.checkKeyDown = function(event) {
			if (event.keyCode === 40) { //down key, increment selectedIndex
				event.preventDefault();
				if (this.selectedIndex+1 !== this.suggestions.length) {
					this.selectedIndex++;
				}
			}
			else if (event.keyCode === 38) { //up key, decrement selectedIndex
				event.preventDefault();
				if (this.selectedIndex-1 !== -1) {
					this.selectedIndex--;
				}
			}
			else if (event.keyCode === 13 || event.keyCode === 9) { //enter pressed
				event.preventDefault();
				this.addToSelectedTags(this.selectedIndex);
				this.searchText = '';
				this.search();
			}
		}

		this.addToSelectedTags = function(index) {
			if (this.selectedTags.indexOf(this.suggestions[index]) == -1 && this.searchText !== '') {
				this.selectedTags.push(this.suggestions[index]);
			}
			console.log(this.selectedTags);
		}

		this.removeTag = function(index) {
			this.selectedTags.splice(index, 1);
			console.log(this.selectedTags);
		}

		this.submit = function() {
			var payload = {
				'title': this.title,
				'collaborators': 1,
				'difficulty': this.difficulty,
				'description': this.description,
				'tags_list': this.selectedTags,

			};
			console.log(payload);
			$http.post('/webapp/create_project/', payload);
		}

	}]);
})();
