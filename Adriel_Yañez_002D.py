productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
             '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
             'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
             'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
             'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
             '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
             '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
             'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
        'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
        'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0]}

##Seguir
def stock_marca():
    marca_encontrada_1 = " "
    marca_encontrada_2 = " "
    marca_encontrada_3 = " "
    marca_encontrada_4 = " "
    marca_encontrada_5 = " "
    marca_encontrada_6 = " "
    marca_encontrada_7 = " "
    marca_encontrada_8 = " "

    buscador_marca = input("Ingresa marca a consultar: ")
    buscador_marca_lower = buscador_marca.lower()
    if buscador_marca_lower == "hp" or buscador_marca_lower == "lenovo" or buscador_marca_lower == "asus" or buscador_marca_lower == "Dell":
        for i in productos['8475HD']:
            if i == buscador_marca:
                marca_encontrada_1 = "8475HD"

        for i in productos['2175HD']:
            if i == buscador_marca:
                marca_encontrada_2 = "2175HD"

        for i in productos['JjfFHD']:
            if i == buscador_marca:
                marca_encontrada_3 = "JjfFHD"

        for i in productos['fgdxFHD']:
            if i == buscador_marca:
                marca_encontrada_4 = "fgdxFHD"

        for i in productos["GF75HD"]:
            if i == buscador_marca:
                marca_encontrada_5 = "GF75HD"

        for i in productos["123FHD"]:
            if i == buscador_marca:
                marca_encontrada_6 = "123FHD"

        for i in productos["342FHD"]:
            if i == buscador_marca:
                marca_encontrada_7 = "342FHD"

        for i in productos["UWU131HD"]:
            if i == buscador_marca:
                marca_encontrada_8 = "UWU131HD"
    
        if marca_encontrada_1 != " ":
            for i in reversed(stock['8475HD']):
                marca_encontrada_1 = i
                break
        else:
            marca_encontrada_1 = 0

        if marca_encontrada_2 != " ":
            for i in reversed(stock["2175HD"]):
                marca_encontrada_2 = i
                break
        else:
            marca_encontrada_2 = 0

        if marca_encontrada_3 != " ":
            for i in reversed(stock["JjfFHD"]):
                marca_encontrada_3 = i
                break
        else:
            marca_encontrada_3 = 0

        if marca_encontrada_4 != " ":
            for i in reversed(stock["fgdxFHD"]):
                marca_encontrada_4 = i
                break
        else:
            marca_encontrada_4 = 0

        if marca_encontrada_5 != " ":
            for i in reversed(stock["GF75HD"]):
                marca_encontrada_5 = i
                break
        else:
            marca_encontrada_5 = 0

        if marca_encontrada_6 != " ":
            for i in reversed(stock["123FHD"]):
                marca_encontrada_6 = i
                break
        else:
            marca_encontrada_6 = 0

        if marca_encontrada_7 != " ":
            for i in reversed(stock["342FHD"]):
                marca_encontrada_7 = i
                break
        else:
            marca_encontrada_7 = 0

        if marca_encontrada_8 != " ":
            for i in reversed(stock["UWU131HD"]):
                marca_encontrada_8 = i
                break
        else:
            marca_encontrada_8 = 0

    print("El stock es:",marca_encontrada_1 + marca_encontrada_2 + marca_encontrada_3 + marca_encontrada_4 + marca_encontrada_5 + marca_encontrada_6 + marca_encontrada_7 + marca_encontrada_8)

def busqueda_precio(p_min,p_max):
    p_min = precio_minimo
    p_max = precio_maximo
    marca_encontrada_1 = " "
    marca_encontrada_2 = " "
    marca_encontrada_3 = " "
    marca_encontrada_4 = " "
    marca_encontrada_5 = " "
    marca_encontrada_6 = " "
    marca_encontrada_7 = " "
    marca_encontrada_8 = " "
    no_encontrado = False

    for i in stock['8475HD']:
        if i < p_max and i > p_min:
            marca_encontrada_1 = "HP--8475HD"
            break
        else:
            marca_encontrada_1 = " "
            break
    
    for i in stock["2175HD"]:
        if i < p_max and i > p_min:
            marca_encontrada_2 = "lenovo--2175HD"
            break
        else:
            marca_encontrada_2 = " "
            break
    
    for i in stock["JjfFHD"]:
        if i < p_max and i > p_min:
            marca_encontrada_3 = "Asus--JjfFHD"
            break
        else:
            marca_encontrada_3 = " "
            break
    
    for i in stock["fgdxFHD"]:
        if i < p_max and i > p_min:
            marca_encontrada_4 = "HP--fgdxFHD"
            break
        else:
            marca_encontrada_4 = " "
            break
    
    for i in stock["GF75HD"]:
        if i < p_max and i > p_min:
            marca_encontrada_5 = "Asus--GF75HD"
            break
        else:
            marca_encontrada_5 = " "
            break
    
    for i in stock["123FHD"]:
        if i < p_max and i > p_min:
            marca_encontrada_6 = "lenovo--123FHD"
            break
        else:
            marca_encontrada_6 = " "
            break
    
    for i in stock["342FHD"]:
        if i < p_max and i > p_min:
            marca_encontrada_7 = "lenovo--342FHD"
            break
        else:
            marca_encontrada_7 = " "
            break
    
    for i in stock["UWU131HD"]:
        if i < p_max and i > p_min:
            marca_encontrada_8 = "Dell--UWU131HD"
            break
        else:
            marca_encontrada_8 = " "
            break
    
    if marca_encontrada_1 == " ":
        if marca_encontrada_2 == " ":
            if marca_encontrada_3 == " ":
                if marca_encontrada_4 == " ":
                    if marca_encontrada_5 == " ":
                        if marca_encontrada_6 == " ":
                            if marca_encontrada_7 == " ":
                                if marca_encontrada_8 == " ":
                                    no_encontrado = True
    if no_encontrado == True:
        print("No hay notebooks en ese rango de precios")
    else:
        print("Los notebooks entre los precios consultas son: [",marca_encontrada_1," ",marca_encontrada_2," ",marca_encontrada_3," ",marca_encontrada_4," ",marca_encontrada_5," ",marca_encontrada_6," ",marca_encontrada_7," ",marca_encontrada_8,"]")

def actualizar_precio(modelo_p):
    modelo_encontrado = " "
    for i in productos:
        if i == modelo_p:
            modelo_encontrado = i
            break
    if modelo_encontrado == " ":
        return False
    nuevo_precio = int(input("Ingrese precio nuevo: "))
    for i in stock[f"{modelo_encontrado}"]:
        stock[f"{modelo_encontrado}"].remove(i)
        if i < 500:
            cantidad_temporal_actualizacion = i
            stock[f"{modelo_encontrado}"].append(nuevo_precio)
            stock[f"{modelo_encontrado}"].append(cantidad_temporal_actualizacion)
            break




while True:
    print("*** MENU PRICIPAL ***")
    print("1. Stock Marca.")
    print("2. Busqueda por precio.")
    print("3. Actualizar precio.")
    print("4. Salir.")
    try:
        opcion = int(input("Ingrese opcion: "))
    except ValueError:
        print("Debes seleccionar una opcion valida!!!")
        continue

    if opcion == 1:
        stock_marca()

    if opcion == 2:
        try:
            precio_minimo = int(input("Ingrese precio minimo: "))
            precio_maximo = int(input("Ingrese precio maximo: "))
            busqueda_precio(precio_minimo,precio_maximo)
        except ValueError:
            print("Debe ingresar valores enteros!!!")
            continue
    
    if opcion == 3:
        actualizar_modelo = input("Ingrese modelo a actualizar: ")
        actualizar_precio(actualizar_modelo)