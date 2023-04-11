import os
import requests

# Test sur l'existence du fichier data_OHE.csv
if not os.path.isfile('data_OHE.csv'):
    url = "https://gist.githubusercontent.com/JQ-DataScience/6ee7f21195acceee0b70e1162a03d087/raw/bd8ad2a095021511256972df87ea1839f4ca8bc5/data_OHE.csv"
    response = requests.get(url)
    with open('data_OHE.csv', 'wb') as f:
        f.write(response.content)
