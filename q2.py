def CheckValidGame(string:str):
    id = int(string.split(":")[0].lower().replace("game ",""))
    GameStrings = string.replace("Game " + str(id) + ": ", "").split(";")
    for line in GameStrings:
        red =-1
        blue=-1
        green=-1
        for color in line.split(","):
            if "red" in color:
                red = int(color.replace("red","").replace(" ",""))
            elif "blue" in color:
                blue = int(color.replace("blue","").replace(" ",""))
            elif "green" in color:
                green = int(color.replace("green","").replace(" ",""))
        if (red >12 or blue >14 or green >13):
            return 0
    return id


def CheckMultiGame(string:str):
    id = int(string.split(":")[0].lower().replace("game ",""))
    GameStrings = string.replace("Game " + str(id) + ": ", "").split(";")
    HIGHEST = [-1,-1,-1]
    for line in GameStrings:
        red =-1
        blue=-1
        green=-1
        for color in line.split(","):
            if "red" in color:
                red = int(color.replace("red","").replace(" ",""))
            elif "blue" in color:
                blue = int(color.replace("blue","").replace(" ",""))
            elif "green" in color:
                green = int(color.replace("green","").replace(" ",""))
        if (HIGHEST[0] < red):
            HIGHEST[0] = red
        if (HIGHEST[1] < blue):
            HIGHEST[1] = blue
        if (HIGHEST[2] < green):
            HIGHEST[2] = green
        
    return HIGHEST[0] * HIGHEST[1] * HIGHEST[2]
    

    


def main():
    file = open("input2.txt", "r")
    total = 0
    for line in file:
        print(line)
        hold = CheckMultiGame(line)
        print(hold)
        total += hold
    file.close()
    return total

print(main())
#print(CheckMultiGame("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"))



