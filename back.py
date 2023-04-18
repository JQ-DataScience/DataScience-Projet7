
from flask import Flask,jsonify
import pickle
import csv
import shap
import pandas as pd
import numba
import numpy as np
import json
import os
from multiprocessing import Process

df = pd.read_csv('./data_OHE.csv')

data = df.copy()

 
# import the model // with  as F a implémenter
model = pickle.load(open('best_model.pkl', 'rb'))

# import SHAP explainer :
explainer = pickle.load(open('explainer.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return "<p>This is a DataScience API!</p>"


# A get list of ids.
@app.route('/get_ids', methods=['GET'])
def get_ids():
    return jsonify(list(data['SK_ID_CURR'])[:10]) 

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
    idx = int(data.loc[data['SK_ID_CURR'] == id].index.tolist()[0])
    row= row.drop(columns=['TARGET','SK_ID_CURR'])
    prediction= model
    # Fits the explainer
    #explainer = shap.Explainer(prediction.predict, row)
    
    # Calculates the SHAP values - It takes some time
    shap_values = explainer(row)

    #{k : round(v, 4) for v,k in zip(shap_values[3].values, shap_values[3].feature_names)}
    shap_dict = {k : round(v, 4) for v,k in zip(shap_values[idx].values, shap_values[idx].feature_names)}
    """shap.plots.bar(shap_values)
    # or
    shap.summary_plot(shap_values)
    # or 
    shap.plots.beeswarm(shap_values)"""
    return shap_dict


# Get shap according to ids

@app.route('/graph/<int:id>', methods=['GET'])
def graph(id):
    graph = data.describe()
    return graph.to_json()

# Hook for git pull

app2 = Flask(__name__)

@app2.route('/')
def trigger_deployment():
    os.system('git pull')
    return 'Git pull effectué avec succès'

# Fonction pour lancer l'application Flask 1
def run_app1():
    app.run(host='0.0.0.0', port=5000)

# Fonction pour lancer l'application Flask 2
def run_app2():
    app2.run(host='0.0.0.0', port=5001)

# Lancement des deux applications Flask
if __name__ == '__main__':
    # Création de deux processus distincts pour chaque application Flask
    p1 = Process(target=run_app1)
    p2 = Process(target=run_app2)

    # Démarrage des deux processus
    p1.start()
    p2.start()

    # Attente de la fin des deux processus
    p1.join()
    p2.join()

