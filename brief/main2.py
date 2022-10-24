import pandas as pd
import joblib

MODEL_NAME = 'model.joblib'

def compute_prediction(input: dict) -> int:
    data  = {
        'longitude': [-117.96], 
        'latitude': [33.89], 
        'housing_median_age': [24.0], 
        'total_rooms': [1332.0], 
        'total_bedrooms': [252.0], 
        'population': [625.0], 
        'households': [230.0], 
        'median_income': [4.4375], 
        'ocean_proximity_<1H OCEAN': [1], 
        'ocean_proximity_INLAND': [0], 
        'ocean_proximity_ISLAND': [0], 
        'ocean_proximity_NEAR BAY': [0], 
        'ocean_proximity_NEAR OCEAN': [0]
    }

    # https://datatofish.com/dictionary-to-dataframe/
    data_frame = pd.DataFrame.from_dict(data)
    model = joblib.load(MODEL_NAME)
    prediction = model.predict(data_frame)
    return prediction[:1].tolist()[0]

if __name__ == '__main__':
    print(main())