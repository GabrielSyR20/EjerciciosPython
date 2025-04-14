'''
nombre_alumno = input("Nombre: ")
comision_alumno = str(input("Comision: "))
asignatura_alumno = input("Asignatura: ")
docente_alumno = input("Docente: ")
asistencia_alumno = input("¿Presenció la clase de hoy? (Si/No): ")
'''
#print("Alumno: "+ nombre_alumno, "Comision: "+comision_alumno, "Asignatura: "+ asignatura_alumno, "Docente: "+ docente_alumno, "Asistencia: "+ asistencia_alumno, sep="\n")

'''nombre_alumno_1 = input("Nombre: ")
apellido_alumnno_1 = input("Apellido: ")
nota_1= int(input("Nota 1er trimestre: "))
nota_2= int(input("Nota 2do trimestre: "))
nota_3= int(input("Nota 3er trimestre: "))
Promedio_Nota = (nota_1 + nota_2 + nota_3) / 3

print("Nombre: "+ nombre_alumno_1, "Apellido: "+apellido_alumnno_1, "Trimestre 1: "+ str(nota_1), "Trimestre 2: "+ str(nota_2), "Trimestre 3: "+ str(nota_3),
     "El promedio de las notas es " + str(Promedio_Nota) ,sep="\n")'''

'''numero = int(input("Ingrese un numero: "))
print(numero)
numero += 1
print(numero)
numero += 1
print(numero)
numero += 1
print(numero)
numero += 1
print(numero)
numero += 1
print(numero)
numero += 1
print(numero)'''


'''Para el departamento de facturación:
A. Ingresar tres precios de productos y mostrar la suma de los mismos.
B. Ingresar tres precios de productos y mostrar el promedio de los mismos.
C. ingresar tres precios de productos sumarlos y mostrar el precio final (más IVA 21%).'''


Precio_1 = int(input("primer precio es ="))
Precio_2 = int(input("segundo precio es ="))
Precio_3 = int(input("tercero precio es ="))
suma = Precio_1 + Precio_2 + Precio_3

print("La suma de los tres es", str(suma))

Precio_1 = int(input("primer precio es ="))
Precio_2 = int(input("segundo precio es ="))
Precio_3 = int(input("tercero precio es ="))
Promedio = (Precio_1 + Precio_2 + Precio_3) / 3

print("El promedio de los tres es", str(Promedio))

Precio_1 = float(input("primer precio es ="))
Precio_2 = float(input("segundo precio es ="))
Precio_3 = float(input("tercero precio es ="))
suma = (Precio_1 + Precio_2 + Precio_3) * 1.21
print("La suma de los tres con iva incluido es de", str(suma))



