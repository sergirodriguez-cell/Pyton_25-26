#P004_RO025_Paritemetrica_03.py
#Exercici mates 15

""" Comentari llarg (3 cometes) """

a1 = -203
an = 902.5
d = 16.5

n = ((an - a1)/d) + 1
print("n = ",n)
print() #Per deixar un espai entre linia i linia

k = n

n = 1

s = 0

print ("n		a		s		\n")

while n < k + 1:
    
    a = a1 + (n - 1) * d
    
    s = a + s

    print(n, "	",a,"		",		s)
    #print (s, end = "	")
    n = n + 1



