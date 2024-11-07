# Ejercicio 10: Clasificación de notas
nota = float(input("Ingrese la nota: "))

if 90 <= nota <= 100:
    print("Clasificación: A")
elif 80 <= nota <= 89:
    print("Clasificación: B")
elif 70 <= nota <= 79:
    print("Clasificación: C")
elif 60 <= nota <= 69:
    print("Clasificación: D")
elif 0 <= nota < 60:
    print("Clasificación: F")
else:
    print("Nota no válida.")



