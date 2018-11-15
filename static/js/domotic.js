function send_request(url, value, id, reqTp, callback) {
	$.ajax({
		url: url,
		data: {'value': value, 'reqType': reqTp},
		type: 'POST',
		async:false,
		success: function(response) {
			console.log(response);
			callback(id, response)
		},
		error: function(error){
			alert(error);
		}
	});
}

function setStatus(id, status) {
	$(id).bootstrapToggle(status)
}

$(document).ready(function()
{
	var reqType = 'socket'
	var old_air = 'off'
	var old_light = 'off'
	var old_tv = 'off'
	var old_audio = 'off'

	$("#air-status:checkbox").change(function() {
		value = $(this).val()
		if (old_air != value) {
			old_air = value
			send_request('/changeAir', value, '#air-status', reqType, setStatus)	
		}
	});
	
	$("#light-status:checkbox").change(function() {
		value = $(this).val()
		if (old_light != value) {
			old_light = value
			send_request('/changeLight', value, '#light-status', reqType, setStatus)
		}
	});
	
	$("#tv-status:checkbox").change(function() {
		value = $(this).val()
		if (old_tv != value) {
			old_tv = value
			send_request('/changeTV', value, '#tv-status', reqType, setStatus)
		}
	});
	 
	 $("#audio-status:checkbox").change(function() {
		value = $(this).val()
		if (old_audio != value) {
			old_audio = value
			send_request('/changeAudio', value, '#audio-status', reqType, setStatus)
		}
	 });

	 $("#radio-socket").prop( "checked", true );
	 
	 $("#radio-socket").click(function() {
		 reqType = 'socket'
		$("#radio-socket").prop("checked", true);
		$("#radio-mqtt").prop("checked", false);
	 });

	 $("#radio-mqtt").click(function() {
		reqType = 'mqtt'
		$("#radio-mqtt").prop("checked", true);
		$("#radio-socket").prop("checked", false);
	 });
});