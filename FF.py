import msvcrt
import getpass


nombre=str(input("Write Your name:"))

password=getpass.getpass("Write the password:")

while password!= "3112003":

    password = getpass.getpass("Incorrect Password:")

    if password== "3112003":
        break

print("Welcome to PhantomAK 1.7")
print(nombre)
print(" Created by Gael, Rights Reserved Phantom Ak Inc 2019-2020")
print("Today is:")
import time
print(time.strftime("%d/%m/%y"))


print(
'''
Sections:
    
- B1 (Phantom Notes)
    
- C2 (Calculator)
    
- D3 (Dedications)
    
- E4 (EasterEggs)
    
- R5 (Phantom Music)

-A6(ShutDown)
    ''')

B1= ('''
The notebook will open in a moment 
''')

D3=('''
Dedications:
 
People who influenced PhantomAK and are thanked:
 
Abraham: My computacion teacher from Jose Marti School

  Me and Eddy in the creation of PhantomAK 1.0 a 1.4 from Jose Marti School

Professor Robles And Professor Jose Manuel In promoting the Project

My brother Kevin who, despite the fights, was supporting me and is now supporting me from CDMX
      even though we no longer speak



''')

Apartados= ("H1", "C2", "D3", "E4", "S5", "A6")

window=str(input("What section do you want to open?: "))


if window:

        if window== "B1":
            print(B1)
            import Bloc

        elif window=="E4":
            EE=getpass.getpass("Enter the secret word:")
            if EE=="5sos":
                print("You discovered my easteregg, well done ")
                print(nombre)
                print("Thank you for supporting my project, it inspires me to continue, thanks :,D, ATTE: Gael")
                print("Dedicated to my girlfriend Jenn")
                

            else:
                while EE!= "5sos":
                    print("She does not love you")
                    EE=str(input("You Failed, Gael's easter egg is missing:"))
                if EE== "5sos":
                    print("You discovered my easteregg, well done ")
                    print(nombre)
                    print("Thank you for supporting my project, it inspires me to continue, thanks :,D, ATTE: Gael ")
                    print("Dedicated to my girlfriend Jenn")
                  
        elif window== "C2":
            print('''
Welcome to PhantomAK 1.7 Caluculator
     
C2:''')
            valor1=int(input("Write the first number:"))
            valor2=int(input("Write the second number:"))
            resultado=valor1+valor2
            sustraccion=valor1-valor2
            producto=valor1*valor2
            cociente=valor1/valor2
            print("The addition is:")
            print(resultado)
            print("The subtraction is:")
            print(sustraccion)
            print("The multiplication is")
            print(producto)
            print("The division is:")
            print(producto)
            print("Thank you for using the PhantomAK 1.7 calculator.")

        elif window == "D3":
            print(D3)

        elif window == "R5":
            import music

        elif window == "A6":
            import os
            os.system('shutdown -s')

else:
    while window!= Apartados:
        window = str(input("What section do you want to open?: "))

msvcrt.getch()







 

 
  


