from fastapi import APIRouter
import services.ServiceJugadores as servicio
from models.Player import Player

router = APIRouter()

@router.get("/players")
def readPlayers():
    players = servicio.getPlayers()
    return {"players": players}

@router.get("/find/{id}")
def findPlayer(id: int):
    player = servicio.findPlayer(id)
    return player