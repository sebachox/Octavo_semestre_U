"""
API REST con FastAPI - Ejemplo documentado para clase
Todo en un solo archivo: base de datos, modelo y endpoints (insert, update, delete, list).

Cómo correr:
    pip install fastapi uvicorn
    uvicorn app:app --reload

Documentación interactiva (Swagger UI) generada automáticamente:
    http://127.0.0.1:8000/docs

Documentación alternativa (ReDoc):
    http://127.0.0.1:8000/redoc
"""

import sqlite3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

# ---------------------------------------------------------
# Metadatos generales de la API (aparecen arriba en /docs)
# ---------------------------------------------------------
app = FastAPI(
    title="API de Productos",
    description=(
        "API REST de ejemplo construida con FastAPI. "
        "Permite insertar, actualizar, eliminar y listar productos "
        "guardados en una tabla SQLite. Proyecto académico."
    ),
    version="1.0.0",
)

DB_NAME = "datos.db"


# ---------------------------------------------------------
# 1. Crear la tabla al iniciar la aplicación
# ---------------------------------------------------------
def crear_tabla():
    """Crea la tabla 'productos' en SQLite si todavía no existe."""
    conexion = sqlite3.connect(DB_NAME)
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            precio REAL NOT NULL
        )
    """)
    conexion.commit()
    conexion.close()


crear_tabla()


# ---------------------------------------------------------
# 2. Modelo de datos (lo que se recibe en insert/update)
#    Pydantic valida automáticamente el JSON que llega
#    y esta clase es la que Swagger usa para mostrar
#    el "esquema" (Schema) del cuerpo de la petición.
# ---------------------------------------------------------
class Producto(BaseModel):
    nombre: str = Field(..., description="Nombre del producto", examples=["Cuaderno"])
    precio: float = Field(..., description="Precio del producto en pesos", examples=[3500])


# ---------------------------------------------------------
# 3. Endpoints
#    summary / description / tags / responses controlan
#    cómo se ve cada endpoint en Swagger (/docs).
# ---------------------------------------------------------

@app.post(
    "/productos",
    tags=["Productos"],
    summary="Insertar un producto",
    description="Crea un nuevo producto en la tabla y devuelve el id generado.",
    status_code=201,
)
def insertar_producto(producto: Producto):
    """
    INSERT: recibe un Producto (nombre, precio), lo valida con Pydantic
    y lo guarda en la tabla 'productos' de SQLite.
    """
    conexion = sqlite3.connect(DB_NAME)
    cursor = conexion.cursor()
    cursor.execute(
        "INSERT INTO productos (nombre, precio) VALUES (?, ?)",
        (producto.nombre, producto.precio)
    )
    conexion.commit()
    nuevo_id = cursor.lastrowid
    conexion.close()
    return {"mensaje": "Producto insertado", "id": nuevo_id}


@app.put(
    "/productos/{producto_id}",
    tags=["Productos"],
    summary="Actualizar un producto",
    description="Reemplaza nombre y precio de un producto existente, identificado por su id.",
)
def actualizar_producto(producto_id: int, producto: Producto):
    """
    UPDATE: primero verifica que el id exista (si no, error 404),
    luego actualiza nombre y precio en la tabla.
    """
    conexion = sqlite3.connect(DB_NAME)
    cursor = conexion.cursor()
    cursor.execute("SELECT id FROM productos WHERE id = ?", (producto_id,))
    existe = cursor.fetchone()

    if not existe:
        conexion.close()
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    cursor.execute(
        "UPDATE productos SET nombre = ?, precio = ? WHERE id = ?",
        (producto.nombre, producto.precio, producto_id)
    )
    conexion.commit()
    conexion.close()
    return {"mensaje": f"Producto {producto_id} actualizado"}


@app.delete(
    "/productos/{producto_id}",
    tags=["Productos"],
    summary="Eliminar un producto",
    description="Elimina de la tabla el producto que tenga el id indicado.",
)
def eliminar_producto(producto_id: int):
    """
    DELETE: primero verifica que el id exista (si no, error 404),
    luego elimina la fila correspondiente de la tabla.
    """
    conexion = sqlite3.connect(DB_NAME)
    cursor = conexion.cursor()
    cursor.execute("SELECT id FROM productos WHERE id = ?", (producto_id,))
    existe = cursor.fetchone()

    if not existe:
        conexion.close()
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    cursor.execute("DELETE FROM productos WHERE id = ?", (producto_id,))
    conexion.commit()
    conexion.close()
    return {"mensaje": f"Producto {producto_id} eliminado"}


@app.get(
    "/productos",
    tags=["Productos"],
    summary="Listar productos",
    description="Devuelve todos los productos guardados en la tabla. Útil para verificar insert/update/delete.",
)
def listar_productos():
    """GET: consulta todas las filas de la tabla 'productos' y las devuelve como lista de JSON."""
    conexion = sqlite3.connect(DB_NAME)
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre, precio FROM productos")
    filas = cursor.fetchall()
    conexion.close()
    return [{"id": f[0], "nombre": f[1], "precio": f[2]} for f in filas]

