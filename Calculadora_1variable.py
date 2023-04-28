print("===================================")
print("            Calculadora            ")
print("===================================\n")
print("""       Menu de Operaciones:
         1. Suma
         2. Resta
         3. Multiplicacion
         4. Division
         5. Modulo
         6. Exponente
         7. Division Entera \n""")
numero= int(input("Ingrese el numero de la operacion que desea: "))
if numero==1:
    print("La opcion elegida fue suma")
    numero=int(input("Ingrese el primer valor a operar: "))
    numero+=int(input("Ingrese el segundo valor a operar: "))
    print("El resultado de la suma es: ", numero)
    
elif numero==2:
    print("La opcion elegida fue resta")
    numero=int(input("Ingrese el primer valor a operar: "))
    numero-=int(input("Ingrese el segundo valor a operar: "))
    print("El resultado de la resta es: ", numero)
    
elif numero==3:
    print("La opcion elegida fue Multiplicacion")
    numero=int(input("Ingrese el primer valor a operar: "))
    numero*=int(input("Ingrese el segundo valor a operar: "))
    print("El resultado de la multiplicacion es: ", numero)
    
elif numero==4:
    print("La opcion elegida fue division")
    numero=int(input("Ingrese el primer valor a operar: "))
    numero/=int(input("Ingrese el segundo valor a operar: "))
    print("El resultado de la division es: ", numero)
    
elif numero==5:
    print("La opcion elegida fue modulo")
    numero=int(input("Ingrese el primer valor a operar: "))
    numero%=int(input("Ingrese el segundo valor a operar: "))
    print("El resultado del modulo es: ", numero)
    
elif numero==6:
    print("La opcion elegida fue exponente")
    numero=int(input("Ingrese el primer valor a operar: "))
    numero**=int(input("Ingrese el segundo valor a operar: "))
    print("El resultado del exponente es: ", numero)
    
elif numero==7:
    print("La opcion elegida fue division entera")
    numero=int(input("Ingrese el primer valor a operar: "))
    numero//=int(input("Ingrese el segundo valor a operar: "))
    print("El resultado de la division es: ", numero)
else:
    print("La opcion elegida no esta registrada en la base")
    
