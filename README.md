=====================================================
          PROJET : SAHELSOUND RECORDS
             Gestion de Catalogue Musical
=====================================================

DESCRIPTION :
Application Python permettant de gérer un catalogue d'artistes 
et d'albums, avec un module d'analyse de données (Pandas) 
et de visualisation (Matplotlib).

FONCTIONNALITÉS :
- Consultation et recherche d'artistes.
- Ajout dynamique d'artistes et d'albums avec sauvegarde JSON.
- Statistiques globales (Top Artiste au cumul).
- Analyse par genre (Moyennes).
- Filtrage par année (Masque booléen).
- Exportation des données en rapport CSV.
- Graphiques de popularité.

STRUCTURE DU ZIP :
- main.py           : Point d'entrée de l'application (Menu).
- label.py          : Module de gestion des données (Chargement/Sauvegarde).
- analyse.py        : Module de traitement de données et graphiques.
- catalogue.json    : Base de données au format JSON.
- rapport.csv       : Export généré pour analyse externe.
- README.txt        : Le présent fichier.

PRÉREQUIS :
Pour lancer l'application, les bibliothèques suivantes sont nécessaires :
> pip install pandas matplotlib

LANCEMENT :
> python main.py

DÉVELOPPÉ PAR :
MEHOUE Manacé
KONOUHO Ulrich
DOHOUNNON Landry
ALESSI Davis
TOSSOU Elysée
=====================================================