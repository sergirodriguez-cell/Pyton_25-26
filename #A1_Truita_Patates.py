#A1_Truita_Patates.py

num_persones = 4
num_ous = 0
num_patates = 0
num_cebes = 0

sal = False
ceba = True

num_patates = num_persones + 1
num_ous = num_persones +2

print("Començem a cuinar:")

print("Per una truita de", num_persones, ", nescessitem:")
print(" ", num_ous," ous")
print(" ", num_patates," patates")

if sal == True:
    print("  Sal")
    
if num_cebes ==True:
    print("  1 ceba.")
    
    
for i in range (num_patates-1):
    print(" -Pela la patata a daus.-", i+1)
    
print("En una paella aboca oli suficient per que cobreixin les patates.")
print("Aboca les patates a la paella quan l'oli estigui calent.")

print("Mentre cuinem les patates, trenca i bat els ous")

for i in range (num_ous-1):
    print(" -Trenca els ous.-", i+1)
    
if sal ==True:
    print("Afegeix sal als ous.")
    
print("Batre els ous.")
print("Quan les patates estiguin llestes, treu-les i escorre l'oli")

if num_cebes == True:
    print("Talla la ceba. Fregeix-la i quan estigui daurada afegeix-la a la barreja.")
    
print("Aboca la barreja a la paella.")
print("- Cuina durant 5 minuts.")
print("- Amb compte, gira-la. ")
print("- Cuina durant 5 minuts més.")

print("La teva truita ja està per menjar")
