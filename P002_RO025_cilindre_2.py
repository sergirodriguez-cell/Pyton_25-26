# P002_RO025_area i volum cilindre.py

# V = pi*r^2*h
# A = 2(pi*r^2) + 2*pi*r

r = int(input("Radi (en cm): "))

a = int(input("Altura (en cm): "))

pi = 3.1416

#volum = (pi * r*r * v)

volum = pi * pow(r,2) * a

print("Volum: ",volum, "cm3")

area = ((2*pi*r*r) + (r*a))

print("Area: ",area, "cm2")
