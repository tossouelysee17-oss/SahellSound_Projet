import pandas as pd
import matplotlib.pyplot as plt

def creer_dataframe(catalogue):
    """
    Transforme la liste de dictionnaires (JSON) en un DataFrame Pandas.
    On 'aplatit' les données pour avoir une ligne par album (Exigence TP).
    """
    donnees_plates = []
    
    for artiste in catalogue:
        if not artiste.get('albums'):
            donnees_plates.append({
                "nom": artiste['nom'],
                "genre": artiste['genre'],
                "album": "Aucun",
                "annee": 0,
                "streams": 0
            })
        else:
            for album in artiste['albums']:
                donnees_plates.append({
                    "nom": artiste['nom'],
                    "genre": artiste['genre'],
                    "album": album['titre'],
                    "annee": album.get('annee', 0),
                    "streams": album['streams']
                })
    
    return pd.DataFrame(donnees_plates) if donnees_plates else None

def filtrer_par_annee(df, annee_min):
    """
    Filtre les albums par année avec un MASQUE BOOLLÉEN (Point clé du TP).
    """
    # Création du masque booléen
    masque = df['annee'] >= annee_min
    return df[masque]

def generer_graphique(df):
    """Génère et sauvegarde un graphique des streams par artiste."""
    stats = df.groupby('nom')['streams'].sum().sort_values(ascending=False)
    
    plt.figure(figsize=(10, 6))
    stats.plot(kind='bar', color='gold', edgecolor='black')
    plt.title('Popularité des Artistes (Total Streams)')
    plt.ylabel('Nombre de Streams')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Sauvegarde en PNG demandée dans l'énoncé
    plt.savefig("graphique_streams.png")
    plt.show()

def exporter_csv(df):
    """Exporte le rapport en CSV sans perdre les accents (utf-8-sig)."""
    try:
        df.to_csv("rapport.csv", index=False, encoding='utf-8-sig')
        print("✅ Rapport exporté : 'rapport.csv'")
        return True
    except Exception as e:
        print(f"❌ Erreur export CSV : {e}")
        return False