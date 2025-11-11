def sumar():
    num1 = float(input("Ingresa el primer numero: "))
    num2 = float(input("Ingresa el segundo numero: "))

    resultado = num1 + num2
    print(f"El resultado es: {resultado}")

def restar():
    num1 = float(input("Ingresa el primer numero: "))
    num2 = float(input("Ingresa el segundo numero: "))

    resultado = num1 - num2
    print(f"El resultado es: {resultado}")


def multiplicar():
    num1 = float(input("Ingresa el primer numero: "))
    num2 = float(input("Ingresa el segundo numero: "))

    resultado = num1 * num2
    print(f"El resultado es: {resultado}")

def division():
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    if num2 == 0:
        print("No se puede dividir por 0")
    else:
        resultado = num1 / num2
        print(f"El resultado es: {resultado}")


print("CALCULADORA\n 1. suma\n 2. resta\n 3.multiplicacion\n 4.division\n 5. salir")

while True:

    try:
        opcion = int(input("Ingresa una opcion: "))
    except ValueError:
        print("Ingrese una opcion valida")
        continue

    if opcion == 1:
        sumar()
    elif opcion == 2:
        restar()
    elif opcion == 3:
        multiplicar()
    elif opcion == 4:
        division()
    elif opcion == 5:
        print("Saliendo")
        exit()
    else:
        break
