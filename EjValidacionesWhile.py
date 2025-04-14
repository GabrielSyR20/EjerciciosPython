#Claves
clave = input("Ingrese su clave: ")
clave = int(clave)

while clave != 234:
    clave = input("ERROR. Ingrese su clave nuevamente: ")
    clave = int(clave)
    
print("ingresaste bien la clave")

#Rango
nota = input("Ingrese la nota: ")
nota = int(nota)

while nota < 1 or nota > 10:
    nota = input("Ingrese nuevamente la nota: ")
    nota = int(nota)

#conjunto de valores

color = input("Ingrese el color: ").lower()

while color != "azul" and color != "rojo" and color != "amarillo":
    color = input("Ingrese nuevamente el color: ")

#Break

contador = 0
while True:
    if contador >= 5:
        break
    contador += 1
    print(contador)
