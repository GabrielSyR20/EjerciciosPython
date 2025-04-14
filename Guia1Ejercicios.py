import random
jugador_altura = input("Ingresar su altura: ")
jugador_altura = int(jugador_altura)

if (jugador_altura < 160):
    print("Jugador juega en BASE")

elif (jugador_altura >= 160 and jugador_altura < 179):
    print("Jugador juega en ESCOLTA")
elif(jugador_altura >= 180 and jugador_altura < 199):
    print("Jugador juega en ALERO")
else:
    print("Jugador juega en PIVOT")

calculate_nota = random.randint(1, 10)
print("Nota: " + str(calculate_nota))

if  (calculate_nota <= 3):
    print("DESAPROBADO")
elif (calculate_nota > 3 and calculate_nota <= 5):
    print("APROBADO")
else:
    print("APROBACION DIRECTA")
    
print("---------------------------------------------------------")
rep = 0
while True:
    rep += 1
    if  rep > 10:
        break
    print(rep)
print("---------------------------------------------------------")

repo = 10
while repo > 0:
    print(repo)
    repo -= 1
print("---------------------------------------------------------")

suma = 0
num = 1
while num <= 10:
    if  num % 2 == 0:
        suma += num
    num += 1
print("la suma de los numeros pares del 1 al 10 es:", suma)
print("---------------------------------------------------------")

sum_num = 0
rep = 0
while rep < 5:
    ingresed = input("Ingresar numero: ")
    ingresed = int(ingresed)
    sum_num += ingresed
    rep += 1

'''for i in range(5):
    ingresed = input("Ingresar numero: ")
    ingresed = int(ingresed)
    sum_num += ingresed
    
promedio = sum_num / i'''
promedio = sum_num / rep
print(f"la suma de los numeros es de {sum_num} y el promedio de: {promedio}")
print("---------------------------------------------------------")

cont_numNegative = 1
cont_numPositive = 0
print("ingresar 0 para dejar de ingresar numeros")
while True:
    ingresed = input("Ingresar numero: ")
    ingresed = int(ingresed)
    if ingresed == 0:
        break
    elif ingresed > 0:
        cont_numPositive += ingresed
        print(cont_numPositive)
    else:
        cont_numNegative *= ingresed
        print(cont_numNegative)

print(f"La suma de los numeros positivos es de {cont_numPositive} y el producto de los numeros negativos es de: {cont_numNegative}")
print("---------------------------------------------------------")
maximo = None
minimo = None

for i in range(10):
    numero = int(input(f"Ingresa el numero {i+1}: "))

    if  maximo is None or numero > maximo:
        maximo = numero
    if minimo is None or numero < minimo:
        minimo = numero

print("El numero maximo es:", maximo)
print("El numero minimo es:", minimo)