import pytest
import os
import back
from flask import json


# Test sur l'existence du fichier data_OHE.csv
if not os.path.isfile('data_OHE.csv'):
    url = "https://gist.githubusercontent.com/JQ-DataScience/6ee7f21195acceee0b70e1162a03d087/raw/bd8ad2a095021511256972df87ea1839f4ca8bc5/data_OHE.csv"
    response = requests.get(url)
    with open('data_OHE.csv', 'wb') as f:
        f.write(response.content)
    assert os.path.isfile('data_OHE.csv')


# Test sur l'existance et l'extension du fichier back.py
def test_back_file_extension():
    assert os.path.isfile('back.py')
    assert os.path.splitext('back.py')[1] == '.py'

# test sur l'existence des fonctions principales et leur utilisation
def test_get_ids_function_exists():
    assert hasattr(back, 'get_ids')
    assert callable(getattr(back, 'get_ids'))
    
# fonctionnalité de fixation (fixture) de pytest pour lancer l'application Flask en mode test.
@pytest.fixture
def client():
    app = back.app
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Test GET sur l'endpoint "/get_ids" //  code HTTP 200 // liste entiers
def test_get_ids_returns_list_of_integers(client):
    response = client.get('/get_ids')
    assert response.status_code == 200
    data = json.loads(response.get_data())
    assert isinstance(data, list)
    assert all(isinstance(i, int) for i in data)        

# Test et Récupération du 1er ID
def test_get_data_returns_json(client):
    response_ids = client.get('/get_ids')
    assert response_ids.status_code == 200
    data_ids = json.loads(response_ids.get_data())
    assert isinstance(data_ids, list)
    assert len(data_ids) > 0
    id_to_test = data_ids[0]

# Test format JSON pour getdata(id)
    response_data = client.get(f'/data/{id_to_test}')
    assert response_data.status_code == 200
    data = json.loads(response_data.get_data())
    assert isinstance(data, list)
    assert len(data) == 1


#Test format JSON pour predict(id)
def test_predict_returns_json(client):
    response_ids = client.get('/get_ids')
    assert response_ids.status_code == 200
    data_ids = json.loads(response_ids.get_data())
    assert isinstance(data_ids, list)
    assert len(data_ids) > 0
    id_to_test = data_ids[0]

    response_predict = client.get(f'/predict/{id_to_test}')
    assert response_predict.status_code == 200
    data = json.loads(response_predict.get_data())
    assert isinstance(data, dict)
    assert "prediction" in data

#Test format JSON pour shap(id)
def test_shap_returns_json(client):
    response_ids = client.get('/get_ids')
    assert response_ids.status_code == 200
    data_ids = json.loads(response_ids.get_data())
    assert isinstance(data_ids, list)
    assert len(data_ids) > 0
    id_to_test = data_ids[0]

    response_shap = client.get(f'/shap/{id_to_test}')
    assert response_shap.status_code == 200
    data = json.loads(response_shap.get_data())
    assert isinstance(data, dict)
    

#Test format JSON pour graph(id)
def test_graph_returns_json(client):
    response_ids = client.get('/get_ids')
    assert response_ids.status_code == 200
    data_ids = json.loads(response_ids.get_data())
    assert isinstance(data_ids, list)
    assert len(data_ids) > 0
    id_to_test = data_ids[0]

    response_graph = client.get(f'/graph/{id_to_test}')
    assert response_graph.status_code == 200
    data = json.loads(response_graph.get_data())
    assert isinstance(data, dict)


