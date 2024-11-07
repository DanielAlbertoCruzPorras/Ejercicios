# Ejercicio 5: Días de la semana
dia = int(input("Ingrese el número del día de la semana: "))

hoy = {
    1: "Lunes",
    2: "Martes",
    3: "Miércoles",
    4: "Jueves",
    5: "Viernes",
    6: "Sábado",
    7: "Domingo"
}

if dia in hoy:
    print(f"{hoy[dia]}")
else:
    print("Número de día no válido, debe ser un entero del 1 al 7.")

