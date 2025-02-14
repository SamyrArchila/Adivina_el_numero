import random

maq = random.randint(1, 100)
i = 1
print("---------------------------------------------")
print("¡Bienvenido al juego de adivinar el número!")
print("Estoy pensando en un número entre 1 y 100.")
print("---------------------------------------------")
while True:

    n = int(input("Introduce un numero: "))


    if n != maq:
        if n < maq:
            print("El valor es mayor al elegido.")
        else:
            print("El valor es menor al elegido.")
        i += 1
    else:
        print(f"¡Felicidades! Adivinaste el número en {i} intentos.")
        break