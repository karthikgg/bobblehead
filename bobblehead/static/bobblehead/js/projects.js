(function(){
	var app = angular.module('projectData', []);

  app.controller('ProjectsController', ['$scope', '$http', function($scope, $http) {
    var data = this;
		$http.get('/webapp/projects_JSON/').then(function(response){
			data.data = JSON.parse(JSON.parse(response.data));
			sessionStorage.setItem('projects', JSON.stringify(data.data));
      // console.log(JSON.stringify(data.data, null, 2));
    });

		// Persist difficulty filter
		if (sessionStorage.getItem('difficulty')) {
			$scope.difficulty = sessionStorage.getItem('difficulty');
		} else {
			$scope.difficulty = '';
		}
		this.changeDifficulty = function() {
			sessionStorage.setItem('difficulty', $scope.difficulty);
		}

		$scope.tags = []
    var projectData = JSON.parse(sessionStorage.getItem('projects'));
    projectData.forEach(getData);
    function getData(allData) {
      allData.fields.tags.forEach(getTags);
      function getTags(tag) {
        if ($scope.tags.indexOf(tag) == -1) {
          $scope.tags.push(tag);
        }
      }
    }

    $scope.searchText = '';
    $scope.suggestions = [];
		$scope.selectedTags = [];
		$scope.selectedIndex = 0;

    $scope.search = function() {
			if ($scope.searchText) {
				searchText = $scope.searchText.toLowerCase();
			} else {
				searchText = $scope.searchText;
			}

      $scope.suggestions.length = 0;
			$scope.tags.forEach(suggest);
			function suggest(value) {
				var value = value.toLowerCase();
				if (value.indexOf($scope.searchText) === 0 && $scope.searchText.length > 0 && $scope.suggestions.indexOf(value) === -1) {
					$scope.suggestions.push(value);
				}
			}
			$scope.selectedIndex = 0;
		}

    $scope.checkKeyDown = function(event) {
			if (event.keyCode === 40) { //down key, increment selectedIndex
				event.preventDefault();
				if ($scope.selectedIndex+1 !== $scope.suggestions.length) {
					$scope.selectedIndex++;
				}
			}
			else if (event.keyCode === 38) { //up key, decrement selectedIndex
				event.preventDefault();
				if ($scope.selectedIndex-1 !== -1) {
					$scope.selectedIndex--;
				}
			}
			else if (event.keyCode === 13 || event.keyCode === 9) { //enter pressed
				if ($scope.searchText.length > 0) {
					event.preventDefault();
					$scope.addToSelectedTags($scope.selectedIndex);
					$scope.searchText = '';
					$scope.search();
				}
			}
		}

    $scope.addToSelectedTags = function(index) {
			if ($scope.suggestions.length > 0) {
				if ($scope.selectedTags.indexOf($scope.suggestions[index]) == -1) {
					$scope.selectedTags.push($scope.suggestions[index]);
				}
			}
			else {
				if ($scope.selectedTags.indexOf($scope.searchText) == -1 && $scope.searchText !== '') {
					$scope.selectedTags.push($scope.searchText);
				}
			}
		}

    $scope.removeTag = function(index) {
			$scope.selectedTags.splice(index, 1);
		}
  }]);

	app.filter('projectFilter', function() {
		return function (items, scope) {
			var filtered = [];
			var checksum = [];
			angular.forEach(items, function(item) {

				itemTags = [];
				item.fields.tags.forEach(lowerCase);
				function lowerCase(value) {
					if (typeof(value) == 'string') {
						itemTags.push(value.toLowerCase());
					} else {
						itemTags.push(value);
					}
				}

				if (scope.selectedTags.length == 0) {
					filtered.push(item);
				} else {
					scope.selectedTags.forEach(checkTags);
					function checkTags(value) {
						if (itemTags.indexOf(value) == -1) {
							checksum.push(0);
						} else {
							checksum.push(1);
						}
					}
					if (checksum.indexOf(0) == -1) {
						filtered.push(item);
					}
				}
				checksum = [];
			});
			return filtered;
		}
	});

})();
