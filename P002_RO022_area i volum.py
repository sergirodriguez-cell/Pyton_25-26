# P002_RO022_area i volum.py

# V = pi*r^2*h
# A = 2(pi*r^2) + 2*pi*r

a = int(input("Radi: "))

b = int(input("Altura: "))

volum = (3.1415 * (a*a * b))

print("Volum: ",volum)

area = (2*(3.1415*a*a) + 2*3.1415*a)

print("Area: ",area)
