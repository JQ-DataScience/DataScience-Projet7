import boto3
import os
import requests

# Création de la connexion S3
session = boto3.Session(
    aws_access_key_id='AKIAUVMIDAYPVH33FRGQ',
    aws_secret_access_key='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'
)
s3 = session.resource('s3')

bucket_name= 'p7-bucket-mlflow'

# Téléchargement du fichier data_OHE.csv depuis S3
if not os.path.isfile('data_OHE.csv'):
    bucket = s3.Bucket(bucket_name)
    obj = bucket.Object('data_OHE.csv')
    obj.download_file('data_OHE.csv')

# Téléchargement du fichier best_model.pkl depuis S3
if not os.path.isfile('best_model.pkl'):
    bucket = s3.Bucket(bucket_name)
    obj = bucket.Object('best_model.pkl')
    obj.download_file('best_model.pkl')

# Téléchargement du fichier explainer.pkl depuis S3
if not os.path.isfile('explainer.pkl'):
    bucket = s3.Bucket(bucket_name)
    obj = bucket.Object('explainer.pkl')
    obj.download_file('explainer.pkl')