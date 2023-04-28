#Ejercicio de empresa de vacaciones con 3 departamentos
print("=====================================")
print("  Sistema de control de vacaciones  ")
print("=====================================\n")
nombre= input("Ingresa tu nombre: ")
print("Hola",nombre,"a continuacion se encuentra el listado de departamentos")
print("""\n Los departamentos son los siguientes:
          Clave         Departamento
            1. Departamento de atencion al cliente
            2. Departamento de logistica
            3. Gerencia \n""")
num_departamento=int(input("Ingresa aqui el numero del departamento al que perteneces: "))
num_año=int(input("Ingresa el numero de años de servicio que llevas trabajando en el departamento: "))

if num_departamento==1:
              
    print("\nBienvenido al departamento de atencion al cliente")
    if num_año==1 and num_año<2:
        print("El/La emplead@",nombre, "recibira 6 dias de vacaciones")
    elif num_año>=2 and num_año<=6:
        print("El/La emplead@",nombre, "recibira 14 dias de vacaciones")
    elif num_año>=7:
        print("El/La emplead@",nombre, "recibira 20 dias de vacaciones")
    else:
        print("El/La emplead@", nombre, "aun no tiene derecho de vacaciones")

elif num_departamento==2:
    
    print("\nBienvenido al departamento de logistica")
    if num_año==1 and num_año<2:
        print("El/La emplead@",nombre, "recibira 6 dias de vacaciones")
    elif num_año>=2 and num_año<=6:
        print("El/La emplead@",nombre, "recibira 15 dias de vacaciones")
    elif num_año>=7:
        print("El/La emplead@",nombre, "recibira 22 dias de vacaciones")
    else:
        print("El empleado", nombre, "aun no tiene derecho de vacaciones")

elif num_departamento==3:
    
    print("\nBienvenido al departamento de gerencia")
    if num_año==1 and num_año<2:
        print("El/La emplead@",nombre, "recibira 10 dias de vacaciones")
    elif num_año>=2 and num_año<=6:
        print("El/La emplead@",nombre, "recibira 20 dias de vacaciones")
    elif num_año>=7:
        print("El/La emplead@",nombre, "recibira 30 dias de vacaciones")
    else:
        print("El/La emplead@", nombre, "aun no tiene derecho de vacaciones")
else:
    print("La clave de departamento ingresada no esta registrada en el sistema")
