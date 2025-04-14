#a = int(input("Coloca un numero A: "))
#b = int(input("Coloca un numero B: "))
#
#if b != 0 | a != 0:
    #division = a / b
    #print("El resultaod de la division es", division)
#else:
    #print("Mielda no se pudo hacer la division")
#
#print("Menu de opciones")
#print("[1] Ventas")
#print("[2] Soporte")
#print("[3] Administracion")
#opcion = int(input("Elegi opcion: "))
#
#match opcion:
    #case 1: print("Ventas")
    #case 2: print("Soporte")
    #case 3: print("Administracion")
    #case _: print("kakaaaaaa")

EDAD_MINIMA = 21
edad = int(input("Ingrese edad: "))
categoria = input("Ingrese su categoria (A, B, C, D): ")

if edad >= EDAD_MINIMA and (categoria == "D" or categoria == "d"):
    print("Puede conducir")
else:
    print("no puede conducir")