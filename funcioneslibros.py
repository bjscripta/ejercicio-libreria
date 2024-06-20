import json,time,os

libros = []

def limpiar():
    os.system("cls")

def opcion1():
    print("AGREGAR LIBRO")
    titulo = validar_nombre()
    autor = validar_autor()
    ano = validar_ano()
    genero = validar_genero()
    libro = ({
        "titulo": titulo,
        "autor": autor,
        "año": ano,
        "genero": genero
    })
    libros.append(libro)
    print("LIBRO REGISTRADO!")

def opcion2():
    print("LISTAR LIBROS")
    if len(libros)==0:
        print("Error, No hay libros registrados")
    else:
        a = 1
        for j in libros:
            print(f"{a}. Titulo:{j['titulo']} Autor:{j['autor']} Año:{j['año']} Genero:{j['genero']}")
            a += 1


def opcion3(libros):
    print("BUSCAR LIBRO POR TITULO")
    if len(libros)==0:
        print("No hay libros registrados")
    else:
        titulo = input("Ingrese titulo del libro a buscar: ")
        libro_encontrado = False
        for l in libros:
            if l["titulo"]==titulo:
                print(f'Titulo:{l["titulo"]} Autor:{l["autor"]} Año:{l["año"]} Genero:{l["genero"]}')
                libro_encontrado = True
                break
        if not libro_encontrado:
            print("Error, no se encontro el libro con el titulo ingresado")

def opcion4(libros):
    print("Actualizar informacion de libro")
    if len(libros)==0:
        print("Error, No hay libros registrados")
    else:
        titulo = input("Ingrese titulo del libro a buscar: ")
        for l in libros:
            if l["titulo"]==titulo:
                print(f"Titulo:{l["titulo"]} Autor:{l["autor"]} Año:{l["año"]} Genero:{l["genero"]}")
                print("Ingrese nueva informacion del libro")
                l["titulo"] = validar_nombre()
                l["autor"] = validar_autor()
                l["año"] = validar_ano()
                l["genero"] = validar_genero()
                print("Informacion actualizada")
                break
            else:
                print("Error, No se encontro el libro")


def opcion5():
    print("Imprimir planilla de libros")
    if len(libros)==0:
        print("Error, No hay libros registrados")
    else:
        librojson = input("Ingrese nombre del archivo: ") + ".json"
        with open(f"{librojson}","w") as archivo:
            json.dump(libros,archivo,indent=4)
        print("Planilla de libros impresa")


def opcion6():
    print("Gracias por usar el programa, adios!")
    exit()

#validaciones de datos

def validar_nombre():
    while True:
        titulo = input("Ingrese titulo: ")
        if len(titulo) >= 3:
            return titulo
        else:
            print("Error, El titulo debe tener mas de 3 caracteres")

def validar_autor():
    while True:
        autor = input("Ingrese autor: ")
        if len(autor) >= 3:
            return autor
        else:
            print("Error, El autor debe tener mas de 3 caracteres")

def validar_ano():
    while True:
        ano = input("Ingrese año: ")
        if len(ano) == 4:
            return ano
        else:
            print("Error, El año debe tener 4 caracteres")

def validar_genero():
    while True:
        genero = input("Ingrese genero: ")
        if len(genero) > 3:
            return genero
        else:
            print("Error, El genero debe tener mas de 3 caracteres")

def validar_opcion():
    while True:
        try:
            opc = int(input("Ingrese opcion: "))
            if opc in (1,2,3,4,5,6):
                return opc
            else:
                print("Error, Ingrese una opcion valida")
        except:
            print("Error, Ingrese una opcion valida")


