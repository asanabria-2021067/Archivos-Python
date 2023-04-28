numero1 = float(input("Introduce tu primer número: ") )
numero2 = float(input("Introduce tu segundo número: ") )

opcion = 0
print("""
    Dime, ¿qué quieres hacer?
    
    1) Sumar los dos números
    2) Restar los dos números
    3) Multiplicar los dos números
    4) Dividir los dos numeros
    """)
opcion = int(input("Elige una opción: ") )     

if opcion == 1:
        print(" ")
        print("RESULTADO: La suma de",numero1,"+",numero2,"es igual a",numero1+numero2)
elif opcion == 2:
        print(" ")
        print("RESULTADO: La resta de",numero1,"-",numero2,"es igual a",numero1-numero2)
elif opcion == 3:
        print(" ")
        print("RESULTADO: El producto de",numero1,"*",numero2,"es igual a",numero1*numero2)
elif opcion == 4:
        print(" ")
        print("RESULTADO: La division de", numero1, "/" ,numero2, "es igual a", numero1/numero2)    
else:
        print("Opción incorrecta")
