# P002_RO022_area i volum cilindre.py

# V = pi*r^2*h
# A = 2(pi*r^2) + 2*pi*r

a = int(input("Radi (en cm): "))

b = int(input("Altura (en cm): "))

pi = 3.1416

volum = (pi * (a*a * b))

print("Volum: ",volum, "cm^3")

area = (2*(pi*a*a) + 2*pi*a)

print("Area: ",area, "cm^2")
