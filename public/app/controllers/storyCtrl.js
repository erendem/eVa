angular.module('storyCtrl' , ['storyService'])

	.controller('StoryController' , function(Story,$scope , socketio){



		Story.allStory()
			.success(function(data){
				$scope.stories = data;
			});

		$scope.createStory = function(){

			$scope.message = '';

				Story.createStorye($scope.storyData)
					.success(function(data){
						
						$scope.storyData = '';

						$scope.message = data.message;

							
					});
				
			};

			socketio.on('story' , function(data){
				$scope.stories.push(data);
			})


	})

 .controller('AllStoriesController' , function(stories , socketio , $scope){
 		

		
		$scope.stories = stories.data;

		socketio.on('story' , function(data){
				$scope.stories.push(data);
			});


		

		

	});