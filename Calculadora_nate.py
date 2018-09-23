seleccion = input("¿que operacion quieres hacer (SUMAR / RESTAR / MULTIPLICAR / DIVIDIR): ").upper()



numero_uno = float(input("dime el primer numero a operar: "))
numero_dos = float(input("dime el segundo numero a operar: "))

sum = numero_uno + numero_dos
res = numero_uno - numero_dos
mul = numero_uno * numero_dos
div = numero_uno / numero_dos

if seleccion == "SUMAR":
    print("el resultado es:{}".format(sum))

elif seleccion == "RESTAR":
    print("el resultado es:{}".format(res))

elif seleccion == "MULTIPLICAR":
    print("el resultado es:{}".format(mul))

elif seleccion == "DIVIDIR":
    print("el resultado es: ".format(div))



