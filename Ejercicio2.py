print("=====================================================")
print("Programa para comprobar si un numero es par o impar")
print("=====================================================\n")
numero=int(input("Ingrese el numero que desea comprobar: "))
if numero % 2== 0:
    print("El numero", numero, "es par")
elif numero % 2== 1:
    print("El numero", numero, "es impar")
