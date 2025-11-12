#P021_RO044_exemple3.py

a = int(input("A = "))
b= int(input("B = "))
c = int(input("C = "))
    
r = 0
n = 10
i = 1

while ((a >= b) and (c <= 0)) and (i <= n):
    print("i = ", i, end = " ")
    if b % 2 != 0:
        r = r + c
        #print("r = ",r)
    b = b - 1
    print("b = ",b, "r = ",r)
    
    i = i + 1
    
print("r = ", r)

