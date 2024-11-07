# Ejercicio 3: Calculadora
import math

def calculadora(operacion, a, b=None):
    match operacion:
        case "suma":
            return a + b
        case "resta":
            return a - b
        case "multiplicacion":
            return a * b
        case "division":
            if b == 0:
                return "Error: División entre cero"
            return a / b
        case "potencia":
            return a ** b
        case "raiz":
            if a < 0:
                return "Error: Raíz de número negativo"
            return math.sqrt(a)
        case "seno":
            return math.sin(math.radians(a))
        case "coseno":
            return math.cos(math.radians(a))

def menu():
    print("Operación a realizar (Seleccione con el número correspondiente):")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Potencia")
    print("6. Raíz cuadrada")
    print("7. Seno")
    print("8. Coseno")
    
    opcion = input("Ingrese el número de la operación: ")

    if opcion in ["1", "2", "3", "4", "5"]:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        
        operacion = {
            "1": "suma",
            "2": "resta",
            "3": "multiplicacion",
            "4": "division",
            "5": "potencia"
        }[opcion]

        resultado = calculadora(operacion, a, b)
        print(f"Resultado: {resultado:.2f}")

    elif opcion in ["6", "7", "8"]:
        a = float(input("Ingrese el número: "))

        operacion = {
            "6": "raiz",
            "7": "seno",
            "8": "coseno"
        }[opcion]

        resultado = calculadora(operacion, a)
        print(f"Resultado: {resultado:.2f}")

    else:
        print("Opción no válida.")

# Ejecutar el menú
menu()


