import requests

# Liste des URLs à tester
urls = ['http://127.0.0.1:5000/get_ids',
       'http://127.0.0.1:5000/data/380921',
        'http://127.0.0.1:5000/predict/380921',
        'http://127.0.0.1:5000/shap/380921'
        
        ]

# Parcourir la liste des URLs
for url in urls:
    try:
        # Effectuer une requête GET à l'URL
        response = requests.get(url)

        # Vérifier le code de réponse et la réponse HTTP
        if response.status_code == 200:
            print("----------------------------------------------------------------------------------------")
            print(f"{url} est en ligne, code de réponse : {response.status_code}")
            print(f"{url} est en ligne, réponse : {response._content}")
        else:
            print("----------------------------------------------------------------------------------------")
            print(f"{url} est en ligne mais avec un code de réponse : {response.status_code}")

    except requests.exceptions.RequestException as e:
        # Si une exception est levée, l'URL est hors-ligne
        print(f"{url} est hors ligne : {e}")


"""Dans cet exemple, nous utilisons la bibliothèque requests pour effectuer des requêtes HTTP. Nous avons une liste d'URL à tester, que nous parcourons à l'aide d'une boucle for. Pour chaque URL, nous essayons d'effectuer une requête GET en utilisant requests.get(). Si une exception est levée, cela signifie que l'URL est hors-ligne et nous affichons un message d'erreur. Si la requête est réussie, nous vérifions le code de réponse HTTP en utilisant response.status_code et affichons le message approprié."""