#Necesitamos una variable llamada app
#que será la de ejecución de nuestro Api
#Dicha variable será de tipo FastApi()
from typing import Union

from fastapi import FastAPI
app = FastAPI()

#DEBEMOS DECORAR EL METODO CON UN TIPO DE METODO Y UN ENDPOINT 
#DE ACCESO PARA EL API
@app.get("/")
#CREAMOS UN NUEVO METODO QUE REALICE COSAS
def metodoRoot():
    #Este método puede hacer de todo: Bucles, condicionales
    #Si el método es para un Api EndPoint necesitamos siempre
    #devolver una respuesta
    return { "data": "Mi primer FastApi, que ilusión" }

@app.get("/saludo")
def metodoSaludo():
    return {"data": "Bienvenido/a a mi FastApi"}

@app.get("/doblemapping/{numero}")
def getNumeroDoble(numero: int, mensaje: str):
    #INTERNAMENTE NO ES NECESARIO EL TIPADO
    doble: int = numero * 2
    return {"doble": doble, 
            "mensaje": mensaje}

@app.get("/saludito")
def dameSaludito(nombre: str
                 , aficion: Union[str, None] = None):
    return {"saludo": "Hola holita " + nombre,
            "Aficion":  aficion}
    
@app.get("/numeros")
def dameNumeros():
    listaNumeros = [45, 55, 22, 10, 14]
    return {"numeros": listaNumeros}

    
