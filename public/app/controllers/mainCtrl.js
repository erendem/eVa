angular.module('mainCtrl' , [])

 .controller('MainController' , function($rootScope, $location , Auth, $scope){

 	//var vm = this;

 	$scope.loggedIn = Auth.isLoggedIn();
 	$rootScope.$on('$routeChangeStart' , function(){

 		$scope.loggedIn = Auth.isLoggedIn(); 

 		Auth.getUser()
	 			.then(function(data){
	 			$scope.user = data.data;
 			});


 	});


 	$scope.doLogin = function(){
 		$scope.processing = true;
 		$scope.error = '';

 		Auth.login($scope.loginData.username, $scope.loginData.password)
 			.success(function(data){
 				$scope.processing = false;

 				Auth.getUser()
 					.then(function(data){
 					$scope.user = data.data;
 			  });
 					if(data.success){
 						$location.path('/');
 					}
 					else{
 						$scope.error = data.message
 						alert(data.message); 
			

 					}

 			});
 	}

 	$scope.doLogout = function(){
 		Auth.logout();
 		$location.path('/logout');
 	}
 });