import label

def afficher_menu():
    print("\n=== SAHELSOUND RECORDS ===")
    print("1. Consulter le catalogue")
    print("2. Ajouter un artiste")
    print("3. Ajouter un album")
    print("4. Statistiques et rapport")
    print("5. Quitter")

def main():
    # On charge les données au démarrage
    catalogue = label.charger_catalogue()
    
    while True:
        afficher_menu()
        choix = input("Faites votre choix (1-5) : ")
        
        if choix == "1":
            print("\n--- CONSULTATION ---")
            print("a. Lister tous les artistes")
            print("b. Rechercher un artiste")
            sous_choix = input("Votre choix (a/b) : ").lower()

            if sous_choix == "a":
                artistes = label.lister_artistes(catalogue)
                print("\nListe des artistes :")
                for a in artistes:
                    print(f"- {a['nom']} ({a['genre']}) | Pays: {a['pays']} | Albums: {a['nb_albums']}")
            
            elif sous_choix == "b":
                critere = input("Chercher par (nom/genre) : ").lower()
                valeur = input(f"Entrez le {critere} à rechercher : ")
                resultats = label.rechercher_artiste(catalogue, critere, valeur)
                
                if resultats:
                    for r in resultats:
                        print(f"Trouvé : {r['nom']} - ID: {r['id']}")
                else:
                    print("Aucun artiste trouvé.")
        elif choix == "2":
            print("\n--- AJOUTER UN NOUVEL ARTISTE ---")
            # 1. Collecte des informations
            id_art = input("ID de l'artiste (ex: ART-001) : ")
            nom = input("Nom de l'artiste : ")
            genre = input("Genre musical : ")
            pays = input("Pays d'origine : ")
            
            # 2. Création du dictionnaire selon la structure du sujet
            nouvel_artiste = {
                "id": id_art,
                "nom": nom,
                "genre": genre,
                "pays": pays,
                "albums": [] # On commence avec une liste d'albums vide
            }
            
            # 3. Appel au moteur (label.py) pour valider et enregistrer
            if label.ajouter_artiste(catalogue, nouvel_artiste):
                print(f"L'artiste {nom} a été ajouté avec succès !")
            else:
                print("L'ajout a échoué (vérifiez si l'ID existe déjà).")
        elif choix == "3":
            print("\n--- AJOUTER UN ALBUM ---")
            # 1. On identifie l'artiste cible
            id_cible = input("Entrez l'ID de l'artiste : ")
            
            # 2. On collecte les infos de l'album
            titre = input("Titre de l'album : ")
            # On convertit les entrées numériques tout de suite
            try:
                annee = int(input("Année de sortie : "))
                streams = int(input("Nombre de streams : "))
            except ValueError:
                print("Erreur : L'année et les streams doivent être des nombres !")
                continue # On repart au menu si l'utilisateur tape n'importe quoi
            
            # 3. On prépare le dictionnaire de l'album
            nouvel_album = {
                "titre": titre,
                "annee": annee,
                "streams": streams
            }
            
            # 4. On demande au moteur de faire la liaison
            if label.ajouter_album(catalogue, id_cible, nouvel_album):
                print(f"L'album '{titre}' a été ajouté au catalogue !")
            else:
                print("Artiste introuvable. Vérifiez l'ID.")

        elif choix == "4":
            print("\n--- ANALYSE ET STATISTIQUES ---")
            # On importe analyse ici ou en haut du fichier
            import analyse 
            
            # On transforme notre catalogue en "DataFrame" (Tableau Pandas)
            df = analyse.creer_dataframe(catalogue)
            
            if df is not None:
                print("\nRésumé des statistiques :")
                # Affiche les 5 premières lignes du tableau pour vérifier
                print(df.head()) 
                
                # Calcul du top artiste
                top_artiste = df.loc[df['streams'].idxmax()]
                print(f"\nL'artiste le plus streamé est : {top_artiste['nom']} "
                      f"avec {top_artiste['streams']} streams !")
                
                # Optionnel : Générer le graphique
                reponse = input("Voulez-vous générer le graphique des streams ? (o/n) : ")
                if reponse.lower() == 'o':
                    analyse.generer_graphique(df)
            else:
                print("Le catalogue est vide. Pas d'analyse possible.")

        elif choix == "5":
            print("Merci d'avoir utilisé SahelSound Records. À bientôt !")
            break
        else:
            print("Choix invalide. Veuillez entrer un chiffre entre 1 et 5.")            
if __name__ == "__main__":
    main()