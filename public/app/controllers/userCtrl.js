angular.module('userCtrl' , [])

	.controller('UserController' , function(User , $scope) {

		//var vm = this;
		User.all()
			.success(function(data){
				$scope.users = data;
			})
	})


	.controller('UserCreateController' , function(User, $location, $window ,$scope){
		//var vm = this;

		$scope.signupUser = function(){
			$scope.message = '';

			User.create($scope.userData)
				.then(function(response){ 
					$scope.userData = {};
					$scope.message = response.data.message;

					$window.localStorage.setItem('token' , response.data.token);
					$location.path('/');
				})
		}
	})

	