#Necesitamos una variable llamada app
#que será la de ejecución de nuestro Api
#Dicha variable será de tipo FastApi()
from typing import Union
from fastapi import FastAPI, Depends
from fastapi.encoders import jsonable_encoder
#Agregamos la librería para utilizar BaseModel
from pydantic import BaseModel
import services.ServiceJugadores as servicio
#Recuperamos la librería de objetos JSON
import json
#DEBEMOS HACER REFERENCIA A NUESTRO CONTROLLER Y SU router
from controllers.DatosController import router as router_controller
from controllers.JugadoresController import router as router_jugadores

def dependencia1(token: str):
    print("Dependencia Global 1: " + token)

def dependencia2():
    print("Dependencia Global 2")

app = FastAPI(dependencies=[Depends(dependencia1), Depends(dependencia2)])

app.include_router(router_jugadores, prefix="/api", tags=["jugadores"])
#POSTERIORMENTE, AGREGAMOS NUESTRO CONTROLLER A LA APLICACION
#Sintaxis si deseamos integrar TODO dentro del Controller principal
#app.include_router(router_controller)
#Si deseamos separar los controller por NAME y EndPoint debemos indicar
#en la agregación del Router, el prefix del Endpoint y el nombre del Controller
app.include_router(router_controller, prefix="/api", tags=["Datos"])




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



    
