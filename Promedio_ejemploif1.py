nombre= input("Cual es tu nombre: ")
calificacion_mate= int(input(nombre + " Ingresa tu calificacion de matematicas: "))
calificacion_fisica= int(input(nombre + " Ingresa tu calificacion de fisica: "))
calificacion_quimica= int(input(nombre + " Ingresa tu calificacion de quimica: "))
promedio= (calificacion_mate + calificacion_fisica + calificacion_quimica)/3

if promedio >= 6:
    print("Felicidades", nombre, "aprobaste el año con un promedio de: " ,str(promedio))

