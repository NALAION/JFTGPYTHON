import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python"
)

resultados = conexion.cursor()

a = input("Inserta un nombre a la base de datos: \n")
b = input("Inserta un usuario a la base de datos: \n")


peticion = "INSERT INTO usuarios (id, nombre, usuario) VALUES (%s, %s, %s)"
valores = (None, a, b)

resultados.execute(peticion, valores)

print(f"Tus datos han sido agregados satisfactoriamente\nNombre: {a}\nUsuario: {b}")

conexion.commit()


resultados2 = conexion.cursor()

peticion2 = "SELECT * FROM usuarios"

resultados2.execute(peticion2)

datos = resultados2.fetchall()

for fila in datos:
    print(fila[0])