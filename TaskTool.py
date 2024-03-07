def AjouterValeur  (dico, cle, valeur) : 
	dico[cle] = valeur 

def Suppression (dico, cle ):
        del dico [cle]


MonDico = {'name' : "John", 'age' : "31"} 

AjouterValeur(MonDico, 'ville', 'RH')
Suppression (MonDico, 'name')
print (MonDico)

