#P010_RO32_conversio_temperatura.py
while True:
    p = int(input("Celsius a Farenheit (1) o Farenheit a Celsius (2)"))
    t = int(input("Temperatura: "))

    c = 5/9*(t-32)
    f = 32 + (9*t/5)

    if p == 1:
        print(c)
        
    else:
        print(f)


