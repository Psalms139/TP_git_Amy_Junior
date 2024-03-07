 taskDisplay.py

import json
import os

def charger_json(chemin_fichier):
    """
    Charge un fichier JSON et renvoie son contenu sous forme de dictionnaire.

    Args:
        chemin_fichier (str): Le chemin du fichier JSON à charger.

    Returns:
        dict: Le contenu du fichier JSON sous forme de dictionnaire.
    """
    with open(chemin_fichier, 'r') as fichier:
        contenu_json = json.load(fichier)
    return contenu_json

def enregistrer_json(dictionnaire, chemin_fichier):
    """
    Enregistre un dictionnaire dans un fichier JSON.

    Args:
        dictionnaire (dict): Le dictionnaire à enregistrer.
        chemin_fichier (str): Le chemin du fichier JSON dans lequel enregistrer le dictionnaire.

    Returns:
        None
    """
    with open(chemin_fichier, 'w') as fichier:
        json.dump(dictionnaire, fichier)

def creer_liste_taches():
    """
    Crée une nouvelle liste de tâches en demandant à l'utilisateur d'entrer des tâches.

    Returns:
        dict: Le dictionnaire contenant la liste de tâches.
    """
    liste_taches = {}
    while True:
        tache = input("Entrez une nouvelle tâche ou 'q' pour quitter : ")
        if tache.lower() == 'q':
            break
        liste_taches[len(liste_taches) + 1] = {"tache": tache, "complete": False}
    return liste_taches

def afficher_liste_taches(liste_taches):
    """
    Affiche la liste de tâches.

    Args:
        liste_taches (dict): Le dictionnaire contenant la liste de tâches.
    """
    print("Liste de tâches :")
    for numero, tache in liste_taches.items():
        etat = "complète" if tache["complete"] else "non complète"
        print(f"{numero}. {tache['tache']} - {etat}")

def main():
    print("Bienvenue dans le gestionnaire de tâches!")
    choix = input("Que souhaitez-vous faire ? (charger / créer) : ")

    if choix.lower() == "charger":
        chemin_fichier = input("Entrez le chemin du fichier JSON : ")
        if os.path.exists(chemin_fichier):
            liste_taches = charger_json(chemin_fichier)
            afficher_liste_taches(liste_taches)
        else:
            print("Le fichier spécifié n'existe pas.")
    elif choix.lower() == "créer":
        liste_taches = creer_liste_taches()
        afficher_liste_taches(liste_taches)
        sauvegarder = input("Voulez-vous sauvegarder cette liste de tâches ? (oui / non) : ")
        if sauvegarder.lower() == "oui":
            chemin_fichier = input("Entrez le chemin du fichier JSON pour sauvegarder : ")
            enregistrer_json(liste_taches, chemin_fichier)
            print("Liste de tâches sauvegardée avec succès.")
    else:
        print("Choix invalide. Veuillez entrer 'charger' ou 'créer'.")

if __name__ == "__main__":
    main()
