import streamlit as st
import pandas as pd
import requests
import json
import logging


################## requests from back end ####################
serveur = 'http://127.0.0.1:5000/'

## request get_ids
response = requests.get(serveur+'get_ids')
get_ids  = response.json()

################## HTML ####################


# Données d'exemple

# Entête centrée
st.title("Simulateur de crédits 3000")

# Menu déroulant
selected_id = st.selectbox("Sélectionnez un ID", get_ids)






#logging.warning(str(get_ids))
#logging.warning(type(get_ids))

## request data
response = requests.get(serveur+'data/'+str(selected_id))
data = pd.DataFrame(response.json())    

#logging.warning(response.status_code)
#logging.warning(response.text)
#logging.warning(response.json())
# Convertir les données JSON en un objet Python
    #json_data = response.json()

    # Convertir les données en un DataFrame
    #df = pd.DataFrame(json_data)



## request predictions
response = requests.get(serveur+'predict/'+str(selected_id))
predict  = response.json()


## request shap according to ids
response = requests.get(serveur+'shap/'+str(selected_id))
shap  = response.json()

## request shap according to ids
response = requests.get(serveur+'graph/'+str(selected_id))
graph  = response.json()

# Trier les valeurs du JSON par ordre croissant tout en conservant les clés
sorted_shap = {}
for key, value in sorted(shap.items(), key=lambda item: item[1]):
    sorted_shap[key] = value







# Données textuelles

st.title("Informations client")
if selected_id:
    st.write(data)
        
 

# Données de prédiction
st.title("Scoring")
st.write("Prédiction:")
st.json(predict)

# Données SHAP
st.title("Composantes déterminante dans la décision")
st.write("SHAP:")
st.json(sorted_shap)   


# Données SHAP
st.title("Graphique")
st.write("GRAPH")
#st.json(graph)   


################## GRAPHS ####################

import plotly.graph_objs as go

# Définir les données de votre graphique
x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

# Créer la figure correspondante à l'aide de Plotly
fig = go.Figure(data=go.Scatter(x=x, y=y))


# Ajouter la figure à votre application Streamlit
st.plotly_chart(fig)

# Ajouter un curseur pour modifier la valeur de x en temps réel
x_value = st.slider("Valeur de x :", min_value=1, max_value=10, value=5)

# Mettre à jour les données de votre graphique avec la valeur de x modifiée
y = [i*x_value for i in y]
fig = go.Figure(data=go.Scatter(x=x, y=y))

# Ajouter la figure mise à jour à votre application Streamlit
st.plotly_chart(fig)
