#funcion Range():

lista_numeros = list(range(5))
print(lista_numeros)

lista_numeros_2 = list(range(0, 15, 3)) #range(x(INICIO), y(FINAL), z(SALTO))
print(lista_numeros_2)

#------------------------------------------

for numero in range(5):
    print(numero)
print("FIN")
print("----------------------------------------------------------")

for i in range(5, -5, -2):
    print(i)
print("FIN")
print("----------------------------------------------------------")

#For en decremento
my_list = [1,2,3,4,5]
lengt = len(my_list)
for i in range(lengt):
    index = lengt - i - 1
    print(my_list[index])
print("FIN")
print("----------------------------------------------------------")

#Break
for num in range(5):
    print(num)
    if (num == 3):
        break
print("FIN")
print("----------------------------------------------------------")

#continue
for numer in range(6):
    if (numer == 4):
        continue
    print(numer)
print("FIN")
print("----------------------------------------------------------")

#Aninado Independiente
for e in [0,1,2]:
    for j in [0, 1]:
        print(f"e vale {e} y j vale {j}")
print("----------------------------------------------------------")

#Aninado con funciion range()

for q in range(4):
    for l in range(3):
        print(f"q vale {q} y l vale {l}")

#Aninado combinaciones

for w in [1 ,2, 3]:
    for o in [11, 12]:
        print(o, end=" ")
        print(w, end=" ")
print("--------------------")
for t in [1 ,2, 3]:
    for m in [11, 12]:
        print(m, end=" ")
print(t, end=" ")
print("--------------------")

for p in [1 ,2, 3]:
    for n in [11, 12]:
        print(n, end=" ")
    print(p, end=" ")