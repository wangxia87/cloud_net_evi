var app=angular.module("forensic-sys",["forensic-sys.directives","forensic-sys.services","ngRoute"]);
app.controller("MainController",function($scope,$route,$routeParams,$location){
	$scope.$route=$route;
	$scope.$location=$location;
	$route.$routeParams=$routeParams;
});
app.controller("ForensicListCtrl",function($scope,$routeParams){
	$scope.name="ForensicListCtrl";
	$scope.params=$routeParams;

});
app.controller("ReportListCtrl",function($scope,$routeParams){
	$scope.name="ReportListCtrl";
	$scope.params=$routeParams;
});
app.controller("routeCtrl",function($scope,$routeParams){
	$scope.name="routeCtrl";
	$scope.params=$routeParams;
});
app.config(["$routeProvider","$locationProvider",function($routeProvider,$locationProvider){
	$routeProvider.when("/forensic-list",{
		templateUrl:"forensic_list.html",
		controller:"ForensicListCtrl"
	}).when("/report-list",{
		templateUrl:"report_list.html",
		controller:"ReportListCtrl"
	}).when("/forensic-detail/:forensic_id",{
		templateUrl:"/views/forensic_detail.html",
		controller:"ForensicDetailCtrl"		
	}).when("/report-detail/:report_id",{
		templateUrl:"/views/report_detail.html",		
		controller:"ReportDetailCtrl"
	}).when("/forensic-request",{
		templateUrl:"/views/requestForm.html",		
		controller:"ForensicReuqestCtrl",
	}).when("/test-route",{
		templateUrl:"/forensic/forensic/static/views/test_route.html",
		controller:"routeCtrl"
	}).otherwise({redirectTo:"/"});

}]);