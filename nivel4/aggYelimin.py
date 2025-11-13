frutas = ["Apple","Orange","Strawberry"]

while True:
    try:
        print("LISTA DE FRUTAS\n 1. para agregar\n 2. para eliminar\n 3. para salir")
        opcion = int(input("digita la opcion: "))
    except ValueError:
        print("\nERROR: ingresa un numero")
        continue

    if opcion == 1:
        frutNuev = input("Ingresa una fruta: ")
        frutas.append(frutNuev.title())
        print(frutas)
    elif opcion == 2:
        print(frutas)
        elimFruta = input("digita la fruta que desea eliminar: ")
        frutas.remove(elimFruta.title())
        print(frutas)
    else:
        print("saliendo")
        break


