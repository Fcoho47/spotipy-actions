import mysql.connector


config = {
        'user': 'bfb762b6680bff',
        'password': '1735c6f6',
        'host': 'us-cluster-east-01.k8s.cleardb.net',
        'database': 'heroku_2a3b9dd61a6a5f6',
        'port': '3306',
    }

# Establecer la conexión con la base de datos
conexion = mysql.connector.connect(**config
)

# Cursor para ejecutar comandos SQL
cursor = conexion.cursor()

# Define los valores de la fila que deseas agregar
nueva_fila = ('asdf', 'asdf', '2021-01-02', 123456, '2021-01-01', '2021-01-01', '12:00:00')

# Consulta SQL de inserción para agregar la nueva fila
insertar_nueva_fila_query = """
INSERT INTO test_spoti (
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