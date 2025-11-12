#P004_RO025_Paritemetrica_04.py
#Exercici mates global

print ("Menú Progressió aritmètica")
print ("================== \n")
print ("Prem l'opció de càlcul:		\n")
print ("Opció 1 : darrer terme an	")
print ("Opció 2 : darrer terme an	")
print ("Opció 3 : numero de termes n	")
print ("Opció 4 : diferència o  raó d	")
opcio = int(input("Prem l'opció entre 1 i 4 "))

#-----------------------------------------------------------

if opcio == 1:
    a1 = eval(input("a1 = "))
    n = int(input("n = "))
    d = eval(input("d = "))

    interacions = n
    n = 1
    while n <= interacions:
        an = a1 + (n - 1) * d
        print(round(an,2),end = "	")
        n = n + 1

if opcio == 2:
    pass
    an = eval(input("an = "))
    n = int(input("n = "))
    d = eval(input("d = "))

    interacions = n
    n = 1
    while n <= interacions:
        a1 = an - (n - 1) * d
        print(round(a1,2),end = "	")
        n = n + 1
            
if opcio == 3:
    
    an = eval(input("an = "))
    a1 = eval(input("n = "))
    d = eval(input("d = "))
                
    n = ((an - a1)/d)  + 1

    if n == int(n):
        print()
            
if opcio == 4:
            pass


