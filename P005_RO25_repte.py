#P005_RO25_repte.py

e = 0.7
l = 0.2
t = 0.1

nota = int(input("Nota examen sobre 100: "))
leccion = float(input("Nota leccion sobre 10: "))
tarea1 = float(input("Nota tarea 1 sobre 10: "))
tarea2 = float(input("Nota tarea 2 sobre 10: "))
tarea3 = float(input("Nota tarea 3 sobre 10: "))


notaexamen  = (nota * e)/10

lecciones = (leccion * l)

tarea = ((tarea1 + tarea2 + tarea3) / 3)*t 

print("La teva nota és: " , (notaexamen + lecciones + tarea)*10)

