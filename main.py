

# Importing files and things
import tkinter as tk
file1 = open("res/pokedex.csv", "r")
file2 = open("res/pokemon_types.csv", "r")
file3 = open("res/type_efficacy.csv", "r")


# Defining Window variables
window = tk.Tk()
window.title("PKMN Type Matchup Calculator")
window.geometry("1920x1080")

# Defining pokemon name entry boxes
entry1_var = tk.StringVar()
entry2_var = tk.StringVar()
entry3_var = tk.StringVar()
entry4_var = tk.StringVar()
entry5_var = tk.StringVar()
entry6_var = tk.StringVar()


# Scrubbing the Files

# List of Pokemon
pokeList = []
for line in file1:
    pokeList.append(line.split("\n")[0])
pokeList.remove(pokeList[0])

# List of Pokemon #s and types
typeList = []
for line in file2:
    typeList.append(line.split("\n")[0])
typeList.remove(typeList[0])

# List of Pokemon types and damage output
typeAdv = []
for line in file3:
    typeAdv.append(line.split("\n")[0])
typeAdv.remove(typeAdv[0])

# Find Pokemon from the list
def getPokemon(name):
     dexNum = ""
     x = 0
     while dexNum == "":
        curr_line = str(pokeList[x])
        curr_slice = curr_line.split(",")
        if(curr_slice[0] == str(name).lower()):
            dexNum = curr_slice[1]
            return dexNum
        x+=1
        if(x == len(pokeList)):
            dexNum = 0
     return dexNum

# Find a Pokemon's type
# The Types are listed in the source material thus:
"""
1 = Normal type
2 = Fighting
3 = Flying
4 = Poison
5 = Ground
6 = Rock
7 = Bug
8 = Ghost
9 = Steel
10 = Fire
11 = Water
12 = Grass
13 = Electric
14 = Psychic
15 = Ice
16 = Dragon
17 = Dark
18 = Fairy
0 = Not Found
"""
def getType(dex)->list[str]:
    x=0
    typeNum = []
    while x < len(typeList)-1:
        curr_line = str(typeList[x])
        curr_slice = curr_line.split(",")
        if(curr_slice[0] == str(dex)):
            typeNum.append(curr_slice[1])
        x+=1
        if(x == len(typeList)):
            return ["NULL"]
    return typeNum   


def getIndexType(typeNum)->int:
    x=0 
    while x < len(typeAdv)-1:
        curr_split = typeAdv[x].split(",")
        if(typeNum == curr_split[0]):
            return x
        x+=1
    return 0
def isAdvantageous(attack, defense)->bool:
    x=0
    while x < len(typeAdv)-1:
        curr_split = typeAdv[x].split(",")
        if(curr_split[0] == attack and curr_split[1] == defense):
            if(curr_split[2] > "100"):
                return True
        x+=1
    return False
def isDisadvantageous(attack, defense)->bool:
    x=0
    while x < len(typeAdv)-1:
        curr_split = typeAdv[x].split(",")
        if(curr_split[0] == attack and curr_split[1] == defense):
            if(curr_split[2] == "50"):
                return True
        x+=1
    return False
def isIneffective(attack, defense)->bool:
    x=0
    while x < len(typeAdv)-1:
        curr_split = typeAdv[x].split(",")
        if(curr_split[0] == attack and curr_split[1] == defense):
            if(curr_split[2] == "0"):
                return True
        x+=1
    return False

# Takes in the Pokedex entry number and outputs the type data ascribed to it
def generateTypeChart(dexNum, chartType)->list[str]:
    typeChart=[]
    if(chartType == "a"):
        pType = getType(dexNum)
        type1 = str(pType[0])
        if(len(pType) < 2):
            for type in typeAdv:
                curr_split = type.split(",") 

                if(curr_split[0] == type1):
                    typeChart.append((f"%s,"%curr_split[1]+f"%s"%curr_split[2]))
        else:
            #does other things
            type2 = str(pType[1])
            typeChart=[]
            x=0
            y=0
            index1=getIndexType(type1)
            index2=getIndexType(type2)
            advList = []
            while x < len(typeAdv):
                curr_split = typeAdv[x].split(",")
                if(curr_split[1]==pType[0] or curr_split[1] == pType[1]):
                    if(isAdvantageous(curr_split[0],curr_split[1])):
                        typeChart.append(f"%s,150"%curr_split[0])
                    if(isDisadvantageous(curr_split[0], curr_split[1])):
                        typeChart.append((f"%s,50"%curr_split[0]))
                    else:
                        typeChart.append(f"%s,0"%curr_split[0])

                y+=1
                x+=19
                if(y==18): y=0
    else:
        pType = getType(dexNum)
        #things and stuff

    return typeChart
def returnType(typeNum)->str:
    match typeNum:
        case "1": 
            return "Normal"
        case "2":
            return "Fighting"
        case "3":
            return "Flying"
        case "4":
            return "Poison"
        case "5":
            return "Ground"
        case "6":
            return "Rock"
        case "7":
            return "Bug"
        case "8":
            return "Ghost"
        case "9":
            return "Steel"
        case "10":
            return "Fire"
        case "11":
            return "Water"
        case "12":
            return "Grass"
        case "13":
            return "Electric"
        case "14":
            return "Psychic"
        case "15":
            return "Ice"
        case "16":
            return "Dragon"
        case "17":
            return "Dark"
        case "18": 
            return "Fairy"
    return "DNF"
"""
1 = Normal type
2 = Fighting
3 = Flying
4 = Poison
5 = Ground
6 = Rock
7 = Bug
8 = Ghost
9 = Steel
10 = Fire
11 = Water
12 = Grass
13 = Electric
14 = Psychic
15 = Ice
16 = Dragon
17 = Dark
18 = Fairy
0 = Not Found
"""
def returnEffectiveness(attackVal)->str:
    match attackVal:
        case "200":
            return "Super "
        case "150":
            return "Advantageous "
        case "100":
            return "Normal "
        case "50":
            return "Reduced "
        case "0":
            return "No "
    return "DNF"

# On-click "submit" function that runs the engine with the input
def submit():
    error = 0
    # Initialize the entry name variables
    entry1=entry1_var.get()
    entry2=entry2_var.get()
    entry3=entry3_var.get()
    entry4=entry4_var.get()
    entry5=entry5_var.get()
    entry6=entry6_var.get()
    
    # Check the Database for matching names, on error return "DNF"
    pkmn1 = [getPokemon(entry1)]
    if(pkmn1[0] == "NULL"):
        text.insert("1.0", f"Could not find: %s.\n" % entry1)
        error = 1
    pkmn2 = [getPokemon(entry2)]
    if(pkmn2[0] == "NULL"):
        text.insert("1.0", f"Could not find: %s.\n" % entry2)
        error = 1
    pkmn3 = [getPokemon(entry3)]
    if(pkmn3[0] == "NULL"):
        text.insert("1.0", f"Could not find: %s.\n" % entry3)
        error = 1
    pkmn4 = [getPokemon(entry4)]
    if(pkmn4[0] == "NULL"):
        text.insert("1.0", f"Could not find: %s.\n" % entry4)
        error = 1
    pkmn5 = [getPokemon(entry5)]
    if(pkmn5[0] == "NULL"):
        text.insert("1.0", f"Could not find: %s.\n" % entry5)
        error = 1
    pkmn6 = [getPokemon(entry6)]
    if(pkmn6[0] == "NULL"):
        text.insert("1.0", f"Could not find: %s.\n" % entry6)
        error = 1
    
    # if a previous error has occurred, the program stops and awaits new input
    if(error == 1):
        return None


    # Assign types to the Pokemon
    pkmnType = getType(str(pkmn1[0]))
    if(pkmnType == []):
        print("1.0", f"Type for %s does not exist.\n" % str(entry1))
        error=1
    else:
        pkmn1.append(pkmnType[0])
        if(len(pkmnType) == 2):
            pkmn1.append(pkmnType[1])

    pkmnType = getType(str(pkmn2[0]))
    if(pkmnType == []):
        text.insert("1.0", f"Type for %s does not exist.\n" % str(entry2))
        error=1
    else:
        pkmn2.append(pkmnType[0])
        if(len(pkmnType) == 2):
            pkmn2.append(pkmnType[1])
    pkmnType = getType(str(pkmn3[0]))
    if(pkmnType == []):
        text.insert("1.0", f"Type for %s does not exist.\n" % str(entry3))
        error=1
    else:
        pkmn3.append(pkmnType[0])
        if(len(pkmnType) == 2):
            pkmn3.append(pkmnType[1])
    pkmnType = getType(str(pkmn4[0]))
    if(pkmnType == []):
        text.insert("1.0", f"Type for %s does not exist.\n" % str(entry4))
        error=1
    else:
        pkmn4.append(pkmnType[0])
        if(len(pkmnType) == 2):
            pkmn4.append(pkmnType[1])
    pkmnType = getType(str(pkmn5[0]))
    if(pkmnType == []):
        text.insert("1.0", f"Type for %s does not exist.\n" % str(entry5))
        error=1
    else:
        pkmn5.append(pkmnType[0])
        if(len(pkmnType) == 2):
            pkmn5.append(pkmnType[1])
    pkmnType = getType(str(pkmn6[0]))
    if(pkmnType == []):
        text.insert("1.0", f"Type for %s does not exist.\n" % str(entry6))
        error=1
    else:
        pkmn6.append(pkmnType[0])
        if(len(pkmnType) == 2):
            pkmn6.append(pkmnType[1])
    #if a previous error has occurred, the program stops and awaits new input
    if(error == 1):
        return None

    # "get individual type charts" function calls
    text.insert("2.0", "Attack Charts for your team: \n")
    pkmn1_attack_profile = generateTypeChart(pkmn1[0], "a")
    output = ""
    if(len(pkmn1) > 2):
        output +=(f"For pokemon %s "%entry1 + "of type(s)" + returnType(pkmn1[1][0]) + " and " + returnType(pkmn1[1][1]) + ":\n")
    else:
        output +=(f"For pokemon %s "%entry1 + "of type(s)" + returnType(pkmn1[1]) + ":\n")
    for val in pkmn1_attack_profile:
        curr_split = val.split(",")
        output += "Attacks against " + returnType(curr_split[0]) + " are " + returnEffectiveness(curr_split[1]) + "effectiveness.\n"
    pkmn2_attack_profile = generateTypeChart(pkmn2[0], "a")
    if(len(pkmn2) > 2):
        output +=(f"For pokemon %s "%entry2 + "of type(s)" + returnType(pkmn2[1][0]) + " and " + returnType(pkmn2[1][1]) + ":\n")
    else:
        output +=(f"For pokemon %s "%entry2 + "of type(s)" + returnType(pkmn2[1]) + ":\n")
    for val in pkmn2_attack_profile:
        curr_split = val.split(",")
        output += "Attacks against " + returnType(curr_split[0]) + " are " + returnEffectiveness(curr_split[1]) + "effectiveness.\n"
    pkmn3_attack_profile = generateTypeChart(pkmn3[0], "a")
    if(len(pkmn3) > 2):
        output +=(f"For pokemon %s "%entry3 + "of type(s)" + returnType(pkmn3[1][0]) + " and " + returnType(pkmn3[1][1]) + ":\n")
    else:
        output +=(f"For pokemon %s "%entry3 + "of type(s)" + returnType(pkmn3[1]) + ":\n")
    for val in pkmn3_attack_profile:
        curr_split = val.split(",")
        output += "Attacks against " + returnType(curr_split[0]) + " are " + returnEffectiveness(curr_split[1]) + "effectiveness.\n"
    pkmn4_attack_profile = generateTypeChart(pkmn4[0], "a")
    if(len(pkmn4) > 2):
        output +=(f"For pokemon %s "%entry4 + "of type(s)" + returnType(pkmn4[1][0]) + " and " + returnType(pkmn4[1][1]) + ":\n")
    else:
        output +=(f"For pokemon %s "%entry4 + "of type(s)" + returnType(pkmn4[1]) + ":\n")
    for val in pkmn4_attack_profile:
        curr_split = val.split(",")
        output += "Attacks against " + returnType(curr_split[0]) + " are " + returnEffectiveness(curr_split[1]) + "effectiveness.\n"
    pkmn5_attack_profile = generateTypeChart(pkmn5[0], "a")
    if(len(pkmn5) > 2):
        output +=(f"For pokemon %s "%entry5 + "of type(s)" + returnType(pkmn5[1][0]) + " and " + returnType(pkmn5[1][1]) + ":\n")
    else:
        output +=(f"For pokemon %s "%entry5 + "of type(s)" + returnType(pkmn5[1]) + ":\n")
    for val in pkmn5_attack_profile:
        curr_split = val.split(",")
        output += "Attacks against " + returnType(curr_split[0]) + " are " + returnEffectiveness(curr_split[1]) + "effectiveness.\n"
    pkmn6_attack_profile = generateTypeChart(pkmn6[0], "a")
    if(len(pkmn6) > 2):
        output +=(f"For pokemon %s "%entry6 + "of type(s)" + returnType(pkmn6[1][0]) + " and " + returnType(pkmn6[1][1]) + ":\n")
    else:
        output +=(f"For pokemon %s "%entry6 + "of type(s)" + returnType(pkmn6[1]) + ":\n")
    for val in pkmn6_attack_profile:
        curr_split = val.split(",")
        output += "Attacks against " + returnType(curr_split[0]) + " are " + returnEffectiveness(curr_split[1]) + "effectiveness.\n"
    text.insert("3.0", output)
    #pkmn1_defense_profile = generateTypeChart(pkmn1[1], "d")
    #TODO Insert the "Compare team type coverages" function calls

    #TODO Insert the findings into a text box like below
    #text.insert("1.0", "We got: " + str(entry1) + ", " + str(entry2) + ", " + str(entry3) + ", " + str(entry4) + ", " + str(entry5) + ", " + str(entry6))
    # call functions here...
    text.insert("1.0", "Your Results are as follows: \n")
    return None



label = tk.Label(window, text="For epic type matchups epically for epic people only (you).\nFor those of you trying to pick a specific variant, please include hyphens.\nFor example: `pikachu-alola`")
label.pack()
button = tk.Button(window, text="Quit", command = window.destroy)
button.pack()

entry1 = tk.Entry(window, textvariable = entry1_var)
entry1.pack()
entry2 = tk.Entry(window, textvariable = entry2_var)
entry2.pack()
entry3 = tk.Entry(window, textvariable = entry3_var)
entry3.pack()
entry4 = tk.Entry(window, textvariable = entry4_var)
entry4.pack()
entry5 = tk.Entry(window, textvariable = entry5_var)
entry5.pack()
entry6 = tk.Entry(window, textvariable = entry6_var)
entry6.pack()

entryButton = tk.Button(window, text="Enter", command = submit)
entryButton.pack()

text = tk.Text(window, height=1000, width=1000)
text.pack()

    

window.mainloop()
