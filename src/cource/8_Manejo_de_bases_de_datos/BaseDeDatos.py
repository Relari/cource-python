import sqlite3

if __name__ == '__main__':

    # Conectar a la base de datos (o crearla si no existe)
    conexion = sqlite3.connect("mi_base.db")

    # Crear un cursor para ejecutar consultas SQL
    cursor = conexion.cursor()

    # Crear una tabla
    cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios (
                        id INTEGER PRIMARY KEY, 
                        nombre TEXT, 
                        edad INTEGER)""")

    # Insertar datos
    cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", ("Renzo", 25))
    conexion.commit()

    # Consultar datos
    cursor.execute("SELECT * FROM usuarios")
    print(cursor.fetchall())

    conexion.close()