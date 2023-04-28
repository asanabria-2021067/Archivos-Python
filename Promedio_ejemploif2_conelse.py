nombre= input("Cual es tu nombre: ")
calificacion_mate= float(input(nombre + " Ingresa tu calificacion de matematicas: "))
calificacion_fisica= float(input(nombre + " Ingresa tu calificacion de fisica: "))
calificacion_quimica= float(input(nombre + " Ingresa tu calificacion de quimica: "))
promedio= (calificacion_mate + calificacion_fisica + calificacion_quimica)/3

if promedio >= 6:
    print("Felicidades", nombre, "aprobaste el año con un promedio de: " ,round(promedio,2))
else:
    print("Lo sentimos", nombre,  "no aprobaste el año, tu promedio fue de: ",round(promedio,3))
