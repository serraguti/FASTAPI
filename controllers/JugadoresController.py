from fastapi import APIRouter, HTTPException
import services.ServiceJugadores as servicio
from models.Player import Player
from utils.responsewrapper import apiResponse
router = APIRouter()

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