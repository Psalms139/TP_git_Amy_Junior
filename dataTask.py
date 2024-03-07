import json

def enregistrer_json (dictionnaire, chemin_fichier):
	with open(chemin_fichier, 'w') as fichier:
		json.dump(dictionnaire, fichier)

def charger_json (chemin_fichier):
	with open(chemin_fichier, 'r') as fichier:
		contenu_json = json.load(fichier)
	return contenu_json

if __name__== "__main__":
	dict={"toto":42}
	enregistrer_json(dict,"/home/student/")
