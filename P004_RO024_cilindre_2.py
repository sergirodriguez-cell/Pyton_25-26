#Cilindre_2
#Fórmula cilindre: (sqrt(volum/(h*pi))*2

from math import sqrt

print ("Càlcul del diametre d'un cilindre:")

pi = 3.14159

v = float(input("Volum del cilindre en dm3: "))
h = float(input("Alçada del cilindre en m: "))

v = v/1000

d = (sqrt(v/(h*pi)))*2

print ("El diàmetre és: ", d ,"m")

