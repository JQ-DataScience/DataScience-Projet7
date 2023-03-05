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

## request graph according to ids
response = requests.get(serveur+'graph/'+str(selected_id))
graph  = pd.DataFrame(response.json())

st.write(graph)

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


################## GRAPHS  ####################

import plotly.graph_objs as go
import plotly.express as px


################## GRAPH 1  ####################


# Convertir le JSON en un dataframe pandas
shap_df = pd.DataFrame.from_dict(sorted_shap, orient='index', columns=['SHAP Value'])

# Afficher le graphique beeswarm
fig2 = px.scatter(shap_df, x='SHAP Value', orientation='h')
st.plotly_chart(fig2)

################## GRAPH 2  ####################

# Options de sélection pour les variables et l'individu
options_vars = data.columns.tolist()


# Sélection par défaut : la première variable et le premier individu
selected_var = options_vars[0]


# Sélection de la variable à afficher via un menu déroulant
selected_var = st.sidebar.selectbox("Choisissez la variable à afficher", options_vars)

# Calcul des statistiques descriptives pour chaque variable
stats = graph

# Récupération des min et max de la variable sélectionnée
var_min = stats.loc["min", selected_var]
var_max = stats.loc["max", selected_var]

# Création du graphique avec Plotly
fig = go.Figure()

# Ajout d'un histogramme pour la variable sélectionnée
fig.add_trace(
    go.Histogram(
        x=data[selected_var],
        nbinsx=20,
        name=selected_var
    )
)

# Ajout d'un marqueur pour le minimum
fig.add_trace(
    go.Scatter(
        x=[var_min],
        y=[0],
        mode="markers",
        marker=dict(size=10, color="red"),
        name="Minimum"
    )
)

# Ajout d'un marqueur pour le maximum
fig.add_trace(
    go.Scatter(
        x=[var_max],
        y=[0],
        mode="markers",
        marker=dict(size=10, color="green"),
        name="Maximum"
    )
)

### Ajout des valeurs de l'individu sélectionné
indiv_values = data.loc[ :, :]
#for i, (var, value) in enumerate(indiv_values.iteritems()):
#    fig.add_annotation(
#        x=value,
#        y=i,
#        text=str(value),
#        showarrow=True,
#        arrowhead=1,
#        font=dict(color="white"),
#        bgcolor="blue",
#        opacity=0.8
#    )

# Configuration du layout du graphique
fig.update_layout(
    title=f"Distribution de {selected_var}, Minimum = {var_min}, Maximum = {var_max}",
    xaxis_title=selected_var,
    yaxis_title="Fréquence",
    bargap=0.1,
    height=600,
    margin=dict(l=50, r=50, b=50, t=100)
)

# Affichage du graphique
st.plotly_chart(fig)


