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

# Consulta SQL para crear la tabla
crear_tabla_query = """
CREATE TABLE IF NOT EXISTS test_spoti (
    song_name VARCHAR(255),
    artist VARCHAR(255),
    album VARCHAR(255),
    duration_ms INT,
    release_date DATE,
    played_date DATE,
    played_time TIME
)
"""

# Ejecutar la consulta para crear la tabla
cursor.execute(crear_tabla_query)

# Confirmar los cambios
conexion.commit()

# Cerrar el cursor y la conexión
cursor.close()
conexion.close()