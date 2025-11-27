# P001_RO022_area triangle.py

from math import *

#a = 4
a = int(input("Valor d'a: "))
#b = 6
b = int(input("Valor de b: "))
#c = 7
c = int(input("Valor de c: "))

semiperimetre = (a + b + c)/2
t = semiperimetre
s = sqrt(t*(t-a)*(t-b)*(t-c))

print("t = ",t)
print("s = ",s)
#print(cos(s))
