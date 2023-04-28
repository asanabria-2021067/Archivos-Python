print("Introduce los numeros a comparar")
num_uno=int(input("Introduce el primer numero a comparar: "))
num_dos=int(input("Introduce el segundo numero a comparar: "))
print("Los numeros a comparar son:", num_uno, "y el numero", num_dos)
if num_uno==num_dos:
    print("Los numeros son iguales")
if num_uno!=num_dos:
    print("Los numeros no son iguales")
if num_uno<num_dos:
    print("El numero", num_uno, "es menor que el numero", num_dos)
if num_uno>num_dos:
    print("El numero", num_uno, "es mayor que el numero", num_dos)
if num_uno<=num_dos:
    print("El numero", num_uno, "es menor o igual que el numero", num_dos)
if num_uno>=num_dos:
    print("El numero", num_uno, "es mayor o igual que el numero", num_dos)

