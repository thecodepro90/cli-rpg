class Sprite:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name
        
player1 = Sprite(0, 0, "Jane Doe")        

map = [
    ["0","0","0","0","0","0"],
    ["0","0","0","0","0","0"],
    ["0","0","0","0","0","0"],
    ["0","0","0","0","0","0"],
    ["0","0","0","0","0","0"],
    ["0","0","0","0","0","0"],
]

map[player1.y][player1.x] = "1"

while True:
    print("\n\n\n\n\n\n")
    print(player1.x, player1.y)
    map[abs(player1.y)][abs(player1.x)] = "1"
    p_map = ""
    for i in map:
        for j in i:
            p_map += j+"  "
        p_map += "\n"
    print(p_map)
    move = input(": ")
        
    if move == "w":
        player1.y += 1
    elif move == "a":
        player1.x -= 1
    elif move == "s":
        player1.y -= 1
    elif move == "d":
        player1.x += 1
        
    
    
        



