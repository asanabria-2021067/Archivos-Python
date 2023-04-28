print("===========================================================")
print("CONVERSOR")
print("===========================================================")
print("Menu de operaciones:")
print("1. Convertir letras a numeros")
print("2. Convertir numeros a letras")
opcion= int(input("¿Cual es la opcion deseada?: "))
if opcion==1:
    print("Bienvenido a Convertidor de letras a numeros")
    letra=input("Ingrese el numero en letras: ")
    letra= letra.lower()
    if letra=="uno":
        print("El numero es 1")
    elif letra=="dos":
        print("El numero es 2")
    elif letra=="tres":
        print("El numero es 3")
    else:
        print("El numero ingresado no esta ingresado en la base")
else:
    print("Bienvenido a Convertidor de numeros a letras")
    print("======================================")
    numero= int(input("Ingrese el numero que desea convertir: "))
    if numero==1:
        print("El numero es uno")
    elif numero==2:
        print("El numero es dos")
    elif numero==3:
        print("El numero es tres")
    else:
        print("El numero ingresado no esta ingresado en la base")
print("======================================")
print("Fin del programa")
