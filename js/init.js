// alert("test");

var windowHeight = $( window ).height();

$("#banner").css("min-height", windowHeight + "px" );
$(".intro-lead-in").css("height", windowHeight/2 + "px");
$("#skills").css("min-height", windowHeight + "px" );
$("#portfolio").css("min-height", windowHeight + "px" );
$("#contact").css("min-height", windowHeight + "px" );


// initilize the typed.js stuff in header

$(function(){

    $("#typedBanner").typed({
        strings: ["<span class = 'blue'>function</span> <span class = 'green'>initilize_portfolio</span> ( ) { </br>" + 
        	"<span class = 'blue'>var</span> skills <span class = 'red'>=</span> { </br><span class = 'yellow tab'>     &apos;JavaScript&apos;</span>, </br><span class = 'yellow tab'>     &apos;HTML&apos;</span>, </br><span class = 'yellow tab'>     &apos;CSS&apos;</span>, </br><span class = 'yellow tab'>     &apos;PHP&apos;</span>, </br>};"
        ],
        typeSpeed: 10,
        backDelay: 500,
        loop: false,
        contentType: 'html', // or text
        // defaults to false for infinite loop
        loopCount: false,
        callback: function(){ },
        resetCallback: function() { newTyped(); }
    });
});


// function initilize_portfolio () {
// 	var skills = {
// 	     'JavaScript',
// 	     'HTML',
// 	     'CSS',
// 	     'PHP',
// 	     'SQL'
// 	};
// 	var projects = {
// 		'nanokeys.com',
// 		'greenarrowloans.com',
// 		'clearlineloans.com',
// 		'geology.morganporritt.com'
// 	};
// 	var contact = {
// 		'email' = 'me@morganporritt.com'
// 	};
// 	$('#portfolio').add(skills, projects, contact);
// }
