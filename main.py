#Necesitamos una variable llamada app
#que será la de ejecución de nuestro Api
#Dicha variable será de tipo FastApi()
from typing import Union

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
#Agregamos la librería para utilizar BaseModel
from pydantic import BaseModel

app = FastAPI()

class Dato(BaseModel):
    nombre: str
    cantidad: int

#Creamos un metodo POST/PUT que recibirá el objeto Dato
@app.put("/put")
def updateDato(dato: Dato):
    return {"nombre recibido": dato.nombre, "cantidad": dato.cantidad}

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
    #Vamos a crear un objeto diccionario para cada número
    # Cada objeto que tengamos, lo almacenaremos en la colección de salida
    salida = []
    for num in listaNumeros:
        #Creamos un diccionario para cada numero
        elemento = {"numero": num}
        codificado = jsonable_encoder(elemento)
        salida.append(codificado) 
    return {"numeros": salida}

@app.get("/nombres")
def dameNombres():
    listaNombres = ["Adrian", "Lucia", "Manuel", "Antonia"]
    #Vamos a crear un objeto diccionario para cada número
    # Cada objeto que tengamos, lo almacenaremos en la colección de salida
    salida = []
    for name in listaNombres:
        #Creamos un diccionario para cada numero
        elemento = {"name": name}
        codificado = jsonable_encoder(elemento)
        salida.append(codificado) 
    return {"nombres": salida}


    
