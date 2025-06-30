
compradores = {
    "Compradores":[
        {
            "Comprador_1":"Nombre1",
            "Comprador_2":"Nombre2"
        }
    ]
}



def concepcion():
    while True:
        try:
            comprador = str(input("Ingresa el nombre del comprador: "))
            for i in compradores["Compradores"]:
                print(i[0])
                if comprador == i:
                    print("Error, este comprador ya esta ingresado en el sistema y no puede repetirse")
                    continue
            break
        except ValueError:
            print("Error, no puedes ingresar numeros")
            continue
        
    while True:
        contador_Mayusculas = 0
        contador_codigo = 0
        codigo_confirmacion = str(input("Ingresa el codigo de confirmacion (minimo 6 caracteres, al menos una letra mayuscula, un numero y sin espacios): "))
        for i in codigo_confirmacion:
            if i == i.upper:
                contador_Mayusculas += 1
            contador_codigo += 1
            if contador_codigo < 6:
                print("Error, codigo demasiado corto")
                print(contador_codigo)
                print(contador_Mayusculas)
                continue
    



while True:
    print("TOTEM AUTOSERVICIO GIRA ROCK AND CHILE IN CHILE")
    print("1.- Comprar entrada a “los Fortificados” en Concepción.")
    print("2.- Comprar entrada a “los Fortificados” en Puente Alto.")
    print("3.- Comprar entrada a “los Fortificados” en Muelle Barón en Valparaíso.")
    print("4.- Comprar entrada a “los Fortificados” en Muelle Vergara en Viña del Mar.")
    print("5.- Salir")
    try:
        opcion = int(input("Ingrese una opcion: "))
    except ValueError:
        print("Debe ingresar una opción válida!!")
        continue

    if opcion == 1:
        concepcion()
    
    elif opcion == 2:
        dsgfh

    elif opcion == 3:
        asdgfhj

    elif opcion == 4:
        adwgr
    
    elif opcion == 5:
        ergferhtyj

    else:
        print("Debe ingresar una opción válida!!")