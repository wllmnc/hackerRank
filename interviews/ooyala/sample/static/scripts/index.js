var getUrlParameter = function getUrlParameter(sParam) {
    var sPageURL = decodeURIComponent(window.location.search.substring(1)),
        sURLVariables = sPageURL.split('&'),
        sParameterName,
        i;

    for (i = 0; i < sURLVariables.length; i++) {
        sParameterName = sURLVariables[i].split('=');

        if (sParameterName[0] === sParam) {
            return sParameterName[1] === undefined ? true : sParameterName[1];
        }
    }
};
function init_admin(n,m){
	  ans=0
          $.ajax({
          type: 'GET',
          async: false,
          url: 'init/',
          data: { 'n' : n, 'm' : m },
          dataType: 'json',
          cache: false ,
          processData: true,
          success: function(jsonData) {
		ans=1;
          },
          error: function() {
		 alert('issues at time to create an admin' );
          }	
          });
	  return ans;

}
function ask_elevator(floor,up_down){
          $.ajax({
          type: 'GET',
          async: true,
          url: 'askelevator/',
          data: { 'floor' : floor, 'up_down' : up_down },
          dataType: 'json',
          cache: false ,
          processData: true,
          success: function(jsonData) {
            $("#f-"+jsonData.Floor+"-status"+up_down).html(jsonData.Elevator+1);
          },
          error: function() {
            alert('Error asking elevator for floor =' + floor);
          }
        });

}

function  sent_elevator_req(elevator,floor){
	  $.ajax({
          type: 'GET',
          async: true,
          url: 'setelevator/',
          data: { 'floor' : floor, 'elevator' : elevator },
          dataType: 'json',
          cache: false ,
          processData: true,
          success: function(jsonData) {
	  $("#e-"+elevator).removeClass("elevator-thinking");
          },
          error: function() {
            alert('Error asking elevator for floor =' + floor);
          }
        });

}


function  update_elevator(elevator){
	  $.ajax({
	  type: 'GET',
          async: true,
	  url: 'status/',
	  data: { 'elevator' : elevator },
	  dataType: 'json',
          cache: false ,
          processData: true,
	  success: function(jsonData) {
	    $("#e-"+jsonData.Elevator).css("bottom",(jsonData.Current_floor-1)*60);
	    if(jsonData.is_openDoors==1)		
		$("#e-"+jsonData.Elevator).addClass("open-doors");
		prefix="up";
		if (jsonData.Sense==0)prefix="down";
		if ($("#"+prefix+"-"+jsonData.Current_floor).hasClass(prefix+"-bussy"))
			$("#"+prefix+"-"+jsonData.Current_floor).removeClass(prefix+"-bussy");			
	    else 
		if ($("#e-"+jsonData.Elevator).hasClass("open-doors"))
			 $("#e-"+jsonData.Elevator).removeClass("open-doors");
	    window.setTimeout(update_elevator, 3000,elevator);//each 5 seconds
	  },
	  error: function() {
	    alert('Error loading elevator =' + elevator);
	  }
	});
}


