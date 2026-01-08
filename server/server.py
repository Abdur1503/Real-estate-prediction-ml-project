from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_location_names')
def get_location_names():
	response = jsonify({
		'locations': util.get_location_names()
	})
	response.headers.add('Access-Control-Allow-Origin', '*')
	return response

@app.route('/get_area_names')
def get_area_names():
	response=jsonify({
		'area type':util.get_area_names()
	})
	response.headers.add('Access-Control-Allow-Origin', '*')
	return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
	location = str(request.form['location'])
	size = int(request.form['size'])
	sqft = float(request.form['sqft'])
	bath = int(request.form['bath'])
	balcony = int(request.form['balcony'])
	area = str(request.form['area'])

	response=jsonify({
		'estimated_price':util.get_estimated_price(location, size, sqft, bath, balcony, area)
	})

	response.headers.add('Access-Control-Allow-Origin', '*')
	return response

if __name__=="__main__":
	print("Starting python flask server for Home prediction..")
	app.run()

# to view http call postman