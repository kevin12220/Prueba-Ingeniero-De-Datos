import csv
import psycopg2

conn = psycopg2.connect(
   host="localhost",
   port="5432",
   database="usuario",
   user="postgres",
   password="12345"
)
cursor = conn.cursor()

with open(r"C:\Users\valen13\Downloads\Prueba Tecnica\Api\src\data.csv", "r", encoding="UTF-8") as archivo:
    lector = csv.DictReader(archivo,delimiter=";")

    for fila in lector:
        cursor.execute(
           """
           INSERT INTO usuarios (id, nombre, correo, telefono)
           VALUES (%s, %s, %s, %s)
           """,
           (
              int(fila["id"]),
              fila["nombre"],
              fila["correo"],
              fila["telefono"]
            )
        )
conn.commit()
print("✅ Datos cargados correctamente")
cursor.close()
conn.close()

