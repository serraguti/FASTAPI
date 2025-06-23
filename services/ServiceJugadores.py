import json
from models.Player import Player

def getPlayers():
    info = open("./data/jugadores.json")
    json_data = json.load(info)
    #Creamos una lista/colección de Salida
    salida = []
    #Recorremos todos los jugadores
    for row in json_data["jugadores"]:
        player: Player = Player()
        player.id = int(row["numero"])
        player.nombre = row["nombre"]
        player.posicion = row["posicion"]
        player.edad = int(row["edad"])
        salida.append(player)
    return salida

def findPlayer(idPlayer: int):
    info = open("./data/jugadores.json")
    json_data = json.load(info)
    #CODIGO PARA BUSCAR UN JUGADOR POR ID
    for jugador in json_data["jugadores"]:
        if jugador["numero"] == idPlayer:
            player: Player = Player()
            player.id = int(jugador["numero"])
            player.nombre = jugador["nombre"]
            player.posicion = jugador["posicion"]
            player.edad = int(jugador["edad"])
            return player