#P003_RO041_Fibonacci.py

terme_anterior = 0
terme_actual = 1

for i in range(2,20):
    print(terme_actual, end = "  ")
    terme_seguent = terme_anterior + terme_actual
    terme_anterior = terme_actual
    terme_actual = terme_seguent


