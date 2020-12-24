function getBathValue(){
	var uiBath=document.getElementsByName("uiBathrooms");
	for(var i in uiBath){
		if(uiBath[i].checked){
			return parseInt(i)+1;
		}
	}
	return-1;//invalid value
}
function getBHKValue(){
	var uiBHK=document.getElementsByName("uiBHK");
	for(var i in uiBHK){
		if(uiBHK[i].checked){
			return parseInt(i)+1;
		}
	}
	return-1;//invalid value
}
function getBalconyValue(){
	var uiBalcony=document.getElementsByName("uiBalcony");
	for(var i in uiBalcony){
		if(uiBalcony[i].checked){
			return parseInt(i)+1;
		}
	}
	return-1;//invalid value
}
function onClickedEstimatedPrice()
{
	console.log("Estmated button clicked");
	var sqft=document.getElementById("uiSqft");
	var size=getBHKValue();
	var bath=getBathValue();
	var balcony=getBalconyValue();
	var location=document.getElementById("uiLocation");
	var area=document.getElementById("uiArea");
	var estPrice=document.getElementById("uiEstimatedPrice");

	var url="http://127.0.0.1:5000/predict_home_price";

	$.post(url,{
		location: location.value,
		size: size,
		sqft: parseFloat(sqft.value),
		bath: bath,
		balcony: balcony,
		area: area.value
	    },function(data,status){
	    	console.log(data.estimated_price);
	    	estPrice.innerHTML="<h2>"+data.estimated_price.toString()+" Lakh<h2>";
	    	console.log(status);	
	    });

}

function onPageLoad()
{
	console.log("document loaded");
	var url="http://127.0.0.1:5000/get_location_names";
	$.get(url,function(data,status){
		console.log("got response for get_location_names request");
		if(data){
			var locations=data.locations;
			var uiLocation=document.getElementById("uiLocation");
			$('#uiLocation').empty();
			for(var i in locations){
				var opt=new Option(locations[i]);
				$("#uiLocation").append(opt);
			}
		}
	});
}
window.onload=onPageLoad;