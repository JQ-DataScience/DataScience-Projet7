import streamlit as st
import pandas as pd
import requests
import json
import logging


################## requests from back end ####################
serveur = 'http://13.37.142.213:5000/'

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
predict  = json.dumps(response.json())


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
prediction_data = json.loads(predict)
st.write(prediction_data['prediction'][0])
# Afficher l'entête "SCORING" en majuscules
st.title("SCORING")

# Récupérer la valeur de prédiction
prediction = prediction_data["prediction"][1]

# Récupérer le pourcentage de la prédiction
pourcentage = prediction_data["pourcentage"]

# Vérifier si la valeur de prédiction est égale à 0
if int(prediction) == 0:
    # Afficher "Vers" en vert
    st.write("Prédiction: ", "<span style='color:green;font-weight:bold'> Avis favorable </span>", unsafe_allow_html=True)
    st.markdown("""<div style='border: 2px solid green; padding: 10px; color: green; text-transform: uppercase; font-weight: bold;'>Risque de défaut de crédit acceptable</div>""", unsafe_allow_html=True)

else:
    # Afficher la valeur de prédiction en rouge
    st.write("Prédiction: ", "<span style='color:red;font-weight:bold'> Avis défavorable" + str(prediction) +"</span>", unsafe_allow_html=True)
    # Afficher le texte "Risque de défaut de crédit important" en rouge et majuscule dans un cadre avec une bordure rouge
    st.markdown("""<div style='border: 2px solid red; padding: 10px; color: red; text-transform: uppercase; font-weight: bold;'>Risque de défaut de crédit important</div>""", unsafe_allow_html=True)

# Afficher le pourcentage de la prédiction
st.write("Pourcentage: ", pourcentage)

##########################data###############################
# TEST COLORISATION PREDICTION

#import plotly.graph_objs as go
#import numpy as np



# Les données fournies
#json_data = predict
#json_data = json.loads(json_data.js#on())


#pourcentage = np.array(json_data['pourcentage'])
#prediction = np.array(json_data['prediction'])

# La définition des couleurs
#colors = ['green' if p == 0 else 'red' for p in prediction]

# La création de la table
#table_data = go.Table(
#    header=dict(values=['Pourcentage', 'Prediction'],
#                fill_color='lightgrey',
#                align='left'),
#    cells=dict(values=[pourcentage[0], prediction],
#               fill_color=[colors],
#               align='left'))
#
# L'affichage de la table
#st.plotly_chart(table_data)



#########################################################

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

# Ajouter une colonne pour la couleur en fonction de la valeur SHAP
shap_df['Color'] = shap_df['SHAP Value'].apply(lambda x: 'blue' if abs(x) < 0.1 else 'green' if x >= 0 else 'orange')

# Afficher le graphique beeswarm avec des couleurs de point personnalisées
fig2 = px.scatter(shap_df, x='SHAP Value', orientation='h', color='Color', color_discrete_map={'blue':'blue', 'green':'green', 'orange':'orange'})
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

################## GRAPH 3  ####################


# Sélectionner l'individu pour lequel on veut afficher les données
individu = data.index[0]

# Sélectionner les caractéristiques à afficher
features = st.multiselect("Sélectionnez les caractéristiques à afficher", data.columns)

# Sous-ensemble de données pour l'individu sélectionné et les caractéristiques sélectionnées
subset = data.loc[individu, features]

# Sous-ensemble des données de describe() pour les caractéristiques sélectionnées
describe_subset = graph 

# Créer un graphique pour chaque caractéristique sélectionnée
for feature in features:
    fig = px.scatter(x=[subset[feature]], y=[feature], color_discrete_sequence=['blue'])
    fig.add_vline(x=describe_subset.loc['min', feature], line_dash='dash', line_color='red', name='min')
    fig.add_vline(x=describe_subset.loc['25%', feature], line_dash='dash', line_color='orange', name='1er quartile')
    fig.add_vline(x=describe_subset.loc['50%', feature], line_dash='dash', line_color='green', name='médiane')
    fig.add_vline(x=describe_subset.loc['75%', feature], line_dash='dash', line_color='orange', name='3ème quartile')
    fig.add_vline(x=describe_subset.loc['max', feature], line_dash='dash', line_color='red', name='max')
    fig.add_vline(x=describe_subset.loc['mean', feature], line_dash='dash', line_color='purple', name='moyenne')
    fig.update_layout(showlegend=True)
    st.plotly_chart(fig)
