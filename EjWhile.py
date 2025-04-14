a = 0
while a <= 5:
    print(a)
    a += 1

acumulador = 0
actived = True
while actived:
    valor = input("ingrese un valor: ")
    valor = int(valor)
    acumulador += valor
    if  acumulador >= 20:
        actived = False
print(acumulador)

encuestas = 0
contador_a = 0
contador_b = 0

while encuestas < 10:
    respuesta = input("Que producto prefiere?(A o B): ").lower()
    match respuesta:
        case "a":
            contador_a += 1
        case "b":
            contador_b += 1
    encuestas +=1

porcentaje_a = (contador_a * 100) / encuestas
porcentaje_b = (contador_b * 100) / encuestas

print(f"Porcentaje de personas que eligen el producto A: {porcentaje_a}")
print(f"Porcentaje de personas que eligen el producto B: {porcentaje_b}")

while True:
    nota = input("Ingrese su nota: ")
    if nota == "FIN":
        break
    else:
        total_notas += int(nota)
        alumnos_registrados += 1

promedio = total_notas / alumnos_registrados
print(f"El promedio de las notas es: {promedio}")