
from server import  util
import streamlit as st
import json
global __data_columns
global __locations
global __area
global __model 
import pickle

import numpy as np

with open("./server/artifacts/banglore_home_prices_model.pickle", 'rb') as f:
      __model = pickle.load(f)


with open("./server/artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[4:245]
        __area = __data_columns[245:]

st.title("Real Estate bangalore prediction")

sqft =st.number_input("Area(squre foot)")
location = st.selectbox(
    "Select Location",
   __locations,
)

area = st.selectbox(
    "Select area",
   __area,
)

size = st.number_input(
    "Number of Bedrooms",
    min_value=1,
    max_value=16,
    step=1
)

bath = st.number_input(
    "Number of Bathrooms",
    min_value=1,
    max_value=16,
    step=1
)

balcony = st.number_input(
    "Number of Balconies",
    min_value=1,
    max_value=5,
    step=1
)


def predict_home_price():

	response=jsonify({
		'estimated_price':util.get_estimated_price(location, size, sqft, bath, balcony, area)
	})
	print( response)

def get_estimated_price(location, size, sqft, bath, balcony, area):
    
    try:
        loc_index = __data_columns.index(location.lower())
        area_index = __data_columns.index(area.lower())
    except:
        loc_index = -1
        area_index = -1
    x = np.zeros(len(__data_columns))
    x[0] = size
    x[1] = sqft
    x[2] = bath
    x[3] = balcony
    if loc_index >= 0:
        x[loc_index] = 1
    if area_index >= 0:
        x[area_index] = 1
    return round(__model.predict([x])[0], 2)


b=st.button("Get Price")
st.subheader("Estimated Price")
if b:
      st.write(get_estimated_price(location, size, sqft, bath, balcony, area))

if __name__=="__main__":
	print("Starting python flask server for Home prediction..")
	print(get_estimated_price('Electronic City Phase II', 2, 1056, 2, 1, 'Super built-up  Area'))
	print(get_estimated_price('Indira Nagar',2,1056,2,1,'Super built-up  Area'))  # other areaprint
	print(get_estimated_price('Indira Nagar',2,1056,2,1,'carpet  Area'))  # other location
	print(get_estimated_price('Ejipura', 3, 1056, 3, 1, 'Super built-up  Area'))  # other location

# to view http call postman