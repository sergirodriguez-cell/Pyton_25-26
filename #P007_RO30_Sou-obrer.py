#P007_RO30_Sou-obrer.py

hores = float(input("Hores: "))
preu_hores = float(input("Preu l'hora: "))
reduccions = 2

if hores <= 40:
    s = hores*preu_hores
    print("El teu sou: " , s , "€")
    
else:
    s = hores*preu_hores
    preu = 40*preu_hores+hores-40*2
    print("El teu sou amb reduccions: " , s + (preu))
    
