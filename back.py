
from flask import Flask,jsonify
import pickle
import csv
import pandas as pd


df = pd.read_csv('./data.csv')
data = df.copy()



app = Flask(__name__)

app.route('/')
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
    row= row.drop(columns=['TARGET','SK_ID_CURR'])
    model = pickle.load(open('best_model.pkl', 'rb'))
    prediction= model.predict(row)
    return prediction


if __name__ == "__main__":
    app.run()