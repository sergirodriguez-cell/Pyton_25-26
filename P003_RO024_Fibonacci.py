#P003_RO024_Fibonacci.py

anterior = 0

fib = 1

fib1 = 0

maxim = 100

a = 1
b = 0
c = 0

print("Sèrie de Fibionacci dels " , maxim , "primers nombres\n")

print(0, fib, end = "  ")

while a < maxim:
        c= b
        b = a
        a= b + c
        print (a, end = "  ")
