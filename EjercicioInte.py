Tipo_Usuarios = input("Tipos de cliente: \nSocio VIP\nCliente Frecuente\nGeneral\nIngrese su tipo de cliente: ").lower()
Cantidad_Entradas = int(input("Cantidad de entradas: "))
Precio_Entradas = 50
Descuento = 0
Precio_Total = 0

Precio_Total += Precio_Entradas * Cantidad_Entradas

if Cantidad_Entradas >= 6:
    Descuento += 50

if Cantidad_Entradas == 5 and Tipo_Usuarios == "socio vip":
    Descuento += 40
elif Cantidad_Entradas == 5:
    Descuento += 30
elif Cantidad_Entradas == 4 and Tipo_Usuarios == "socio vip" or Tipo_Usuarios == "cliente frecuente":
    Descuento += 25
elif Cantidad_Entradas == 4:
    Descuento += 20
elif Cantidad_Entradas == 3:
    match Tipo_Usuarios:
        case "socio vip":
            Descuento += 15

        case "cliente frecuente":
            Descuento += 10

        case _:
            Descuento += 5

if  Cantidad_Entradas == 2:
    Descuento += 5

Precio_Total *= Descuento / 100

if  Cantidad_Entradas == 1:
    Precio_Total = Precio_Entradas


print("El precio total de las entradas son de:", Precio_Total)


