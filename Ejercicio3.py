print("=====================================================")
print("Programa para comprobar que numero es mayor")
print("=====================================================\n")
num_uno= int(input("Ingrese el primer numero a comprobar: "))
num_dos= int(input("Ingrese el segundo numero a comprobar: "))
num_tres= int(input("Ingrese el tercer numero a comprobar: "))
if num_uno>num_dos and num_uno>num_tres:
    print("El numero", num_uno, "es el mayor de los tres")
else:
    if num_dos>num_uno and num_dos>num_tres:
        print("El numero", num_dos, "es el mayor de los tres")
    else:
        print("El numero", num_tres, "es el mayor de los tres")
