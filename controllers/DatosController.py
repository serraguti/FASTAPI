from fastapi import APIRouter

#creamos un objeto que lo utilizaremos posteriormente
#dentro de nuestra clase main
router = APIRouter()

#este objeto crea los metodos
@router.get("/pruebas")
def misPruebas():
    return {"data", "haciendo pruebas Controller"}

@router.get("/pruebas/{dato}")
def pruebasDato(dato: str):
    return {"data", "Recibiendo dato en controller " + dato}