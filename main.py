"""
Programa simulador de ATM  con un saldo inicial de $5500

1.Ingrese el dinero en la cuenta
2. Retirar dinero de la cuenta
3. Mostrar dinero disponible
4. Salir
"""

print("\t. <<<<<<<<<<<<< ATM >>>>>>>>>>>:")
print("1. Ingresar dinero en la cuenta")
print("2. Retirar dinero de la cuenta")
print("3. Mostrar dinero disponible")
print("4. Salir")

opcion = int(input("Ingrese una opción: "))

print()
sal = 5500
total = 0

if opcion == 1:
    depClien = float(input("Cuánto dinero desea ingresar -> "))
    total = sal + depClien
    print(f"Dinero en la cuenta es de: {total}")


elif opcion == 2:
    retClien = float(input("Cuánto dinero desea retirar ->  "))
    if retClien > sal:
        print("No tienes saldo suficiente...")
    else:
        total = sal - retClien
        print(f"Su Dinero en la cuenta es de: {total}")
elif opcion == 3:
    print(f"Su Dinero en la cuenta es de: {sal}")
elif opcion == 4:
    print("Gracias por utilizar el ATM")
else:
    print("Error, se equivocó de opción de menú")
