# Ejercicio 6: Juego adivinanza
import random

numero_aleatorio = random.randint(1, 10)

while True:
    intento = int(input("Adivina el número entre 1 y 10: "))

    if intento < numero_aleatorio:
        print("El número es mayor.")
    elif intento > numero_aleatorio:
        print("El número es menor.")
    else:
        print("¡Correcto! Has adivinado el número.")
        break
