import pandas as pd
import matplotlib.pyplot as plt

def creer_dataframe(catalogue):
    """
    Transforme la liste de dictionnaires (JSON) en un tableau Pandas (DataFrame).
    On 'aplatit' les données pour avoir une ligne par album.
    """
    donnees_plates = []
    
    for artiste in catalogue:
        # Si l'artiste n'a pas encore d'album, on crée quand même une ligne avec 0 streams
        if not artiste['albums']:
            donnees_plates.append({
                "nom": artiste['nom'],
                "genre": artiste['genre'],
                "album": "Aucun",
                "streams": 0
            })
        else:
            for album in artiste['albums']:
                donnees_plates.append({
                    "nom": artiste['nom'],
                    "genre": artiste['genre'],
                    "album": album['titre'],
                    "streams": album['streams']
                })
    
    if not donnees_plates:
        return None
        
    return pd.DataFrame(donnees_plates)

def generer_graphique(df):
    """Génère un graphique en barres du total des streams par artiste."""
    # On groupe par nom d'artiste et on fait la somme des streams
    stats = df.groupby('nom')['streams'].sum().sort_values(ascending=False)
    
    # Création du graphique
    plt.figure(figsize=(10, 6))
    stats.plot(kind='bar', color='gold', edgecolor='black')
    plt.title('Popularité des Artistes (Total Streams)')
    plt.ylabel('Nombre de Streams')
    plt.xlabel('Artistes')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()