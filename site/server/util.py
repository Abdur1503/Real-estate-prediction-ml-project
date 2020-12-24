import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None
__area = None


def get_estimated_price(location, size, sqft, bath, balcony, area):
    load_saved_artifacts()
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


def get_location_names():
    load_saved_artifacts()
    return __locations


def get_area_names():
    load_saved_artifacts()
    return __area


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations
    global __area

    with open("./artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[4:245]
        __area = __data_columns[245:]

    global __model
    with open("./artifacts/banglore_home_prices_model.pickle", 'rb') as f:
        __model = pickle.load(f)
    print('loading the artifacts done')


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_area_names())
    print(get_estimated_price('Electronic City Phase II', 2, 1056, 2, 1, 'Super built-up  Area'))
    print(get_estimated_price('Indira Nagar',2,1056,2,1,'Super built-up  Area'))  # other area
    print(get_estimated_price('Indira Nagar',2,1056,2,1,'carpet  Area'))  # other location
    print(get_estimated_price('Ejipura', 3, 1056, 3, 1, 'Super built-up  Area'))  # other location
