import sys
import gc

a = "Hello World!"
#Affiche le nombre de références vers la variable a
print(sys.getrefcount(a))

ma_liste = []
ma_liste.append(a)
#Affiche le nombre de références vers la variable a
print(sys.getrefcount(a))
#Affiche les éléments qui font référence à la variable a
print(gc.get_referrers(a))
#Affiche les cycle de génération du garbage collector
print(gc.get_threshold())
#Modifie les cycles de générations
gc.set_threshold(1000, 20, 30)
#Affiche les cylce de génération du garbage collector
print(gc.get_threshold())
#Affiche les cycles actuels
print(gc.get_count())
#désactive le garbage collector
gc.disable()
#active le garbage collector
gc.enable()
# Le garbage collector est lié au script



# Script à utliser à part pour "jouer" !

import gc
import sys
import time

# gc.set_debug(True)
# gc.set_threshold(20000, 50, 100)
gc.disable()

class lien:

    def __init__(self, prochain_lien, valeur):
        self.prochain_lien = prochain_lien
        self.valeur = valeur

    def __repr__(self):
        return self.valeur


l = lien(None, "Lien Principal")

ma_liste = []

start = time.perf_counter()
for i in range(5000000):
    l_temp = lien(l, i)
    ma_liste.append(l_temp)
end = time.perf_counter()
print(end-start)