import label
import analyse

def afficher_menu():
    """Affiche le menu principal de l'application."""
    print("\n" + "="*25)
    print("   SAHELSOUND RECORDS   ")
    print("="*25)
    print("1. Consulter le catalogue")
    print("2. Ajouter un artiste")
    print("3. Ajouter un album")
    print("4. Statistiques et rapport")
    print("5. Quitter")

def main():
    # Chargement initial des données
    catalogue = label.charger_catalogue()
    
    while True:
        afficher_menu()
        choix = input("\nFaites votre choix (1-5) : ").strip()
        
        if choix == "1":
            print("\n--- CONSULTATION ---")
            print("a. Lister tous les artistes")
            print("b. Rechercher un artiste")
            sous_choix = input("Votre choix (a/b) : ").lower().strip()

            if sous_choix == "a":
                artistes = label.lister_artistes(catalogue)
                print("\nListe des artistes enregistrés :")
                for a in artistes:
                    print(f"- {a['nom']} ({a['genre']}) | Pays: {a['pays']} | Albums: {a['nb_albums']}")
            
            elif sous_choix == "b":
                critere = input("Chercher par (nom/genre) : ").lower().strip()
                if critere in ["nom", "genre"]:
                    valeur = input(f"Entrez le {critere} à rechercher : ")
                    resultats = label.rechercher_artiste(catalogue, critere, valeur)
                    if resultats:
                        for r in resultats:
                            print(f"✅ Trouvé : {r['nom']} (ID: {r['id']}) - {len(r['albums'])} album(s)")
                    else:
                        print("❌ Aucun artiste ne correspond à votre recherche.")
                else:
                    print("❌ Critère invalide.")

        elif choix == "2":
            print("\n--- AJOUTER UN NOUVEL ARTISTE ---")
            id_art = input("ID de l'artiste (ex: ART-001) : ").strip()
            nom = input("Nom de l'artiste : ").strip()
            genre = input("Genre musical : ").strip()
            pays = input("Pays d'origine : ").strip()
            
            nouvel_artiste = {
                "id": id_art,
                "nom": nom,
                "genre": genre,
                "pays": pays,
                "albums": []
            }
            
            if label.ajouter_artiste(catalogue, nouvel_artiste):
                label.sauvegarder_catalogue(catalogue, "catalogue.json")
                print(f"✨ L'artiste {nom} a été ajouté et sauvegardé !")
            else:
                print("⚠️ Erreur : Impossible d'ajouter l'artiste.")

        elif choix == "3":
            print("\n--- AJOUTER UN ALBUM ---")
            id_cible = input("Entrez l'ID de l'artiste : ").strip()
            titre = input("Titre de l'album : ").strip()
            try:
                annee = int(input("Année de sortie : "))
                streams = int(input("Nombre de streams : "))
                
                nouvel_album = {
                    "titre": titre,
                    "annee": annee,
                    "streams": streams
                }
                
                if label.ajouter_album(catalogue, id_cible, nouvel_album):
                    label.sauvegarder_catalogue(catalogue, "catalogue.json")
                    print(f"💿 L'album '{titre}' a bien été rattaché à l'artiste.")
                else:
                    print("❌ Artiste introuvable. Vérifiez l'ID.")
            except ValueError:
                print("❌ Erreur : L'année et les streams doivent être des nombres entiers.")

        elif choix == "4":
            df = analyse.creer_dataframe(catalogue)
            if df is not None:
                # --- CALCUL DU TOP ARTISTE PAR CUMUL TOTAL ---
                top_serie = df.groupby('nom')['streams'].sum()
                nom_top = top_serie.idxmax() 
                total_streams = top_serie.max() 

                print("\n" + "⭐"*10 + " TOP GLOBAL " + "⭐"*10)
                print(f"L'artiste n°1 au cumul des streams est : {nom_top}")
                print(f"Total catalogue : {total_streams} streams")
                print("="*32)

                while True:
                    print("\n--- ANALYSE ET STATISTIQUES ---")
                    print("a. Top 5 artistes (Graphique)")
                    print("b. Moyenne des streams par genre")
                    print("c. Filtrer par année (Masque Booléen)")
                    print("d. Exporter le rapport CSV")
                    print("q. Retour au menu principal")
                    
                    sous_choix = input("\nVotre choix (a/b/c/d/q) : ").lower().strip()

                    if sous_choix == 'a':
                        analyse.generer_graphique(df)
                    elif sous_choix == 'b':
                        print("\n--- MOYENNE DES STREAMS PAR GENRE ---")
                        # On calcule la moyenne, on arrondit et on enlève les virgules
                        moyennes = df.groupby('genre')['streams'].mean().round(0).astype(int)
                        
                        for genre, valeur in moyennes.items():
                            print(f"- {genre} : {valeur:,} streams en moyenne")
                    elif sous_choix == 'c':
                        try:
                            annee_min = int(input("Afficher les albums à partir de l'année : "))
                            # Appel de la fonction corrigée
                            df_filtre = analyse.filtrer_par_annee(df, annee_min)
                            print(f"\n--- ALBUMS DEPUIS {annee_min} ---")
                            print(df_filtre if not df_filtre.empty else "Aucun résultat.")
                        except ValueError:
                            print("❌ Année invalide.")
                    elif sous_choix == 'd':
                        analyse.exporter_csv(df)
                    elif sous_choix == 'q':
                        break
            else:
                print("⚠️ Catalogue vide ou corrompu. Analyse impossible.")

        elif choix == "5":
            print("👋 Merci d'avoir utilisé SahelSound Records. À bientôt !")
            break
        else:
            print("❌ Choix invalide (1-5 uniquement).")

if __name__ == "__main__":
    main()