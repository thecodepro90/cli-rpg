import logger
from db import DB
logger.logger_init()

class Sprite:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name
        
        
        
player1 = Sprite(2, 3, "Jane Doe")    
levels = DB("levels", 0)
levels.create_table("player_map")
levels.create_table("level_map")

class MapController:
    def __init__(self, map):
        self.map = map

    def get_map(self):
        return self.map
    
    def get_value(self, x, y):
        return self.map[y][x]
    
    def set_value(self, x, y, value):
        self.map[y][x] = value
        


level_map = [
    ["0","0","0","0","0","0"],
    ["0","0","0","|","0","0"],
    ["0","0","0","|","0","0"],
    ["0","0","0","|","0","0"],
    ["0","0","0","0","0","0"],
    ["0","0","0","0","0","0"],
]

player_map = [
    ["0","0","0","0","0","0"],
    ["0","0","0","0","0","0"],
    ["0","0","0","0","0","0"],
    ["0","0","0","0","0","0"],
    ["0","0","0","0","0","0"],
    ["0","0","0","0","0","0"],
]
levels.append("player_map", str(player_map))
logger.log(str(player_map))

player_map_controller = MapController(player_map)
level_map_controller = MapController(level_map)

try:
    while True:
        print("\n\n\n\n\n\n")
        logger.log(f"X: {player1.x} Y:{player1.y}")
        print()

        if player1.x == 6:
            player1.x -= 1
        elif player1.x == -1:
            player1.x += 1

        if player1.y == -1:
            player1.y += 1

        if player1.y == 6:
            player1.y -= 1
        
        for y in range(6):
            for x in range(6):
                if level_map_controller.get_value(x, y) != "0":
                    player_map_controller.set_value(x, y, level_map_controller.get_value(x, y))
                
        player_map_controller.set_value(player1.x, player1.y, "1")
        for i in player_map_controller.get_map():
            for j in i:
                print(j+" ", end="")
            print()




        move = input(": ")
            
        if move == "w":
            player_map_controller.set_value(player1.x, player1.y, level_map_controller.get_value(player1.x, player1.y))
            player1.y -= 1
            logger.log("W KEY PRESSED")
            
        elif move == "a":
            player_map_controller.set_value(player1.x, player1.y, level_map_controller.get_value(player1.x, player1.y))
            player1.x -= 1
            logger.log("A KEY PRESSED")
        elif move == "s":
            player_map_controller.set_value(player1.x, player1.y, level_map_controller.get_value(player1.x, player1.y))
            player1.y += 1
            logger.log("S KEY PRESSED")
        elif move == "d":
            player_map_controller.set_value(player1.x, player1.y, level_map_controller.get_value(player1.x, player1.y))
            player1.x += 1
            logger.log("D KEY PRESSED")
except:
    logger.log("PROGRAM EXIT")
        
    
    
        



