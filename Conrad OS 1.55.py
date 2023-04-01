import msvcrt
import getpass
print(''''
 xxxxxxxxxxxxxxxxxxxxxx
 x--------------------x
 x-----Phantom AK------x
 x--------------------x
 xxxxxxxxxxxxxxxxxxxxxx
 ''')
print("Idiomas")
print("-ES")
print("-EN")
Idioma=str(input("Elige tu idioma preferido-Choose your preferred language:"))

if Idioma=="ES":
    print("Bienvenido")

    nombre=str(input("Escribe tu nombre:"))
    password = getpass.getpass("Ingrese el password:")

    while password != "3112003":

        password = getpass.getpass("Ingrese el password correctamente:")

        if password == "3112003":
            break

    print("Bienvenido a PhantomAK version 1.7")
    print(nombre)
    print(" Creado por Gael Meza")
    print("Hoy es:")
    import time
    print(time.strftime("%d/%m/%y"))

    print(
        '''
        Apartados:
    
        - B1(BLOC DE NOTAS)
    
        - C2(CALCULADORA)
    
        - D3(DEDICACIONES)
    
        - E4(EASTEREGGS)
    
        - R5(REPRODUCTOR)
        
        -A6(APAGADO)
            ''')

    B1 = ('''
    El bloc de notas abrira en un momento
    ''')

    D3 = ('''
    Dedicaciones:

    Personas que influyeron en PhantomAK y se les agradece:

    Abraham: Mi profesor de computacion del colegio Jose Marti

     Yo y Eddy en la creacion de PhantomAK 1.0 a la version 1.4 ,del colegio Jose Marti  

     El Profe Robles Y El Profe Jose Manuel En impulsar el Proyecto

     Mi Novia Jenn que me estuvo apoyando

    
   
    ''')

    Apartados = ("H1(HISTORIA)", "C2(CALCULADORA)", "D3(DEDICACIONES)", "E4(EASTEREGGS)", "R5(REPRODUCTOR)","A6(APGADO)")

    window = str(input("¿Que apartado deseas abrir?: "))

    if window:

        if window == "B1":
            print(B1)
            import Bloc

        elif window == "E4":
            EE = getpass.getpass("Ingresa la palabra secreta: ")
            if EE == "5sos":
                print("Descubriste mi easteregg, bien hecho ")
                print("Gracias por apoyar mi proyecto,me inspira a seguir,gracias :D, ATTE:Gael ")
                print("Dedicado para mi novia Jenn")


            else:
                while EE != "5sos":
                    print("Ella no te ama")
                    EE = getpass.getpass("Fallaste,Sigue buscando:")
                if EE == "5sos":
                    print("Descubriste mi easteregg,bien hecho ")
                    print(nombre)
                    print("Gracias por apoyar mi proyecto,me inspira a seguir,gracias :D, ATTE:Gael ")
                    print("Dedicado para mi novia Jenn")


        elif window == "C2":
            print('''
    Bienvenido A La caluculadora de PhantomAK 1.7

    Calculadora:''')
            valor1 = int(input("Ingresa tu primer valor:"))
            valor2 = int(input("Ingresa tu segundo valor:"))
            resultado = valor1 + valor2
            sustraccion = valor1 - valor2
            producto = valor1 * valor2
            cociente = valor1 / valor2
            print("La suma es:")
            print(resultado)
            print("La resta es:")
            print(sustraccion)
            print("La multiplicacion es")
            print(producto)
            print("La division es:")
            print(cociente)
            print("Gracias por utlizar la calculadora de PhantomAK 1.7")

        elif window == "D3":
            print(D3)

        elif window == "R5":
            import Musica

        elif window == "A6":
            import os
            os.system('shutdown -s')

else:
    import FF
msvcrt.getch()









