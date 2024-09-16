class Sprite:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name
        
player1 = Sprite(2, 3, "Jane Doe")    


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
    ["0","0","0","0","0","0"],
    ["0","0","0","0","0","0"],
    ["0","0","0","0","0","0"],
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

player_map_controller = MapController(player_map)
level_map_controller = MapController(level_map)

while True:
    print("\n\n\n\n\n\n")
    print(player1.x, player1.y)
    print(level_map)
    print(player_map)
    print()
    player_map_controller.set_value(player1.x, player1.y, "1")

    for i in player_map_controller.get_map():
        for j in i:
            print(j+" ", end="")
        print()

    print(level_map)
    print(player_map)



    move = input(": ")
        
    if move == "w":
        player_map_controller.set_value(player1.x, player1.y, level_map_controller.get_value(player1.x, player1.y))
        player1.y -= 1
        
    elif move == "a":
        player_map_controller.set_value(player1.x, player1.y, level_map_controller.get_value(player1.x, player1.y))
        player1.x -= 1
    elif move == "s":
        player_map_controller.set_value(player1.x, player1.y, level_map_controller.get_value(player1.x, player1.y))
        player1.y += 1
    elif move == "d":
        player_map_controller.set_value(player1.x, player1.y, level_map_controller.get_value(player1.x, player1.y))
        player1.x += 1
        
    
    
        



