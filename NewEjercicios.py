print("Usuario: \n[1] Cliente Regular\n[2] Cliente VIP\n[3] Empleado del supermercado")
Solicitar_Usuario = int(input("Ingresar usuario: "))
Monto_Total = float(input("Monto total de la compra: "))
Cantitad_Total = float(input("Cantidad de productos comprados: "))

if Solicitar_Usuario == 1:
    print("Cliente Regular") 
    print("El monto total SIN impuesto es:", Monto_Total)

    if Monto_Total >= 100000 or Cantitad_Total >= 25: 
        Monto_Total -= Monto_Total * 0.10
        print("El monto con descuento aplicado es:", Monto_Total)
    
    if Monto_Total <= 50000 and Cantitad_Total >= 15:
        Monto_Total -= Monto_Total * 0.05
        print("Descuento Bonus Aplicado:", Monto_Total)
    
    Monto_Total = Monto_Total * 1.21
    print("El monto total CON impuesto es:", Monto_Total)
    print("Total a pagar:", Monto_Total)
    
elif Solicitar_Usuario == 2:
    print("Cliente VIP")
    print("El monto total SIN impuesto es:", Monto_Total)

    if Monto_Total >= 80000: 
        Monto_Total -= Monto_Total * 0.15
        if Cantitad_Total >= 20:
            Monto_Total -= Monto_Total * 0.05
            print("El monto con descuento BONUS aplicado es:", Monto_Total)
        else:
            print("El monto con descuento aplicado es:", Monto_Total)
    
    if Monto_Total <= 50000 and Cantitad_Total >= 15:
        Monto_Total -= Monto_Total * 0.05
        print("Descuento Bonus Aplicado:", Monto_Total)
    
    Monto_Total = Monto_Total * 1.21

    print("El monto total CON impuesto es:", Monto_Total)
    print("TOTAL A PAGAR:", Monto_Total)

elif Solicitar_Usuario == 3:
    print("Empleado")
    print("El monto total SIN impuesto es:", Monto_Total)

    Monto_Total -= Monto_Total * 0.20
    print("El monto con descuento aplicado es:", Monto_Total)
    
    if Monto_Total <= 50000 and Cantitad_Total >= 15:
        Monto_Total -= Monto_Total * 0.05
        print("Descuento Bonus Aplicado:", Monto_Total)
    
    Monto_Total = Monto_Total * 1.21
    print("El monto total CON impuesto es:", Monto_Total)
    print("Total a pagar:", Monto_Total)

else:
    print("Usuario no identificado")