
from flask import Flask,jsonify
import pickle
import csv
import shap
import pandas as pd
import numba
import numpy as np


df = pd.read_csv('./data_OHE.csv')

data = df.copy()


# import du model // with  as F a implémenter
model = pickle.load(open('best_model.pkl', 'rb'))


app = Flask(__name__)

@app.route('/')
def home():
    return "<p>This is a DataScience API!</p>"


# A get list of ids.
@app.route('/get_ids', methods=['GET'])
def get_ids():
    return jsonify(list(data['SK_ID_CURR']))

# Get infos according to ids
@app.route('/data/<int:id>', methods=['GET'])
def get_data(id):
    row = data.loc[data['SK_ID_CURR'] == id]
    return row.to_json(orient='records')

# Get prediction according to ids
@app.route('/predict/<int:id>', methods=['GET'])
def predict(id):
    row = data.loc[data['SK_ID_CURR'] == id]
    row = row.drop(columns=['TARGET','SK_ID_CURR'])
    prediction = model.predict(row)
    pourcentage = model.predict_proba(row)
    pred={
        "prediction":str(prediction),
        "pourcentage":str(pourcentage)
    }
    

    return jsonify(pred)

# Get shap according to ids
@app.route('/shap/<int:id>', methods=['GET'])
def shap(id):
    row = data.loc[data['SK_ID_CURR'] == id]
    row= row.drop(columns=['TARGET','SK_ID_CURR'])
    prediction= model
    # Fits the explainer
    explainer = shap.Explainer(prediction, row)
    
    # Calculates the SHAP values - It takes some time
    shap_values = explainer(row)

    """shap.plots.bar(shap_values)
    # or
    shap.summary_plot(shap_values)
    # or 
    shap.plots.beeswarm(shap_values)"""

    return str(shap_values)


if __name__ == "__main__":
    app.run()