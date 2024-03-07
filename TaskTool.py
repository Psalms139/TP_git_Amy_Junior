def AjouterValeur  (dico, cle, valeur) : 
	dico[cle] = valeur 


MonDico = {'name' : "John", 'age' : "31"} 

AjouterValeur(MonDico, 'ville', 'RH')
del MonDico ['name']
print (MonDico)
