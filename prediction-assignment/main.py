from flask import Flask, render_template, jsonify, request
import logging
import pandas as pd
import joblib
import datetime


MODEL_NAME = 'model.joblib'

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(message)s',
                    handlers=[logging.StreamHandler()])

log = logging.getLogger(__name__)
app = Flask(__name__)


def calculate_prediction(data: dict) -> float:
    """
    :param data: data from the user
    """
    # https://datatofish.com/dictionary-to-dataframe/
    data_frame = pd.DataFrame.from_dict(data)
    model = joblib.load(MODEL_NAME)
    prediction = model.predict(data_frame)
    return prediction[:1].tolist()[0]


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


# https://stackoverflow.com/questions/13279399/how-to-obtain-values-of-request-variables-using-python-and-flask
@app.route('/api/prediction', methods=['GET'])
def get_prediction():
    data  = {
        'longitude': [float(request.args.get("longitude"))], 
        'latitude': [float(request.args.get("latitude"))], 
        'housing_median_age': [float(request.args.get("housing_median_age"))], 
        'total_rooms': [float(request.args.get("total_rooms"))], 
        'total_bedrooms': [float(request.args.get("total_bedrooms"))], 
        'population': [float(request.args.get("population"))], 
        'households': [float(request.args.get("households"))],  
        'median_income': [float(request.args.get("median_income"))], 
        'ocean_proximity_<1H OCEAN': [1 if request.args.get("ocean_proximity") == "<1H OCEAN" else 0], 
        'ocean_proximity_INLAND': [1 if request.args.get("ocean_proximity") == "INLAND" else 0], 
        'ocean_proximity_ISLAND': [1 if request.args.get("ocean_proximity") == "ISLAND" else 0], 
        'ocean_proximity_NEAR BAY': [1 if request.args.get("ocean_proximity") == "NEAR BAY" else 0], 
        'ocean_proximity_NEAR OCEAN': [1 if request.args.get("ocean_proximity") == "NEAR OCEAN" else 0]
    }

    return jsonify({'prediction': calculate_prediction(data), 'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M")})
    

 
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=80, debug=False)