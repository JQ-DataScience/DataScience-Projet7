import os
import requests


# Test sur l'existence du fichier data_OHE.csv
if not os.path.isfile('data_OHE.csv'):
    url = "https://p7-bucket-mlflow.s3.eu-west-3.amazonaws.com/data_OHE.csv?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaDGV1LWNlbnRyYWwtMSJHMEUCIQDCpU1%2BOtb6bViemBRoDC1jQnACXPhz5UVnv5%2FrOUxMAQIgXNGuDx7iOZStmn29iolGA9b8Gd%2Bxa5oDOcWQMfoxOL0q7QII1f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgwzMjA3OTczNDUzMTEiDESy1mOgTN%2FUsA6%2FaCrBAj4d34fz7RNN1iFQodPnV9ggAACjFgQ7Vo94%2FBrdhbhDEelX98%2BP08UCjuxG01zY8vQYtcAFoxLkEbmr95KKxUpTyc9v7MTpbKltFrCuYW%2BpWYNsDp9x3by0CqsytfajJdlZAUoPEOWevuRq3DAZSMvQVIP4VIj%2B%2FSt%2BqDUI2xJ5x8KcCYQFEabSKUEiGXR6vHkHyXrI6JF6dX2KBTHR23HiQD1AtapEkngTaxI7mNNlu9Szuzrq8h8yG9ZBCf4Nen%2BzSYqgnibUHKeX7b9yWxqBCuYWqB0D3lefDsMr1Bdi6jj8HkrCMqPo5TQfoSbd3LtojrQxOpnCNUQ3y3n6hjYxDRrztsdQvfjL6HWaiwLHt0VL37lTI6ADv3fAhpDton%2BvF4VFQ9SkeqcD9TzWVqvUvC1Lnb5MOesXJKxF6tpt7DDx4t%2BhBjqzAutpkWhOur1dnT2aXqNSZKHuaBWXW1Hf7nWB1MOZHF7u2M8o8ZZuyq6ECHBH%2BAu06SMKrWYuBXlya3fZf%2BfILoQ742TwftTxW7In%2FQyqppBiVRiy%2B70i3qPok47Fc03Mb46KlGv58rIOsahyxqaCuAvmVYTw3gHG6mdHPg1793tDXQSWBIpUKsrU%2B73xAypC2QFG%2BHKFV44OMlUktZw0BWgCYVhFf6qmJqbjWJ1uJkHMsNSHtQNaRjKZErJDK%2Fyki3Hg6oIAOqyvVqlsgwwAMXPqhxo8Yb6lb%2FcIgTKamujKrY1k3ynD08WXPiPDRlYM3GpjKxFUB3EqoDRWy7tpFiSl6wYiemgEVH6q0xfrPBsVz5bLYYPkHLMiPYrCkbuZSMfYNCqd7eQS2L9kqOh3W%2BcWhHs%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20230413T125538Z&X-Amz-SignedHeaders=host&X-Amz-Expires=7200&X-Amz-Credential=ASIAUVMIDAYP2OZJPL6K%2F20230413%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Signature=d464c0f0e11843ed2e6ce5126b044d631323b571e09166bc3e115ed1f759549c"
    response = requests.get(url)
    with open('data_OHE.csv', 'wb') as f:
        f.write(response.content)


# Test sur l'existence du fichier best_model.pkl
model_link = 'https://p7-bucket-mlflow.s3.eu-west-3.amazonaws.com/best_model.pkl?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaDGV1LWNlbnRyYWwtMSJHMEUCIQDCpU1%2BOtb6bViemBRoDC1jQnACXPhz5UVnv5%2FrOUxMAQIgXNGuDx7iOZStmn29iolGA9b8Gd%2Bxa5oDOcWQMfoxOL0q7QII1f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgwzMjA3OTczNDUzMTEiDESy1mOgTN%2FUsA6%2FaCrBAj4d34fz7RNN1iFQodPnV9ggAACjFgQ7Vo94%2FBrdhbhDEelX98%2BP08UCjuxG01zY8vQYtcAFoxLkEbmr95KKxUpTyc9v7MTpbKltFrCuYW%2BpWYNsDp9x3by0CqsytfajJdlZAUoPEOWevuRq3DAZSMvQVIP4VIj%2B%2FSt%2BqDUI2xJ5x8KcCYQFEabSKUEiGXR6vHkHyXrI6JF6dX2KBTHR23HiQD1AtapEkngTaxI7mNNlu9Szuzrq8h8yG9ZBCf4Nen%2BzSYqgnibUHKeX7b9yWxqBCuYWqB0D3lefDsMr1Bdi6jj8HkrCMqPo5TQfoSbd3LtojrQxOpnCNUQ3y3n6hjYxDRrztsdQvfjL6HWaiwLHt0VL37lTI6ADv3fAhpDton%2BvF4VFQ9SkeqcD9TzWVqvUvC1Lnb5MOesXJKxF6tpt7DDx4t%2BhBjqzAutpkWhOur1dnT2aXqNSZKHuaBWXW1Hf7nWB1MOZHF7u2M8o8ZZuyq6ECHBH%2BAu06SMKrWYuBXlya3fZf%2BfILoQ742TwftTxW7In%2FQyqppBiVRiy%2B70i3qPok47Fc03Mb46KlGv58rIOsahyxqaCuAvmVYTw3gHG6mdHPg1793tDXQSWBIpUKsrU%2B73xAypC2QFG%2BHKFV44OMlUktZw0BWgCYVhFf6qmJqbjWJ1uJkHMsNSHtQNaRjKZErJDK%2Fyki3Hg6oIAOqyvVqlsgwwAMXPqhxo8Yb6lb%2FcIgTKamujKrY1k3ynD08WXPiPDRlYM3GpjKxFUB3EqoDRWy7tpFiSl6wYiemgEVH6q0xfrPBsVz5bLYYPkHLMiPYrCkbuZSMfYNCqd7eQS2L9kqOh3W%2BcWhHs%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20230413T121408Z&X-Amz-SignedHeaders=host&X-Amz-Expires=7200&X-Amz-Credential=ASIAUVMIDAYP2OZJPL6K%2F20230413%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Signature=c8b197b35dee2753f2b037d81f7fc38a08ebb02340a6c2d9bbcc2a9904cbf3b2'
# vérifier l'existence du fichier "best_model.pkl"
if not os.path.isfile("best_model.pkl"):
    # Téléchargement du fichier en utilisant requests
    response = requests.get(model_link)

    # Enregistrement du fichier pickle
    with open('best_model.pkl', 'wb') as f:
        f.write(response.content)


# Test sur l'existence du fichier explainer.pkl
explainer_link = 'https://p7-bucket-mlflow.s3.eu-west-3.amazonaws.com/explainer.pkl?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaDGV1LWNlbnRyYWwtMSJHMEUCIQDCpU1%2BOtb6bViemBRoDC1jQnACXPhz5UVnv5%2FrOUxMAQIgXNGuDx7iOZStmn29iolGA9b8Gd%2Bxa5oDOcWQMfoxOL0q7QII1f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgwzMjA3OTczNDUzMTEiDESy1mOgTN%2FUsA6%2FaCrBAj4d34fz7RNN1iFQodPnV9ggAACjFgQ7Vo94%2FBrdhbhDEelX98%2BP08UCjuxG01zY8vQYtcAFoxLkEbmr95KKxUpTyc9v7MTpbKltFrCuYW%2BpWYNsDp9x3by0CqsytfajJdlZAUoPEOWevuRq3DAZSMvQVIP4VIj%2B%2FSt%2BqDUI2xJ5x8KcCYQFEabSKUEiGXR6vHkHyXrI6JF6dX2KBTHR23HiQD1AtapEkngTaxI7mNNlu9Szuzrq8h8yG9ZBCf4Nen%2BzSYqgnibUHKeX7b9yWxqBCuYWqB0D3lefDsMr1Bdi6jj8HkrCMqPo5TQfoSbd3LtojrQxOpnCNUQ3y3n6hjYxDRrztsdQvfjL6HWaiwLHt0VL37lTI6ADv3fAhpDton%2BvF4VFQ9SkeqcD9TzWVqvUvC1Lnb5MOesXJKxF6tpt7DDx4t%2BhBjqzAutpkWhOur1dnT2aXqNSZKHuaBWXW1Hf7nWB1MOZHF7u2M8o8ZZuyq6ECHBH%2BAu06SMKrWYuBXlya3fZf%2BfILoQ742TwftTxW7In%2FQyqppBiVRiy%2B70i3qPok47Fc03Mb46KlGv58rIOsahyxqaCuAvmVYTw3gHG6mdHPg1793tDXQSWBIpUKsrU%2B73xAypC2QFG%2BHKFV44OMlUktZw0BWgCYVhFf6qmJqbjWJ1uJkHMsNSHtQNaRjKZErJDK%2Fyki3Hg6oIAOqyvVqlsgwwAMXPqhxo8Yb6lb%2FcIgTKamujKrY1k3ynD08WXPiPDRlYM3GpjKxFUB3EqoDRWy7tpFiSl6wYiemgEVH6q0xfrPBsVz5bLYYPkHLMiPYrCkbuZSMfYNCqd7eQS2L9kqOh3W%2BcWhHs%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20230413T124709Z&X-Amz-SignedHeaders=host&X-Amz-Expires=7200&X-Amz-Credential=ASIAUVMIDAYP2OZJPL6K%2F20230413%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Signature=c09d2179c6431bf278b96801e29b0b0673a50e05236857dab2edee4339d17570'
# vérifier l'existence du fichier "explainer.pkl"
if not os.path.isfile("explainer.pkl"):
    # Téléchargement du fichier en utilisant requests
    response = requests.get(explainer_link)

    # Enregistrement du fichier pickle
    with open('explainer.pkl', 'wb') as f:
        f.write(response.content)