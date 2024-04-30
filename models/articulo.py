
from datetime import datetime
from pydantic import BaseModel

class Articulo(BaseModel):
    id: int
    titulo: str
    autor: str
    contenido: str
    creado: str
    categoria: str



    

    
    
    
