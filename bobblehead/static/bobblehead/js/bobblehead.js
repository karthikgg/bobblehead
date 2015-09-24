(function(){
	var app = angular.module('bobblehead', []);

	app.config(['$httpProvider', function($httpProvider) {
		$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
		$httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
  }]);

  app.controller('ProjectsController', ['$http', function($http) {
		var data = this;
		$http.get('/webapp/projects_JSON/').then(function(response){
			data.data = JSON.parse(JSON.parse(response.data));
    });
  }]);

// http://www.htmlxprs.com/post/32/creating-an-angularjs-autocomplete-tag-input-widget
	app.controller('FormController', ['$scope', '$http', '$window', function($scope, $http, $window){
		// Set defaults where necessary
		this.difficulty = 'EASY';

		// Need to get this.tags from server
		this.tags = ['python', 'javascript', 'java', 'css', 'django', 'jello'];
		this.tags = this.tags.sort();

		// Tags!
		this.searchText = '';
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
				if (this.searchText.length > 0) {
					event.preventDefault();
					this.addToSelectedTags(this.selectedIndex);
					this.searchText = '';
					this.search();
				}
			}
		}

		this.addToSelectedTags = function(index) {
			if (this.suggestions.length > 0) {
				if (this.selectedTags.indexOf(this.suggestions[index]) == -1) {
					this.selectedTags.push(this.suggestions[index]);
				}
			}
			else {
				if (this.selectedTags.indexOf(this.searchText) == -1 && this.searchText !== '') {
					this.selectedTags.push(this.searchText);
				}
			}
			document.getElementById('id_tags').required = false;
		}

		this.removeTag = function(index) {
			this.selectedTags.splice(index, 1);
		}

		// Articles
		this.article = '';
		this.articles = [];
		this.maxArticlesText = '';
		this.maxArticles = 5;

		this.addArticle = function(event) {
			if (event.keyCode === 13 || event.keyCode === 9) { //Enter or Tab pressed
				// To-dp: validate for URL instead of >0
				if (this.article.length > 0 && this.articles.indexOf(this.article) == -1) {
					event.preventDefault();
					if (this.articles.length < this.maxArticles) {
						this.articles.push(this.article);
						this.article = '';
					}
					if (this.articles.length == this.maxArticles) {
						this.maxArticlesText = 'Maximum number of articles reached';
					}
				}
			}
		}

		this.removeArticle = function(index) {
			this.articles.splice(index, 1);
			this.maxArticlesText = '';
		}


		// Submit function
		this.submit = function() {
			// Define required fields
			var required = [this.title, this.difficulty, this.description, this.selectedTags];

			// Set counter to check each required field actually contains data
			var allDataPresent = '0';

			// Check that all the required fields contain data
			var checkData = function(value) {
				if (value && value.length > 0) {
					allDataPresent++;
				}
			}
			required.forEach(checkData);

			// If all required fields contain data, then submit
			if (allDataPresent == required.length) {

				// Payload for POST request
				var payload = {
					'title': this.title,
					'collaborators': 1,
					'difficulty': this.difficulty,
					'description': this.description,
					'tags_list': this.selectedTags,
					'articles': this.articles
				};

				// POST request to submit data
				$http.post('/webapp/create_project/', payload).
					then (function(response) {
						$window.location.href = '/webapp/' + response.data;
					});
			}
		}
	}]);
})();
