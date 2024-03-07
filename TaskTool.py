def AjouterValeur  (dico, cle, valeur) : 
	dico[cle] = valeur 

def Suppression (dico, cle ):
        del dico [cle]
def TacheFinie(tache):
	if tache in MonDico :
	MonDico [tache]+= ("Terminee")
	else :
	print("La tache n'existe pas")



MonDico = {'name' : "John", 'age' : "31"} 

AjouterValeur(MonDico, 'ville', 'RH')
Suppression (MonDico, 'name')
TacheFinie ('name') 

print (MonDico)

