#P006_RO28_condicio.py

n = int(input("Quantitat de llantes: "))

p = int(input("Preu inicial de la llanata: "))

if n >=4:
    t = p*0.9*n
    print(t)
else:
   t =  p*n
   print(t)
