var piedata = [
    {
        value: 473,
        color:"#F7464A",
        highlight: "#FF5A5E",
        label: "IPv4 Only Sites"
    },
    {
        value: 27,
        color: "#46BFBD",
        highlight: "#5AD3D1",
        label: "IPv6 Enabled Sites"
    }
]

var alexaipv6 = [
	'Att.com',
	'Blogger.com',
	'Blogspot.com',
	'Cisco.com',
	'Conservativetribune.com',
	'Drugs.com',
	'Ed.gov',
	'Facebook.com',
	'Fbcdn.net',
	'Gfycat.com',
	'Google.com',
	'Healthcare.gov',
	'Jet.com',
	'Mit.edu',
	'Nametests.com',
	'Noaa.gov',
	'Office.com',
	'Speedtest.net',
	'Ssa.gov',
	'Stanford.edu',
	'State.gov',
	'Timeanddate.com',
	'Wikimedia.org',
	'Wikipedia.org',
	'Xhamster.com',
	'Yahoo.com',
	'Youtube.com'
]

$(document).ready(function () {
	var pieexists = false;
	var generate = false;
	var ctx = $("#myChart").get(0).getContext("2d");
	
	$('#dns').fadeOut(500, function(){
		$('#dns').html('www.google.com');
		$('#dns').fadeIn(500, function(){
			$('#ipv4').fadeOut(500, function(){
				$('#ipv4').html('195.13.231.168');
				$('#ipv4').fadeIn(500, function(){
					$('#ipv6').fadeOut(500, function(){
						$('#ipv6').html('2a00:1450:4009:811::200e');
						$('#ipv6').fadeIn(500, function(){
						});
					});
				});
			});
		});
	});

	$('#dns').hover(
		function(){
			$('#dns').fadeOut(500, function(){
				$('#dns').html('DNS');
				$('#dns').fadeIn(500)
			});
		},
		function(){
			$('#dns').fadeOut(500, function(){
				$('#dns').html('www.google.com');
				$('#dns').fadeIn(500)
			});
	});

	$('#ipv4').hover(
		function(){
			$('#ipv4').fadeOut(500, function(){
				$('#ipv4').html('IPv4');
				$('#ipv4').fadeIn(500)
			});
		},
		function(){
			$('#ipv4').fadeOut(500, function(){
				$('#ipv4').html('195.13.231.168');
				$('#ipv4').fadeIn(500)
			});
	});

	$('#ipv6').hover(
		function(){
			$('#ipv6').fadeOut(500, function(){
				$('#ipv6').html('IPv6');
				$('#ipv6').fadeIn(500)
			});
		},
		function(){
			$('#ipv6').fadeOut(500, function(){
				$('#ipv6').html('2a00:1450:4009:811::200e');
				$('#ipv6').fadeIn(500)
			});
	});

	$(window).scroll( function(){
    	if(!generate){
    		/* Check the location of each desired element */
	        $('.hidden').each( function(i){
	            
	            var bottom_of_object = $(this).offset().top + $(this).outerHeight();
	            var bottom_of_window = $(window).scrollTop() + $(window).height();
	            
	            /* If the object is completely visible in the window, fade it in */
	            if( bottom_of_window > bottom_of_object ){
	                
	                $(this).animate({'opacity':'1'},1000);
	                if(!pieexists){
	                	var myPieChart = new Chart(ctx).Pie(piedata);
	                	pieexists = true;
	                }
	            }

	        }); 
    	}
    });

	$('#ipv6sites').append('<ul></ul>')
    for(site of alexaipv6){
    	$('#ipv6sites > ul').append('<li>' + site + '</li>');
    }
});

