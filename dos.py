import random

nombre = input("Ingresa tu nombre: ")
minusculas = nombre.lower()
apellido = input("Ingresa tu apellido: ")
mayusculas = apellido.upper()
edad = input("Ingresa tu edad: ")
numeros = edad
signos = "!@#$%^&*()/*-+"

cadena = mayusculas + minusculas + numeros + signos

tamano = int(input("Ingresa el tamaño de tu contraseña: "))
longitud = tamano

password = "".join(random.sample(cadena, longitud))

print(password)