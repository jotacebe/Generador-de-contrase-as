import random
from os import system

numeros = ["0","1","2","3","4","5","6","7","8","9"]
minusculas = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
mayusculas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
simbolos = ["!", "$", "%", "&", "/", "(", ")", "=", "?", "¿", "@", "#", "¡", "+", "-", "*", "_", ";", ":", "{", "}", "[", "]"]

caracteres = []

def menu():
    system("cls")
    print("GENERADOR DE CONTRASEÑAS")
    print("1. Generar contraseña personalizada")
    print("2. Generar contraseña aleatoria.")
    print("3. Salir")
    while (opcion := input("Opción: ")) not in ["1", "2", "3"]:
        opcion = input("Opción: ")
    else:
        if opcion == "1":
            personalizada()
        elif opcion == "2":
            aleatoria()
        else:
            system("cls")
            system("exit")
    
def personalizada():
    while (longitud := input("Longitud de la contraseña: ")).isdecimal() == False:
        longitud = input("Longitud de la contraseña: ")
    while (siNumero := input("¿Quieres que la contraseña contenga números? (s/n) ").lower()) not in ["s", "n"]:
        siNumero = input("¿Quieres que la contraseña contenga números? (s/n) ")
    while (siMinusculas := input("¿Quieres que la contraseña contenga letras minúsculas? (s/n) ").lower()) not in ["s", "n"]:
        siMinusculas = input("¿Quieres que la contraseña contenga letras minúsculas? (s/n) ")
    while (siMayusculas := input("¿Quieres que la contraseña contenga letra mayúsuculas? (s/n) ").lower()) not in ["s", "n"]:
        siMayusculas = input("¿Quieres que la contraseña contenga letras mayúsculas? (s/n) ")
    while (siSimbolos := input("¿Quieres que la contraseña contenga caracteres especiales? (s/n) ").lower()) not in ["s", "n"]:
        siSimbolos = input("¿Quieres que la contraseña contenga caracteres especiales? (s/n) ")

    while (cantidad := input("Número de contraseñas que se van a generar: ")).isdecimal() == False:
            cantidad = input("Número de contraseñas que se van a generar: ")

    if siNumero == "s":
        caracteres.append(numeros)
    if siMinusculas == "s":
        caracteres.append(minusculas)
    if siMayusculas == "s":
        caracteres.append(mayusculas)
    if siSimbolos == "s":
        caracteres.append(simbolos)  

    if len(caracteres) > 0:
        for m in range(int(cantidad)):
            contraseña = ""
            for n in range(int(longitud)):
                contraseña += random.choice(random.choice(caracteres))
            print(contraseña)

def aleatoria():
    caracteres = [numeros, minusculas, mayusculas, simbolos]
    while (cantidad := input("Número de contraseñas que se van a generar: ")).isdecimal() == False:
            cantidad = input("Número de contraseñas que se van a generar: ")
    for m in range(int(cantidad)):
        contraseña = ""
        longitud = random.randrange(1, 50)
        for n in range(int(longitud)):
            contraseña += random.choice(random.choice(caracteres))
        print(contraseña)
    otro = ""
    while otro not in ["s", "n"]:
        otro = input("¿Quieres generar más contraseñas? (s/n)").lower()
    if otro == "s":
        menu()
    else:
        system("cls")
        system("exit")


def ayuda():
    pass

menu()
