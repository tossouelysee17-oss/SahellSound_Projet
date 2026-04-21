import json

def charger_catalogue(chemin="catalogue.json"):
    """
    Charge les données depuis le fichier JSON.
    Gère les erreurs de fichier absent ou corrompu (Exception Handling).
    """
    try:
        with open(chemin, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # Si problème, on retourne une liste vide pour ne pas faire planter le main
        return []

def sauvegarder_catalogue(catalogue, chemin="catalogue.json"):
    """
    Sauvegarde l'état actuel du catalogue dans le fichier JSON.
    L'argument 'indent=4' permet de garder le fichier lisible.
    """
    try:
        with open(chemin, 'w', encoding='utf-8') as f:
            json.dump(catalogue, f, indent=4, ensure_ascii=False)
            return True
    except Exception as e:
        print(f"Erreur lors de la sauvegarde : {e}")
        return False

def lister_artistes(catalogue):
    """
    Retourne une liste simplifiée pour l'affichage.
    Utilise .get() pour éviter les erreurs si la clé 'albums' manque.
    """
    liste_resume = []
    for artiste in catalogue:
        infos = {
            "nom": artiste["nom"],
            "genre": artiste["genre"],
            "pays": artiste["pays"],
            "nb_albums": len(artiste.get("albums", []))
        }
        liste_resume.append(infos)
    return liste_resume

def rechercher_artiste(catalogue, critere, valeur):
    """
    Recherche un artiste selon un critère (nom ou genre).
    Ignore la casse (majuscules/minuscules) pour plus de souplesse.
    """
    resultats = []
    for artiste in catalogue:
        # Vérification sécurisée de l'existence de la clé
        if critere in artiste and valeur.lower() in artiste[critere].lower():
            resultats.append(artiste)
    return resultats

def ajouter_artiste(catalogue, artiste):
    """
    Ajoute un artiste si son ID est unique.
    La persistance est assurée par l'appel à sauvegarder_catalogue.
    """
    for a in catalogue:
        if a["id"] == artiste["id"]:
            print(f"Erreur : L'identifiant {artiste['id']} existe déjà.")
            return False
            
    catalogue.append(artiste)
    return sauvegarder_catalogue(catalogue)

def ajouter_album(catalogue, id_artiste, album):
    """
    Ajoute un album à un artiste trouvé par son ID.
    """
    for artiste in catalogue:
        if artiste["id"] == id_artiste:
            # On initialise la liste d'albums si elle n'existe pas encore
            if "albums" not in artiste:
                artiste["albums"] = []
            artiste["albums"].append(album)
            return sauvegarder_catalogue(catalogue)
    return False