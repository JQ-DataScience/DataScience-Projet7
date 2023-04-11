import os
import requests


# Test sur l'existence du fichier data_OHE.csv
if not os.path.isfile('data_OHE.csv'):
    url = "https://gist.githubusercontent.com/JQ-DataScience/6ee7f21195acceee0b70e1162a03d087/raw/bd8ad2a095021511256972df87ea1839f4ca8bc5/data_OHE.csv"
    response = requests.get(url)
    with open('data_OHE.csv', 'wb') as f:
        f.write(response.content)



model_link = 'https://p7-bucket-mlflow.s3.eu-west-3.amazonaws.com/artifacts/891670944991620342/db67dfa076c448deae28cfd1318d5f17/artifacts/model/model.pkl?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaDGV1LWNlbnRyYWwtMSJHMEUCIQC%2FyVCGDFpPfyDw00Lh2rAVk9rKjfjEF74Ip3i8ymC%2BCwIgVgt7piOU7hiep%2BCdhARUQbpTji%2B3mp7IRxktlbMtT2Mq7QIIqv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgwzMjA3OTczNDUzMTEiDAoTvwW4TFuk5Uan3yrBAu11hpv9RQ%2F0HZyfMy98fC8VSCHIyLgJ9PXqoHsu%2FFaufUpoRWkbpdjZTM7FHY27YHSZQ6ltnbQRmDGPrjOMicbQM3Usu4icuA5Z4eX36BTzUfv74XcoNIMfBU9lNzuHCq7DWD0fNsX1%2BDljWeD03pqRBIzX6EKlgm2WtSMNiDTbNnLoaTO9EliZe%2BlNHL6JesHE5FQiCaoLxsq4gdVylC2MCiinsIcoCFrUQXYu2Lao5aFfIkFNLemoumShJxwOLEbylYqowhXRkXfPj%2BoGGxG6AFMIvycezlK1X7C4Aq7ZVJmyINDDAH3x%2FZjcoE4SwQ96dk6b3FFlTBIR5lloFL008X3etk%2FkipP0z8o%2F0vgoldkc%2FexblVDOU3l57nLSoJ245wG7%2BuPscETL7cQKaxsVbPO9iDKLkP4mXY2OLB4IVTCeptahBjqzAtyjh3Hrt66mv2wlrNjqzvbU8vbgwwWzHhaidrDhJMbOQi%2Bvs3I7Vim7wxA8XOsVWUJcB6sCv9C6Id2JyuIagXGGulYerUaNZJM1DrIHCVeGaHEKWWN9hsYLb47SPF17KZP3G3s6DhmWMO6an74pmR1R6LOruAgnqv4I2LTTqJy8iAn25qtiuvFMLg83oHAxLPsDPCXAniURq5TQ7PK0b3fnrfZ5dRraFTRzCHqRQrGPtWQvaWumdrL0Bz99SeS64gm%2BnbT8W4oFxSPDex2G5Of70zyibBMmhfxZTuuSIi7lM%2FjGZz1aYlQFcqaWXC73Ibv%2FC7wmj4zpm7O7BKKqrOy49FctXwXTmZ2gHnl4bo8gQBoUT%2B692EAFE60j13vQ4ACdGn2nAeCYV2HGOHM2lZhvt3g%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20230411T173403Z&X-Amz-SignedHeaders=host&X-Amz-Expires=1800&X-Amz-Credential=ASIAUVMIDAYPU3ODKY4K%2F20230411%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Signature=7057f75372fbfc714869b070c77c5784f9e588a8f042a95ba9f696c3b0ad8c13https://p7-bucket-mlflow.s3.eu-west-3.amazonaws.com/artifacts/891670944991620342/db67dfa076c448deae28cfd1318d5f17/artifacts/model/model.pkl?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaDGV1LWNlbnRyYWwtMSJHMEUCIQC%2FyVCGDFpPfyDw00Lh2rAVk9rKjfjEF74Ip3i8ymC%2BCwIgVgt7piOU7hiep%2BCdhARUQbpTji%2B3mp7IRxktlbMtT2Mq7QIIqv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgwzMjA3OTczNDUzMTEiDAoTvwW4TFuk5Uan3yrBAu11hpv9RQ%2F0HZyfMy98fC8VSCHIyLgJ9PXqoHsu%2FFaufUpoRWkbpdjZTM7FHY27YHSZQ6ltnbQRmDGPrjOMicbQM3Usu4icuA5Z4eX36BTzUfv74XcoNIMfBU9lNzuHCq7DWD0fNsX1%2BDljWeD03pqRBIzX6EKlgm2WtSMNiDTbNnLoaTO9EliZe%2BlNHL6JesHE5FQiCaoLxsq4gdVylC2MCiinsIcoCFrUQXYu2Lao5aFfIkFNLemoumShJxwOLEbylYqowhXRkXfPj%2BoGGxG6AFMIvycezlK1X7C4Aq7ZVJmyINDDAH3x%2FZjcoE4SwQ96dk6b3FFlTBIR5lloFL008X3etk%2FkipP0z8o%2F0vgoldkc%2FexblVDOU3l57nLSoJ245wG7%2BuPscETL7cQKaxsVbPO9iDKLkP4mXY2OLB4IVTCeptahBjqzAtyjh3Hrt66mv2wlrNjqzvbU8vbgwwWzHhaidrDhJMbOQi%2Bvs3I7Vim7wxA8XOsVWUJcB6sCv9C6Id2JyuIagXGGulYerUaNZJM1DrIHCVeGaHEKWWN9hsYLb47SPF17KZP3G3s6DhmWMO6an74pmR1R6LOruAgnqv4I2LTTqJy8iAn25qtiuvFMLg83oHAxLPsDPCXAniURq5TQ7PK0b3fnrfZ5dRraFTRzCHqRQrGPtWQvaWumdrL0Bz99SeS64gm%2BnbT8W4oFxSPDex2G5Of70zyibBMmhfxZTuuSIi7lM%2FjGZz1aYlQFcqaWXC73Ibv%2FC7wmj4zpm7O7BKKqrOy49FctXwXTmZ2gHnl4bo8gQBoUT%2B692EAFE60j13vQ4ACdGn2nAeCYV2HGOHM2lZhvt3g%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20230411T173403Z&X-Amz-SignedHeaders=host&X-Amz-Expires=1800&X-Amz-Credential=ASIAUVMIDAYPU3ODKY4K%2F20230411%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Signature=7057f75372fbfc714869b070c77c5784f9e588a8f042a95ba9f696c3b0ad8c13'
# vérifier l'existence du fichier "best_model.pkl"
if not os.path.isfile("best_model.pkl"):
    # Téléchargement du fichier en utilisant requests
    response = requests.get(model_link)

    # Enregistrement du fichier pickle
    with open('best_model.pkl', 'wb') as f:
        f.write(response.content)