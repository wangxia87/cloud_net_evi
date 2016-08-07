var directives=angular.module("forensic-sys.directives",[]);
directives.directive("holderFix",[function(){
	return {
		link:function(scope,element,attrs){
			attrs.$set("data-src",attrs.holderFix);
			Holder.run({images:element[0], nocss:true});
		}
	};
}]);
directives.directive('showTab',
    function () {
        return {
            link: function (scope, element, attrs) {
                element.on("click",function(e) {
                	//阻止a连接的跳转行为
                    e.preventDefault();
                    $(element).tab('show');
                });
            }
        };
    });
