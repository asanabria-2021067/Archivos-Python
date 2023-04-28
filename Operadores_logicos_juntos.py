#Conjución

print("Conjunción (and)")

num_uno = int(input("Escribe un número mayor a 2 y menor a 5: "))

if num_uno > 2 and num_uno < 5:
    print("El número ", num_uno, " cumple con la condición")
else:
    print("El número ", num_uno, " NO cumple con la condición")


#Disyunción
print("Disyunción (or)")

palabra = input("Para cumplir con la condición escribe 'si' o 'yes':")

if palabra == "si" or palabra == "yes":
    print("La condición se ha cumplido.")
else:
    print("La condición no se ha cumplido.")


#Negación
print("Negación (not)")

num_uno = int(input("Introduce un número distinto a 5: "))

if not num_uno == 5:
    print("El número es diferente de cinco y si cumple la condición.")
else:
    print("El número es igual a cinco y no cumple la condición.")
