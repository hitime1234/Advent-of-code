import re
def getNums(string:str):

    return re.sub('\D', '', string)

def FindDigitName(string:str):
    string = string.lower()
    string = string.replace("one", "one1one")
    string = string.replace("two", "two2two")
    string = string.replace("three", "three3three")
    string = string.replace("four", "four4four")
    string = string.replace("five", "five5five")
    string = string.replace("six", "six6six")
    string = string.replace("seven", "seven7seven")
    string = string.replace("eight", "eight8eight")
    string = string.replace("nine", "nine9nine")
    return string
    

    

def GetLineValue(string:str):
    hold = getNums(string)
    if (len(hold) == 1):
        return int(str(hold) + str(hold))
    elif (len(hold) == 2):
        return int(hold)
    elif (len(hold) >= 3):
        return int(str(hold)[0] +str(hold)[len(hold)-1])
    
    



def main():
    total = 0
    file = open("input.txt", "r")
    for line in file:
        total += GetLineValue(FindDigitName(line))
        print(GetLineValue(FindDigitName(line)))
        print(line)
    file.close()



    return total



print(main())