from funcioneslibros import *

while True:
    limpiar()
    print("""
        Libreria Online: 
        1. Agregar libro
        2. Mostrar libros
        3. Buscar libro (Ver informacion de un libro en especifico)
        4. Actualizar libro
        5. Imprimir planilla de libros
        6. Salir del programa""")
    opc = validar_opcion()
    limpiar()
    if opc==1:
        opcion1()
    elif opc==2:
        opcion2()
    elif opc==3:
        opcion3()
    elif opc==4:
        opcion4()
    elif opc==5:
        opcion5()
    else:
        opcion6()
    time.sleep(2)