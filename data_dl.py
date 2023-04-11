import os
import requests
import boto3

# Test sur l'existence du fichier data_OHE.csv
if not os.path.isfile('data_OHE.csv'):
    url = "https://gist.githubusercontent.com/JQ-DataScience/6ee7f21195acceee0b70e1162a03d087/raw/bd8ad2a095021511256972df87ea1839f4ca8bc5/data_OHE.csv"
    response = requests.get(url)
    with open('data_OHE.csv', 'wb') as f:
        f.write(response.content)



# vérifier l'existence du fichier "best_model.pkl"
if not os.path.isfile("best_model.pkl"):
    # créer une session boto3 S3 et télécharger le fichier depuis le lien S3
    s3 = boto3.resource('s3')
    s3.Bucket('monlien').download_file('model.pkl', 'best_model.pkl')

