
$(document).ready( function () {
	
	//logout();
	adjustBanner();
	
	$(window).on("resize", adjustBanner);
});

function adjustBanner () {
	var headerHeight = $("header").height();
	$(".content").css("top", headerHeight+2);
};
