#P009_for_n_imparells

from math import *

n = int(input("Número d'imparells: "))
suma = 0

for i in  range(1,n+1):
    k = (2*i) - 1
    suma = suma + k
    print(suma)
print ("suma: " , suma)
if suma == pow(n,2):
    print("Verdader")
else:
    print("Fals")

