from fastapi import APIRouter, HTTPException, Depends
import services.ServiceJugadores as servicio
from models.Player import Player
from utils.responsewrapper import apiResponse
router = APIRouter()

def parametrosDepends(inicio:int = 0, fin: int = 100):
    #aqui hacemos todo lo necesario con los parametros
    return {"inicio": inicio, "fin": fin}

@router.get("/players")
def readPlayers():
    players = servicio.getPlayers()
    return apiResponse(data=players, message="All players OK")

@router.get("/find/{id}")
def findPlayer(id: int):
    player = servicio.findPlayer(id)
    if (player is None):
        raise HTTPException(status_code=404,detail=f"Player not found {id}")
    return apiResponse(data=player)

@router.get("/filteredad/{edad}")
def jugadoresEdad(edad: int, commons: dict = Depends(parametrosDepends)):
    players = servicio.searchPlayersAge(edad, commons["inicio"], commons["fin"])
    return apiResponse(data=players)

@router.get("/filterposicion/{posicion}")

def jugadoresEdad(posicion: str, commons: dict = Depends(parametrosDepends)):
    players = servicio.searchPlayersPosition(posicion, commons["inicio"], commons["fin"])
    return apiResponse(data=players)

@router.get("/filterplayers")
def filterPlayers(commons: dict = Depends(parametrosDepends)):
    players = servicio.filterPlayers(commons["inicio"], commons["fin"])
    return apiResponse(data=players)