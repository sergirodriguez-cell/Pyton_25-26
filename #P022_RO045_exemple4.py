#P022_RO045_exemple4.py

a = int(input("A = "))
b= int(input("B = "))

x = 0

if a<5:
    x = x+(a-b)
else:
    control = True
    while control == True:
        x = x+a
        print("X = " , x)
        control = False
print("X = " , x)


