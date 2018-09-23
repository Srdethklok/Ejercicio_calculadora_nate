numero_a_adivinar = int(input("Dime el numero a adivinar: "))


numero_del_usuario = int(input("Prueba un numero: "))



while numero_del_usuario != numero_a_adivinar:


    if numero_del_usuario == numero_a_adivinar:
        print("You win")

    elif numero_del_usuario < numero_a_adivinar:
         print("El numero a adivinar es mayor")

    else:
         print("El numero es menor")

    numero_del_usuario = int(input("Prueba un numero: "))

print("you win")