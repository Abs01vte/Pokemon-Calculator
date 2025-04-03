

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
        # Some pokemon have one type
        if(len(pType) < 2):
            for type in typeAdv:
                curr_split = type.split(",") 

                if(curr_split[0] == type1):
                    if(curr_split[2]!="100"):
                        typeChart.append((f"%s,"%curr_split[1]+f"%s"%curr_split[2]))
                        
                    else:
                        pass
        # Or they have two
        else:
            #does other things
            for val in typeAdv:
                curr_split = val.split(",")
                if(curr_split[0] == pType[0] or curr_split[0] == pType[1]):
                    if(curr_split[2] != "100"):
                        typeChart.append(f"%s,"%curr_split[1] + f"%s"%curr_split[2])
                    else:
                        pass
    # Or it is a defensive chart
    elif(chartType == "d"):
        pType = getType(dexNum)
        #things and stuff
        
        # check for one or two type
        if(len(pType) < 2):
            for val in typeAdv:
                curr_split = val.split(",")
                if(curr_split[1] == pType[0]):
                    if(curr_split[2] != "100"):
                        typeChart.append(f"%s,"%curr_split[0] + f"%s"%curr_split[2])
                    else:
                        typeChart.append(f"%s,"%curr_split[0]+f"%s"%curr_split[2])
        # it is a two type
        else:
            for val in typeAdv:
                curr_split = val.split(",")
                if(curr_split[1] == str(pType[0]) or curr_split[1] == str(pType[1])):
                    if(curr_split[2] != "100"):
                        typeChart.append(f"%s,"%curr_split[0] + f"%s"%curr_split[2])
                    else:
                        pass
    return typeChart
def compareCharts(attackChart, defenseChart)->list[str]:

    # Generate a chart that displays advantage positively and disadvantage negatively, but normal is 0
    attackStrengths = []
    x=18
    while x > 0:
        attackStrengths.append(0)
        x-=1
    # Generate a chart that displays advantage (for attacker) negatively, and disadvantage positively, but normal is 0
    defenseStrengths = []
    x=18
    while x > 0:
        defenseStrengths.append(0)
        x-=1
    # Populate the attacking chart with the information gained from the matrix of team type advantages and disadvantages
    for val in attackChart:
        for sub in val:
            curr_split=sub.split(",")
            if(curr_split[1] == "200"):
                attackStrengths[int(curr_split[0])-1] = attackStrengths[int(curr_split[0])-1] + 1
            else:
                pass        
    # Populate the defending chart with the information gained from the matrix of team type advantages and disadvantages
    for val in defenseChart:
        for sub in val:
            curr_split=sub.split(",")
            if(curr_split[1] == "200"):
                defenseStrengths[int(curr_split[0])-1] = defenseStrengths[int(curr_split[0])-1] - 1
            elif(curr_split[1] == "50" or curr_split[1] == "0"):
                defenseStrengths[int(curr_split[0])-1] = defenseStrengths[int(curr_split[0])-1] + 1
    # Combine the two sets of data into a comma separated value list
    x=0
    chartComparison = []
    while x < 18:
        chartComparison.append(f"%s,"%attackStrengths[x] + f"%s"%defenseStrengths[x])
        x+=1
    return chartComparison
    
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
def returnPokemon(dexNum)->str:
    for val in pokeList:
        curr_split = val.split(",")
        if(int(curr_split[1]) == dexNum):
            return curr_split[0]
    return None
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
    if(pkmn1[0] == 0):
        text.insert("1.0", f"Could not find: %s.\n" % entry1)
        error = 1
    pkmn2 = [getPokemon(entry2)]
    if(pkmn2[0] == 0):
        text.insert("1.0", f"Could not find: %s.\n" % entry2)
        error = 1
    pkmn3 = [getPokemon(entry3)]
    if(pkmn3[0] == 0):
        text.insert("1.0", f"Could not find: %s.\n" % entry3)
        error = 1
    pkmn4 = [getPokemon(entry4)]
    if(pkmn4[0] == 0):
        text.insert("1.0", f"Could not find: %s.\n" % entry4)
        error = 1
    pkmn5 = [getPokemon(entry5)]
    if(pkmn5[0] == 0):
        text.insert("1.0", f"Could not find: %s.\n" % entry5)
        error = 1
    pkmn6 = [getPokemon(entry6)]
    if(pkmn6[0] == 0):
        text.insert("1.0", f"Could not find: %s.\n" % entry6)
        error = 1
    
    # if a previous error has occurred, the program stops and awaits new input
    if(error == 1):
        return None


    # Assign types to the Pokemon
    pkmnType = getType(str(pkmn1[0]))
    if(pkmnType == []):
        text.insert("1.0", f"Type for %s does not exist.\n" % str(entry1))
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

    # Generate Attack Efficacy charts
    pkmn1_attack_profile = generateTypeChart(pkmn1[0], "a")
    pkmn2_attack_profile = generateTypeChart(pkmn2[0], "a")
    pkmn3_attack_profile = generateTypeChart(pkmn3[0], "a")
    pkmn4_attack_profile = generateTypeChart(pkmn4[0], "a")
    pkmn5_attack_profile = generateTypeChart(pkmn5[0], "a")
    pkmn6_attack_profile = generateTypeChart(pkmn6[0], "a")
    if(pkmn1_attack_profile == [] or pkmn2_attack_profile == [] or pkmn3_attack_profile == [] or pkmn4_attack_profile == [] or pkmn5_attack_profile == [] or pkmn6_attack_profile == []):
        text.insert("1.0", "Something went wrong... attack")
        return None
    # Generate Defense Efficacy charts
    pkmn1_defense_profile = generateTypeChart(pkmn1[0], "d")
    if(pkmn1_defense_profile == []):
        text.insert("1.0", f"Something went wrong... defense chart for %s"%returnPokemon(pkmn1[0]))
        return None
    pkmn2_defense_profile = generateTypeChart(pkmn2[0], "d")
    if(pkmn2_defense_profile == []):
        text.insert("1.0", f"Something went wrong... defense chart for %s"%returnPokemon(pkmn2[0]))
        return None
    pkmn3_defense_profile = generateTypeChart(pkmn3[0], "d")
    if(pkmn3_defense_profile == []):
        text.insert("1.0", f"Something went wrong... defense chart for %s"%returnPokemon(pkmn3[0]))
        return None
    pkmn4_defense_profile = generateTypeChart(pkmn4[0], "d")
    if(pkmn4_defense_profile == []):
        text.insert("1.0", f"Something went wrong... defense chart for %s"%returnPokemon(pkmn4[0]))
        return None
    pkmn5_defense_profile = generateTypeChart(pkmn5[0], "d")
    if(pkmn5_defense_profile == []):
        text.insert("1.0", f"Something went wrong... defense chart for %s"%returnPokemon(pkmn5[0]))
        return None
    pkmn6_defense_profile = generateTypeChart(pkmn6[0], "d")    
    if(pkmn6_defense_profile == []):
        text.insert("1.0", f"Something went wrong... defense chart for %s"%returnPokemon(pkmn6[0]))
        return None
    # Compare team advantages and weaknesses
    team_attack_profile = []
    team_attack_profile.append(pkmn1_attack_profile)
    team_attack_profile.append(pkmn2_attack_profile)
    team_attack_profile.append(pkmn3_attack_profile)
    team_attack_profile.append(pkmn4_attack_profile)
    team_attack_profile.append(pkmn5_attack_profile)
    team_attack_profile.append(pkmn6_attack_profile)
    team_defense_profile = []
    team_defense_profile.append(pkmn1_defense_profile)
    team_defense_profile.append(pkmn2_defense_profile)
    team_defense_profile.append(pkmn3_defense_profile)
    team_defense_profile.append(pkmn4_defense_profile)
    team_defense_profile.append(pkmn5_defense_profile)
    team_defense_profile.append(pkmn6_defense_profile)

    team_profile = compareCharts(team_attack_profile, team_defense_profile)

    # Find the worst performing defense against a certain type

    hardestType = 0
    lowestDefense = 1
    x = 0
    while x < 18:
        curr_split = team_profile[x].split(",")
        if(int(curr_split[1]) < lowestDefense):
            lowestDefense = int(curr_split[1])
            hardestType = x+1
        x+=1
    # Find the best performing attack against a certain type
    x=0
    bestType = 0
    highestAttack = -1
    while x < 18:
        curr_split = team_profile[x].split(",")
        if(int(curr_split[0]) > highestAttack):
            highestAttack = int(curr_split[0])
            bestType = x+1
        x+=1
    bestTypes = []
    worstTypes = []
    x=0
    while x < len(team_profile):
        curr_split = team_profile[x].split(",")
        if(int(curr_split[0]) > 0):
            bestTypes.append(str(x+1) + f",%s"%curr_split[0])
        elif(int(curr_split[1]) < 0):
            worstTypes.append(str(x+1) + f",%s"%curr_split[1])
        x+=1
    

    #Insert the findings into a text box
    text.insert("1.0", "Your team analysis is below: \n")
    if(len(bestTypes) <= 1): 
        text.insert("end", f"Your team's attacks have an advantage against %s type Pokemon.\n"%returnType(str(bestType[0])))
    else:
        typeNames = []
        for num in bestTypes:
            curr_split = num.split(",")
            typeNames.append(returnType(curr_split[0]))
        typeDeclaration = ""
        x = 0

        while(x<len(typeNames)):
            curr_split = typeNames[x].split(",")
            typeDeclaration += (curr_split[0] +  f" at %s occurances\n"%bestTypes[x].split(",")[1])
            x+=1
        text.insert("end", "Your Pokemon have advantages against the types: \n" + typeDeclaration)
    if(len(worstTypes) <= 1): 
        text.insert("end", f"Your team's defenses have a disadvantage against %s type Pokemon.\n"%returnType(str(hardestType)))
    else:
        typeNames = []
        for num in worstTypes:
            curr_split = num.split(",")
            typeNames.append(returnType(curr_split[0]))
        typeDeclaration = ""
        x = 0
        while(x<len(typeNames)):
            curr_split = typeNames[x].split(",")
            typeDeclaration = (curr_split[0] +  f" at %d occurances\n"%(int(worstTypes[x].split(",")[1]) * -1))
            x+=1
        text.insert("end","Your Pokemon have disadvantages against the types: " + typeDeclaration)



    # call functions here...
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
