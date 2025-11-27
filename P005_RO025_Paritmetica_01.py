#P005_RO0025_Paritmetrica_01.py
#Exercici 1 llibre mates

a1 = 13
t = 0
n= 11
d = 2
an = 0

while t < n:
        an = a1 +  (t-1) * d
        print ("a",t,"= ", round(an,2),"       ", end = "")
        t = t+1
print("a",t-1,"= ",round(an,2),"        ") 
