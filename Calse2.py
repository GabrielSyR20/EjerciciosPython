edad = 0
nombre = "patricio"

edad = int(input("Ingrese su edad: "))

print(f"Hola {nombre}, tienes {edad} años")

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
print("---------------------------------------------------------")

mascotas = ["perro", "gato", "loro"]
print(mascotas[0])
print(mascotas[1]) 
print(mascotas[2])
if "perro" in mascotas:
    print("El perro es una mascota")
else:
        print("El perro no es una mascota")
print("---------------------------------------------------------")

hijos = int(input("Cuantos hijos tienes?: "))
if hijos == 0:
    print("No tengo hijos")
else:
    print(f"Tengo {hijos} hijos")
     