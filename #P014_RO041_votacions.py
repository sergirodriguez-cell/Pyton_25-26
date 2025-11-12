#P014_RO041_votacions.py

n = 0

print ("Vot a favor (0): ")
print ("Vot en contra (1): ")
n = int(input("Num. persones: "))
i =1
vott = 0
while i <=n:
    i= i+1
    vot = int(input("A qui votes? "))
    vott = vott + vot
vot0 = n - vott
vot1 = n - vot0
print ("vot0", vot0)
print ("vot1", vot1)


