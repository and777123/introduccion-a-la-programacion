#proyecto
#hacer un test, un cuestionario que guarde las respuestas y al funal, le de un puntaje al usiario.
#tema abierto
#al menos 7 preguntas
#al final, debe decir cuantas se contestaron bien 
#debe pedirle el nombre al usuario
#preguntas de multiples opciones 

#TEMA: ccomo se usa una camara?
nombre = input("ingrese su nombre: ")
if nombre == " ":
    print("ingrese un nombre valido")
else:
    print("bienvenido al test de camaras", nombre)
input("presione enter para continuar")

res1 = "b"  
print("cual es la piesa ma importante de una camara?") 
print("a) el lente")
print("b) el sensor")   
print("c) el flash")
print("d) el visor")

res1 = input("ingrese su respuesta: ")

if res1 == "b":
    print("correcto")
else:
    print("incorrecto")

input ("presione enter para continuar")

res2 = "a"

print("cual es la funcion del sensor?")
print("a) capturar la luz")
print("b) almacenar la imagen")
print("c) enfocar la imagen")
print("d) iluminar la escena")

res2 = input("ingrese su respuesta: ")

if res2 == "a":
    print("correcto")
else:
    print("incorrecto")

input ("presione enter para continuar")

res3 = "c"
print("para que sirve el visor de una camara?")
print("a) para almacenar la imagen")
print("b) para iluminar la escena")
print("c) para ver la imagen antes de tomarla")
print("d) para capturar la luz")

res3 = input("ingrese su respuesta: ")

if res3 == "c":
    print("correcto")
else:
    print("incorrecto")

input("presione enter para continuar")

res4 = "d"
print("para que se usa el triangulo de exposicion")
print("a) para enfocar la imagen")
print("b) para capturar la luz")
print("c) para almacenar la imagen")
print("d) para controlar la exposicion de la imagen")

res4 = input("ingrese su respuesta: ")
if res4 == "d":
    print("correcto")       
else:
    print("incorrecto")

input("presione enter para continuar")

res5 = "a"
print("que es el ISO en una camara?")
print("a) la sensibilidad del sensor a la luz")
print("b) la cantidad de luz que entra al lente")
print("c) la velocidad de obturacion")
print("d) la distancia focal del lente")

res5 = input("ingrese su respuesta: ")
if res5 == "a":
    print("correcto")
else:
    print("incorrecto")

input("presione enter para continuar")

res6 = "b"
print("que es la velocidad de obturacion?")
print("a) la cantidad de luz que entra al lente")
print("b) el tiempo que el sensor esta expuesto a la luz")
print("c) la sensibilidad del sensor a la luz")
print("d) la distancia focal del lente")

res6 = input("ingrese su respuesta: ")
if res6 == "b":
    print("correcto")
else:
    print("incorrecto")

input("presione enter para continuar")

res7 = "c"
print("que es la distancia focal de un lente?")
print("a) la cantidad de luz que entra al lente")
print("b) la sensibilidad del sensor a la luz")
print("c) la distancia entre el lente y el sensor")
print("d) el tiempo que el sensor esta expuesto a la luz")

res7 = input("ingrese su respuesta: ")
if res7 == "c":
    print("correcto")
else:
    print("incorrecto")

input("presione enter para ver puntuacion final")

if res1 == "correcta":
    puntaje1 = 1
else:
    puntaje0 = 0


for i in [res2, res3, res4, res5, res6, res7]:
    if i == "correcta":
        puntaje1 += 1
else:
        puntaje0 += 0
while True:
    if res1 == "b":
        puntaje1 = 1
    else:
        puntaje0 = 0

    if res2 == "a":
        puntaje1 += 1
    else:
        puntaje0 += 0

    if res3 == "c":
        puntaje1 += 1
    else:
        puntaje0 += 0

    if res4 == "d":
        puntaje1 += 1
    else:
        puntaje0 += 0

    if res5 == "a":
        puntaje1 += 1
    else:
        puntaje0 += 0

    if res6 == "b":
        puntaje1 += 1
    else:
        puntaje0 += 0

    if res7 == "c":
        puntaje1 += 1
    else:
        puntaje0 += 0
    break

print("su puntaje final es: ", puntaje1 + puntaje0, "de 7")   
