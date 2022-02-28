color=input("Ingrese un color: ")

if color.upper() == "ROJO":
    print("Adivinaste el color, crack")
else:
    print("Lo siento, color equivocado :c")



year=input("Ingrese un año: ")
if int(year) > 2021:
    print("Es mayor al 2021 .-.")
elif int(year) == 2021:
    print("es el 2021, ^-^")
else:
    print("Es menor al 2021")


print("********************EJEMPLO 3********************")
nombre="james"
ciudad="medellin"
continente="america"
edad=20
mayoriaEdad=18

if edad >= mayoriaEdad:
    print(f"{nombre} es mayor de edad")
    if continente != "america":
        print(f"{nombre} no es de america y vive en {ciudad}")
    else:
        print(f"{nombre} si es de america B|")
else:
    print(f"{nombre} es menor de edad .-.")


print("\n\n****************EJEMPLO 4****************\n\n")
dia=int(input("Ingrese un numero entre 1 y 7 porfis: "))
"""if dia==1:
    print("Es lunes :c")
else:
    if dia==2:
        print("Es martes jeje")
    else:
        if dia==3:
            print("Es miercoles :3")
        else
            if dia==4:
                print("Es jueveees uwu")
            else:
                if dia==5:
                    print("Es viernes 3:)")
                else
                    if dia==6:
                        print("Es savado :)")
                    else
                        if dia==7:
                            print("Es domingo O:)")
                        else:
                            print("Opcion incorrecta :/")
 """
if dia==1:
    print("Es lunes")
elif dia==2:
    print("Es Martes")
elif dia==3:
    print("Es Miercoles")
elif dia==4:
    print("Es Jueves")
elif dia==5:
    print("Es Viernes")
elif dia==6:
    print("Es Sabado")
elif dia==7:
    print("Es Domingo")
else:
    print("Opcion incorrecto")