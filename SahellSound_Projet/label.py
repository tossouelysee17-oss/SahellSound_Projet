import json

def charger_catalogue(chemin="catalogue.json"):
    """
    Charge et retourne les données depuis le fichier JSON. [cite: 21]
    Si le fichier est absent ou corrompu, retourne une liste vide. 
    """
    try:
        with open(chemin, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # Gestion d'exception : fichier manquant ou vide 
        return []

def sauvegarder_catalogue(catalogue, chemin="catalogue.json"):
    """
    Écrit les données du catalogue dans le fichier JSON. [cite: 22]
    """
    try:
        with open(chemin, 'w', encoding='utf-8') as f:
            # indent=4 rend le fichier lisible par un humain
            json.dump(catalogue, f, indent=4, ensure_ascii=False)
            return True
    except Exception as e:
        print(f"Erreur lors de la sauvegarde : {e}")
        return False
    

def lister_artistes(catalogue):
    """
    Parcourt le catalogue et retourne une liste de dictionnaires simplifiés
    contenant : nom, genre, pays et le nombre d'albums. [cite: 31, 52]
    """
    liste_resume = []
    for artiste in catalogue:
        infos = {
            "nom": artiste["nom"],
            "genre": artiste["genre"],
            "pays": artiste["pays"],
            "nb_albums": len(artiste["albums"])
        }
        liste_resume.append(infos)
    return liste_resume

def rechercher_artiste(catalogue, critere, valeur):
    """
    Recherche un artiste par nom ou par genre musical. [cite: 32, 57]
    Retourne une liste des artistes correspondants.
    """
    resultats = []
    for artiste in catalogue:
        # On compare en minuscule pour ignorer la casse
        if valeur.lower() in artiste[critere].lower():
            resultats.append(artiste)
    return resultats

def ajouter_artiste(catalogue, artiste):
    """
    Ajoute un nouvel artiste après avoir vérifié que l'ID est unique. [cite: 36, 57]
    Sauvegarde immédiatement les modifications. [cite: 37]
    """
    # Vérification de l'identifiant unique 
    for a in catalogue:
        if a["id"] == artiste["id"]:
            print(f"Erreur : L'identifiant {artiste['id']} existe déjà.")
            return False
            
    catalogue.append(artiste)
    # Persistance : on met à jour le fichier JSON tout de suite [cite: 65]
    sauvegarder_catalogue(catalogue)
    return True

def ajouter_album(catalogue, id_artiste, album):
    """
    Cherche un artiste par son ID et lui ajoute un nouvel album.
    Sauvegarde ensuite le catalogue mis à jour.
    """
    for artiste in catalogue:
        if artiste["id"] == id_artiste:
            # On ajoute l'album à la liste des albums de cet artiste
            artiste["albums"].append(album)
            # On enregistre la modification dans le fichier JSON
            sauvegarder_catalogue(catalogue)
            return True
    return False