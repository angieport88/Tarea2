import random

#1
numero_secreto = random.randint(1, 20)  

#2: 
intentos = 0

#3: 
print("¡Bienvenido al juego de adivinanzas, creado por Angie Estrada!")


while True:

    intentos += 1

    #4
    try:
        numero_usuario = int(input("Ingresa un número: "))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        continue

    
    if numero_usuario == numero_secreto:
        print(f"¡Felicitaciones! Adivinaste el número en {intentos} intentos.")
        break 


    elif numero_usuario > numero_secreto:
        print("El número es demasiado alto. Intenta nuevamente.")
    else:
        print("El número es demasiado bajo. Intenta nuevamente.")

#5
print(f"¡Gracias por jugar! El número secreto era: {numero_secreto}.")
