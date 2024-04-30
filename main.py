from fastapi import FastAPI
from models.articulo import Articulo
from services.repository import Repository

app = FastAPI()
db = Repository()

@app.get("/articulos")
def get_articulos():
    return db.get_articulos()

@app.get("/articulo/{id}")
def find_articulo(id: int):
    return db.get_articulo(id)

@app.post("/articulo")
def add_articulo(articulo: Articulo):
    return db.add_articulo(articulo)

@app.put("/articulo")
def update_articulo(articulo: Articulo):
    return db.update_articulo(articulo)

@app.delete("/articulo/{id}")
def delete_articulo(id: int):
    return db.delete_articulo(id)




