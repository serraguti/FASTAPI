from pydantic import BaseModel

class Player(BaseModel):
    id: int = 0
    nombre: str = ""
    posicion: str= ""
    edad: int = 0
    imagen: str = ""