print("+++++++++++++++ALMACEN:'El Buen Precio'+++++++++++++++\n");

nombre = str(input("Ingrese su nombre: "));
anio = int(input("Ingrese su año de nacimiento: "))

edad = 2022-anio

if edad < 18:
    print("Lo sentimos, pero es menor de edad. Hasta pronto.")
else:
    print("¨¨¨¨¨¨¨¨¨¨¨¨VENTAS DEL AÑO 2021¨¨¨¨¨¨¨¨¨¨¨¨\n");
    ventaPrimerSem = float(input("Ingrese las ventas del primer semestre: "));
    ventaSegundoSem = float(input("Ingrese las ventas del segundo semestre: "));
    Total = float(ventaPrimerSem+ventaSegundoSem);
    if ventaPrimerSem > ventaSegundoSem :
        mejor1 = "Primer semestre, mejor venta";
    elif ventaSegundoSem> ventaPrimerSem:
        mejor1 = "Segundo semestre, mejor venta";
    else:
        mejor1 = "Vendio lo mismo en ambos semestres"
    if Total <= 100000:
        Medalla = "Medalla Bronce";
        Premio = "Un día libre";
        Bono = "Bono: Q 0.00";
    elif Total <= 500000:
        Medalla = "Medalla Plata";
        Premio = "Un día libre";
        Bono = "Bono: Q 250.00";
    elif Total <= 1000000:
        Medalla = "Medalla Oro";
        Premio = "Un día libre"
        Bono = "Bono: Q 500.00"
    elif Total > 1000000:
        Medalla = "Medalla Diamante";
        Premio = "Dos días libres"
        Bono = "Bono: Q 1000.00"

    print("Vendedor: "+nombre);
    print("Ventas anuales: Q "+str(Total));
    print("Mejor Semestre: "+mejor1);
    print("Medalla acreditada: "+Medalla);
    print("Premio: "+Premio);
    print(Bono)