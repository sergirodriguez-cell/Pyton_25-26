#P020_RO042_exemple2.py

a = int(input("A = "))
b= int(input("B = "))
c = int(input("C = "))
t =  0

if (a<b) or (c <= b):
    t = a+b

else:
    t = b-c

print("A=" , a , "T=" , t)
print("B=" , b , "T=" , t)
    