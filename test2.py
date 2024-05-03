import mysql.connector


# Establecer la conexión con la base de datos
conexion = mysql.connector.connect(
    host="database-test.cfmse2i6c9e0.eu-north-1.rds.amazonaws.com",
    user="admin",
    password="Admin123",
    database="spotify_test")


cursor = conexion.cursor()

# Define los valores de la fila que deseas agregar
nueva_fila = ('asdf', 'asdf', '2021-01-01', 123456, '2021-01-01', '2021-01-01', '12:00:00')

# Consulta SQL de inserción para agregar la nueva fila
insertar_nueva_fila_query = """
INSERT INTO nombre_tabla (
    song_name,
    artist,
    album,
    duration_ms,
    release_date,
    played_date,
    played_time
)
VALUES (%s, %s, %s, %s, %s, %s, %s)
"""

# Ejecuta la consulta de inserción con los valores de la nueva fila
cursor.execute(insertar_nueva_fila_query, nueva_fila)

# Confirma los cambios en la base de datos
conexion.commit()

# Cierra el cursor y la conexión
cursor.close()
conexion.close()