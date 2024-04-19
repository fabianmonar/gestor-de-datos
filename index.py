import sqlite3

# conexion a la base de datos

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

#crear tabla si no existe
cursor.execute("""
               CREATE TABLE IF NOT EXISTS usuarios(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nombre TEXT,
               email TEXT
               )
               """)

conn.commit()

# crear resgistro ->c

def crear_usuario(nombre: str, email)-> str:
    cursor.execute("INSERT INTO usuarios(nombre, email) VALUES (?,?)", (nombre, email))
    conn.commit()
    return"Usuario Agregado"

# obtener registros

def obtener_registros() -> list:
    cursor.execute("SELECT id, nombre, email FROM usuarios")
    usuarios =  cursor.fetchall()
     
    lista_usuarios = []
    for usuario in usuarios:
        lista_usuarios.append(usuario)
   
    return lista_usuarios

# Actualizar usuario

def Actualizar_usuario(id: int, nombre:str, email: str) -> str:
    cursor.execute(
        "UPDATE usuarios SET nombre=?, email=? WHERE id = ?" , (nombre, email, id)
    )
    # Se ejecuta una consulta SQL para actualizar los datos del usuario en la tabla "usuarios". Se utilizan marcadores de posición (?) para los valores que se van a actualizar.
    # El método "execute" del objeto "cursor" ejecuta la consulta SQL.
    # Se proporcionan los valores a actualizar (nombre, email, id) como una tupla como segundo argumento del método "execute".
    
    conn.commit()
    return "usuario actualizado"

#eliminar usuario
def eliminar_usuario(id) -> str:
    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id,))
    conn.commit()
    return "Usuario eliminado"
# Leer registro por su id
def obtener_usuario(id: int) -> list:
    cursor.execute("Select id, nombre, email FROM usuarios WHERE id = ?", (id,))
    usuario = cursor.fetchone()

    if usuario:
        return usuario
    return "Usuario no encontrado"

# crear usuario
# crear_usuario("Brenda", "brenda@example.com")
# crear_usuario("Andres", "andres@example.com")
# crear_usuario("Caiceo", "caiceo@example.com")

#print(obtener_usuarios())

#Actualizar usuarios 
print(Actualizar_usuario(2, "Andres Lopez", "andres@example.com"))

# obtener_usuario
print(obtener_usuario(1))

# eliminar usuario
print(eliminar_usuario(5))
print(eliminar_usuario(6))
print(eliminar_usuario(7))
print(eliminar_usuario(8))
