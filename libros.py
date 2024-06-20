from funcioneslibros import *

while True:
    os.system("cls")
    print("""
        Libreria Online: 
        1. Agregar libro
        2. Mostrar libros
        3. Imprimir planilla de libros
        4. Salir del programa""")
    opc = int(input("Ingrese opcion: "))
    os.system("cls")
    if opc==1:
        opcion1()
    elif opc==2:
        opcion2()
    elif opc==3:
        opcion3()
    else:
        opcion4()
    time.sleep(2)