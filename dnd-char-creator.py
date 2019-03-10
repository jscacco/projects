import time
import random
import operator

def d4(amt=1):
    counter = 0
    for _ in range(amt):
        counter += random.randint(1,5)
    return counter

def d6(amt=1):
    counter = 0
    for _ in range(amt):
        counter += random.randint(1,6)
    return counter

def d8(amt=1):
    counter = 0
    for _ in range(amt):
        counter += random.randint(1,8)
    return counter

def d10(amt=1):
    counter = 0
    for _ in range(amt):
        counter += random.randint(1,10)
    return counter

def d12(amt=1):
    counter = 0
    for _ in range(amt):
        counter += random.randint(1,12)
    return counter

def d20(amt=1):
    counter = 0
    for _ in range(amt):
        counter += random.randint(1,20)
    return counter

def d100(amt=1):
    counter = 0
    for _ in range(amt):
        counter += random.randint(1,100)
    return counter


def genSheetTemplate():
    """Returns the framework of a character sheet"""
    sheet = {"name" : "Teste",
             "class" : "testicle",
             "level" : 1,
             "background" : None,
             "player name" : None,
             "race" : None,
             "proficiency" : 2,
             "scores" : {"str" :  {"assigned" : False, "val" : 0, "order" : 1, "mod" : 0},
                         "dex" : {"assigned" : False, "val" : 0, "order" : 2, "mod" : 0},
                         "con" : {"assigned" : False, "val" : 0, "order" : 3, "mod" : 0},
                         "int" : {"assigned" : False, "val" : 0, "order" : 4, "mod" : 0},
                         "wis" : {"assigned" : False, "val" : 0, "order" : 5, "mod" : 0},
                         "cha" : {"assigned" : False, "val" : 0, "order" : 6, "mod" : 0}},
             "saves" : {"str" :  0, "dex" : 0, "con" : 0, "int" : 0, "wis" : 0, "cha" : 0},
             "skills" : {"acrobatics" : {"base" : "dex", "mod" : 0, "proficient" : False},
                         "animal handling" : {"base" : "wis", "mod" : 0, "proficient" : False},
                         "arcana" : {"base" : "int", "mod" : 0, "proficient" : False},
                         "athletics" : {"base" : "str", "mod" : 0, "proficient" : False},
                         "deception" : {"base" : "cha", "mod" : 0, "proficient" : False},
                         "history" : {"base" : "int", "mod" : 0, "proficient" : False},
                         "insight" : {"base" : "wis", "mod" : 0, "proficient" : False},
                         "intimidation" : {"base" : "cha", "mod" : 0, "proficient" : False},
                         "investigation" : {"base" : "int", "mod" : 0, "proficient" : False},
                         "medicine" : {"base" : "wis", "mod" : 0, "proficient" : False},
                         "nature" : {"base" : "int", "mod" : 0, "proficient" : False},
                         "perception" : {"base" : "wis", "mod" : 0, "proficient" : False},
                         "performance" : {"base" : "cha", "mod" : 0, "proficient" : False},
                         "persuasion" : {"base" : "cha", "mod" : 0, "proficient" : False},
                         "religion" : {"base" : "int", "mod" : 0, "proficient" : False},
                         "sleight of hand" : {"base" : "dex", "mod" : 0, "proficient" : False},
                         "stealth" : {"base" : "dex", "mod" : 0, "proficient" : False},
                         "survival" : {"base" : "wis", "mod" : 0, "proficient" : False}},
             "combat info" : {"ac" : 0,
                              "initiative" : 0,
                              "speed" : 0,
                              "hp" : 0,
                              "hit dice type" : None,
                              "hit dice amt" : 0},
             "passives" : {"perception" : 0,
                           "investigation" : 0,
                           "insight" : 0},
             "languages" : [],
             "equipment" : {},
             "spellcasting" : {},
             "proficiencies" : {"weapons" : [], "armor" : [], "tools" : []},
             "features" : {},
             "attacks" : {},
             "resistances" : [],
             "recommended" : {}}
    return sheet

def printSheet(sheet):
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("******************************")
    print(sheet["name"] + ", " + sheet["race"] + " " + sheet["class"])

    print("-----------------------------")
    print("Name:\n" + sheet["name"])
    print("-----------------------------")
    print("Class:\n" + sheet["class"])
    print("-----------------------------")  
    print("Background:\n" + sheet["background"])
    print("-----------------------------")  
    print("Race:\n" + sheet["race"])
    print("-----------------------------")  
    #Scores
    print("Scores:" + "\n")
    current = 1
    i = "scores"
    while current < 7:
        for s in sheet[i]:
            if sheet[i][s]["order"] == current:
                if(sheet[i][s]["mod"] >= 0):
                   print(s + ": " + str(sheet[i][s]["val"]) + " (+" + str(sheet[i][s]["mod"]) + ")")
                else:
                     print(s + ": " + str(sheet[i][s]["val"]) + " (" + str(sheet[i][s]["mod"]) + ")")
        current += 1
    print("-----------------------------")
    #Combat info
    i = "combat info"
    print("Combat Info:\n")
    for a in sorted(sheet[i]):
        print(a + ": " + str(sheet[i][a]))
    print("-----------------------------")
    #Saves
    i = "saves"
    print("Saves:\n")
    for s in sheet[i]:
        if(sheet[i][s] >= 0):
            print(s + ": +" + str(sheet[i][s]))
        elif(sheet[i][s] < 0):
            print(s + ": " + str(sheet[i][s]))
    print("-----------------------------")
    if(sheet["resistances"] != []):
        #Resistances
        print("Resistances:")
        i = "resistances"
        for t in range(len(sheet[i])):
            if(t < len(sheet[i]) - 1):
                print(sheet[i][t] + ", ", end='')
            else:       
                print(sheet[i][t])    
        print("-----------------------------")
    #Skills
    i = "skills"
    print("Skills:\n")
    for s in sorted(sheet[i]):
        if(sheet[i][s]["mod"] >= 0):
            print(s + ": " + "(+" + str(sheet[i][s]["mod"]) + ")")
        else:
            print(s + ": " + "(" + str(sheet[i][s]["mod"]) + ")")
    print("-----------------------------")
    #Passives
    i = "passives"
    print("Passives:\n")
    for p in sheet[i]:
        print(p + ": " + str(sheet[i][p]))
    print("-----------------------------")
    #Languages
    i = 'languages'
    print("Languages:\n")
    for t in range(len(sheet[i])):
        if(t < len(sheet[i]) - 1):
            print(sheet[i][t] + ", ", end='')
        else:       
            print(sheet[i][t])
    print("-----------------------------")
    #Attacks
    i = "attacks"
    print("Attacks:\n")
    for a in sorted(sheet[i]):
        print(a + ": " + str(sheet[i][a]))
    print("-----------------------------")
    #Spellcasting
    i = "spellcasting"
    if(sheet[i] != {}):
        print("Spellcasting:\n")
        print("Stats:\nSpell Save DC: " + str(sheet[i]["dc"]) + "\nSpell Attack Modifier: " + str(sheet[i]["mod"]) + "\n")
        
        print("Slots:")
        for s in sheet[i]["slots"]:
            print(s + ": " + str(sheet[i]["slots"][s]))
        print("\nSpells:")
        print("Cantrips: ", end='')
        for n in range(len(sheet[i][0])):
            if(n < len(sheet[i][0]) - 1):
                print(sheet[i][0][n] + ", ", end='')
            else:
                print(sheet[i][0][n])
        print("Level 1: ", end='')
        for n in range(len(sheet[i][1])):
            if(n < len(sheet[i][1]) - 1):
                print(sheet[i][1][n] + ", ",end='')
            else:
                print(sheet[i][1][n])
        print()
        print("-----------------------------")
    #Features
    i = "features"
    print("Features:\n")
    for f in sorted(sheet[i]):
        print(f + " - " + str(sheet[i][f]) + "\n")     
    print("-----------------------------")
    #Proficiencies
    i = "proficiencies"
    print("Proficiencies:\n")
    for p in sheet[i]:
        if(sheet[i][p] != []):
            print(p + ": ", end='')
            for t in range(len(sheet[i][p])):
                if(t < len(sheet[i][p]) - 1):
                    print(sheet[i][p][t] + ", ", end='')
                else:
                    print(sheet[i][p][t])
    print("-----------------------------")
    #Equipment
    i = "equipment"
    print("Equipment:\n")
    for e in sheet[i]:
        if(sheet[i][e] > 1):
            print(e + " (x" + str(sheet[i][e]) + ")")
        else:
            print(e)
    print("-----------------------------")
    print("******************************")
    return

def doASI(sheet, score, amt):
    temp = sheet
    temp["scores"][score]["val"] += amt
    return temp

def chooseOneTool(list):
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("Please choose one of the following to be proficient with: ")
    for i in list:
        print(i)
    chosen = input("")
    if not chosen in list:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("***Please enter a valid choice (capitalization matters). Try again!***")
        time.sleep(3)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        return chooseOneTool(list)
    return chosen

def chooseSubrace(sheet, subraces):
    temp = sheet
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("Please choose a subrace from the following options: ")
    for r in subraces:
        print("-----------------------------")
        print("Subrace: " + r)
        print("\nDescription: " + subraces[r]["desc"])
    print("-----------------------------")

    subrace = input("Which subrace do you want to play as?\n")
    #Check to make sure the input race is valid
    if not subrace in subraces:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("***Please enter a valid subrace (capitalization matters). Try again!***")
        time.sleep(3)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        return chooseSubrace(temp, subraces)
    else:
        #Update race
        temp["race"] = subrace
        #Update speed
        if "speed" in subraces[subrace]:
            temp["combat info"]["speed"] = subraces[subrace]["speed"]
        #Update ability scores
        for score in subraces[subrace]["asi"]:
            temp = doASI(temp, score, subraces[subrace]["asi"][score])
        #Update resistances
        if "resistances" in subraces[subrace]:
            sheet["resistances"].extend(subraces[subrace]["resistances"])
        #Update features
        if("features" in subraces[subrace]):
            temp["features"].update(subraces[subrace]["features"])
        #Add 1 to hp max if the character is a dwarf
        if(subrace == "hill dwarf"):
            temp["combat info"]["hp"] += 1
        #Update proficiencies
        if("proficiencies" in subraces[subrace]):
            #Update weapon proficiencies
            if "weapons" in subraces[subrace]["proficiencies"]:
                temp["proficiencies"]["weapons"].extend(subraces[subrace]["proficiencies"]["weapons"])
            #Update armor proficiencies
            if "armor" in subraces[subrace]["proficiencies"]:
                temp["proficiencies"]["armor"].extend(subraces[subrace]["proficiencies"]["armor"])
            #Update tool proficiencies
            if "tools" in subraces[subrace]["proficiencies"]:
                for t in subraces[subrace]["proficiencies"]["tools"]:
                    if(t == "choose one"):
                        chosen = chooseOneTool(subraces[subrace]["proficiencies"]["tools"][t])
                        temp["proficiencies"]["tools"].extend([chosen])
                    else:
                        temp["proficiencies"]["tools"].extend([t])
        return temp

def chooseDraconicAncestry(sheet):
    """Chooses a draconic ancestry and updates the sheet accordingly.  Should only be called for dragonborn."""
    temp = sheet
    ancestry = {"black" : {"type" : "acid", "weapon" : "5x30 line (dex save)"},
                "blue" : {"type" : "lightning", "weapon" : "5x30 line (dex save)"},
                "brass" : {"type" : "fire", "weapon" : "5x30 line (dex save)"},
                "bronze" : {"type" : "lightning", "weapon" : "5x30 line (dex save)"},
                "copper" : {"type" : "acid", "weapon" : "5x30 line (dex save)"},
                "gold" : {"type" : "fire", "weapon" : "15ft cone (dex save)"},
                "green" : {"type" : "poison", "weapon" : "15ft cone (con save)"},
                "red" : {"type" : "fire", "weapon" : "15ft cone (dex save)"},
                "silver" : {"type" : "cold", "weapon" : "15ft cone (con save)"},
                "white" : {"type" : "cold", "weapon" : "15ft cone (con save)"}}
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("Please select a draconic ancestry color from the following. You gain the associated breath attack, as well as resistance to the associated type of damage.")
    for a in ancestry:
        print("-----------------------------")
        print("Color: " + a + "\nType: " + ancestry[a]["type"] + "\nWeapon: " + ancestry[a]["weapon"])
    print("-----------------------------")
    choice = input("Which ancestry do you want to choose?\n")
    #Check to make sure the input race is valid
    if not choice in ancestry:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("***Please enter a valid ancestry type (capitalization matters). Try again!***")
        time.sleep(3)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        return chooseDraconicAncestry(temp)
    else:
        temp["attacks"].update({"Breath Weapon" : ancestry[choice]["type"] + " - " + ancestry[choice]["weapon"]})
        temp["resistances"].extend([ancestry[choice]["type"]])
    return temp

def chooseTwoASI(sheet):
    """Increases two ability scores by one each."""
    temp = sheet
    scores = ["str", "dex", "con", "int", "wis", "cha"]
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("Please select a score to increase by 1:")
    for s in scores:
        print("-----------------------------")
        print(s)
    print("-----------------------------")
    choice = input("Which ability would you like to increase?\n")
    if not choice in scores:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("***Please enter a valid ability score (capitalization matters). Try again!***")
        time.sleep(3)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        return chooseTwoASI(sheet)
    else:
        temp["scores"][choice]["val"] += 1
        scores.remove(choice)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("Please select a second score to increase by 1:")
        for s in scores:
            print("-----------------------------")
            print(s)
        print("-----------------------------")
        choice = input("Which ability would you like to increase?\n")
        if not choice in scores:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("***Please enter a valid ability score (capitalization matters). Start choosing two again!***")
            time.sleep(3)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            return chooseTwoASI(sheet)
        else:
            temp["scores"][choice]["val"] += 1
            return temp

def chooseRace(sheet, rand):
    """Chooses a race and a subrace."""
    races = {"dwarf" : {"desc" : "Kingdoms rich in ancient grandeur, halls carves into the roots of mountains, the echoing of picks and hammers in deep mines and blazing forges, a commitment to clan and tradition, and a burning hatred of goblins and orcs - these common threads unite all dwarves.",
                        "asi" : {"con" : 2},
                        "speed" : 25,
                        "resistances" : ["poison"],
                        "features" : {"Darkvision" : "Accustomed to life underground, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern colors in the dark, only shades of gray.",
                                      "Dwarven Resilience" : "You have advantage on saving throws against poison, and you have resistance against poison damage.",
                                      "Stonecunning" : "Whenever you make an Intelligence (History) check related to the origin of stonework, you are considered proficient in the History skill and add double your proficiency bonus to the check, instead of your normal proficiency."},
                        "proficiencies" : {"weapons" : ["battleaxe", "handaxe", "light hammer", "warhammer"],
                                           "tools" : {"choose one" : ["smith's tools", "brewer's supplies", "mason's tools"]}},
                        "languages" : ["common", "dwarvish"],
                        "subraces" : {"hill dwarf" : {"desc" : "As a hill dwarf, you have keen senses, deep intuition, and remarkable resilience. The gold dwarves of Faerun in their mighty southern kingdom are hilll dwarves, as are the exiled Neidar and the debased Klar of Krynn in the Dragonlance setting.",
                                            "asi" : {"wis" : 1},
                                            "features" : {"Dwarven Toughness" : "Your hit point maximum increases by 1, and it increases by 1 every time you gain a level."}},
                            "mountain dwarf" : {"desc" : "As a mountain dwarf, you're strong and hardy, accusstomed to a difficult life in rugged terrain. You're probably on the tall side (for a dwarf), and tend toward lighter coloration. The shield dwarves of northern Faerun, as well as the ruling Hylar clan and the noble Daewar clan of Dragonlance, are mountain dwarves.",
                                                "asi" : {"str" : 2},
                                                "proficiencies" : {"armor" : ["light", "medium"]}}}},
             "elf" : {"desc" : "Elves are magical people of people of otherworldly grace, living in the world but not entirely part of it. They live in places of ethereal beauty, in the midst of ancient forests or in silvery spires glittering with faerie light, where soft music drifts through the air and gentle fragrances waft on the breeze. Elves love nature and magic, art and artistry, music and poetry, and the good things of the world.",
                      "asi" : {"dex" : 2},
                      "speed" : 30,
                      "features" : {"Darkvision" : "Accustomed to life underground, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern colors in the dark, only shades of gray.",
                                    "Fey Ancestry" : "You have advantage on saving throws against being charmed, and magic can't put you to sleep.",
                                    "Trance" : "Elves don't need to sleep. Instead, they meditate deeply, remaining semiconscious, for 4 hours a day. (The common word for such meditation is 'trance.') While meditating, you can dream after a fashion; such dreams are actually mental exercises that have become reflexive through years of practice. After resting in this way, you gain the same benefit that a human does from 8 hours of sleep."},
                      "proficiencies" : {"skills" : ["perception"]},
                      "languages" : ["common", "elvish"],
                      "subraces" : {"high elf" : {"desc" : "As a high elf, you have a keen mind and a mastery of at least the basics of magic. In many of the world of D&D, there are twoo kinds of high elves. One type (which includes the gray elves and valley elves of Greyhawk, the Silvanesti of Dragonlance, and the sun elves of the Forgotten Realms) is haughty and reclusive, believing themselves to be superior to non-elves and even other elves. The other type (including the high elves of Greyhawk, the Qualinesti of Dragonlance, and the moon elves of the Forgotten Realms) are more common and more friendly, and often encountered among humans and other races.",
                                                  "asi" : {"int" : 1},
                                                  "proficiencies" : {"weapons" : ["longsword", "shortsword", "shortbow", "longbow"]},
                                                  "features" : {"Cantrip" : "You know one extra cantrip of your choice from the wizard spell list. Intelligence is your spellcasting ability for it."}},
                                    "wood elf" : {"desc" : "As a wood elf, you have keen senses and intuition, and your fleet feet carry you quickly and stealthily through your native forests. This category includes the wild elves (grugach) of Greyhawk and the Kagonesti of Dragonlance, as well as the races called wood elves in Greyhawk and the Forgotten Realms. In Faer�n, wood elves (also called wild elves, green elves, or forest elves) are reclusive and distrusting of non-elves.",
                                                  "asi" : {"wis" : 1},
                                                  "proficiencies" : {"weapons" : ["longsword", "shortsword", "shortbow", "longbow"]},
                                                  "speed" : 35,
                                                  "features" : {"Mask of the Wild" : "You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling snow, mist, and other natural phenomena."}},
                                    "dark elf" : {"desc" : "Descended from an earlier subrace of elves, the drow were banished from the surface world for following the goddess Lolth down the path of evil. Now they have built their own civilization in the depths of the Underdark, patterned after the Way of Lolth. Also called dark elves, the drow have skin that resembles charcoal or obsidian, as well as stark white or pale yellow hair. They commonly have very pale eyes (so pale as to be mistaken for white) in shades of lilac, silver, pink, red, and blue. They tend to be smaller and thinner than most elves.",
                                                  "asi" : {"cha" : 1},
                                                  "features" : {"Superior Darkvision" : "Your darkvision has a range of 120 feet.",
                                                                "Sunlight Sensitivity" : "You have disadvantage on attack rolls and Wisdom (Perception) checks that rely on sight when you, the target of the attack, or whatever you are trying to perceive is in direct sunlight.",
                                                                "Drow Magic" : "You know the 'dancing lights' cantrip. When you reach 3rd level, you can cast the 'faerie fire' spell once with this trait and regain the ability to do so when you finish a long rest. When you reach 5th level, you can cast the 'darkness' spell once with this trait and regain the ability to do so once you finish a long rest. Charisma is your spellcasting ability for these spells."},
                                                  "proficiencies" : {"weapons" : ["rapiers", "shortswords", "hand crossbows"]}}}},
             "halfling" : {"desc" : "The comforts of home are the goals of most halflings� lives: a place to settle in peace and quiet, far from marauding monsters and clashing armies; a blazing fire and a generous meal; fine drink and fine conversation. Though some halflings live out their days in remote agricultural communities, others form nomadic bands that travel constantly, lured by the open road and the wide horizon to discover the wonders of new lands and peoples. But even these wanderers love peace, food, hearth, and home, though home might be a wagon jostling along a dirt road or a raft floating downriver.",
                           "asi" : {"dex" : 2},
                           "speed" : 25,
                           "features" : {"Lucky" : "When you roll a 1 on the d20 for an attack roll, ability check, or saving throw, you can reroll the die and must use the new roll.",
                                         "Brave" : "You have advantage on saving throws against being frightened.",
                                         "Halfling Nimbleness" : "You can move through the space of any creature that is of a size larger than yours."},
                           "languages" : ["common", "halfling"],
                           "subraces" : {"lightfoot" : {"desc" : "As a lightfoot halfling, you can easily hide from notice, even using other people as cover. You're inclined to be affable and get along well with others. In the Forgotten Realms lightfoot halflings have spread the farthest and thus are the most common variety. Lightfoots are prone to wanderlust than other halflings, and often dwell alongside other races or take up a nomadic life. In the world of Greyhawk, these halflings are called hairfeet or tallfellows",
                                                        "asi" : {"cha" : 1},
                                                        "features" : {"Naturally Stealthy" : "You can attempt to hide even when you are obscured only by a creature that is at least one size larger than you."}},
                                         "stout" : {"desc" : "As a stout halfling, you're hardier than average and have some resistance to poison. Some say that stouts have dwarven blood. In the Forgotten Realms, these halflings are colled stronghearts, and they're most common in the south.",
                                                    "asi" : {"con" : 1},
                                                    "resistances" : ["poison"],
                                                    "features" : {"Stout Resilience" : "You have advantage on saving throws against poison, and you have resistance against poison damage."}}}},
    "human" : {"desc" : "In the reckonings of most worlds, humans are the youngest of the common races, late to arrive on the world scene and short-lived in comparison to dwarves, elves, and dragons. Perhaps it is because of their shorter lives that they strive to achieve as much as they can in the years they are given. Or maybe they feel they have something to prove to the elder races, and that�s why they build their mighty empires on the foundation of conquest and trade. Whatever drives them, humans are the innovators, the achievers, and the pioneers of the worlds.",
               "asi" : {"str" : 1, "dex" : 1, "con" : 1, "int" : 1, "wis" : 1, "cha" : 1},
               "speed" : 30,
               "languages" : ["common", "choose 1"]},
             "dragonborn" : {"desc" : "Born of dragons, as their name proclaims, the dragonborn walk proudly through a world that greets them with fearful incomprehension. Shaped by draconic gods or the dragons themselves, dragonborn originally hatched from dragon eggs as a unique race, combining the best attributes of dragons and humanoids. Some dragonborn are faithful servants to true dragons, others form the ranks of soldiers in great wars, and still others find themselves adrift, with no clear calling in life.",
                             "asi" : {"str" : 2, "cha" : 1},
                             "speed" : 30,
                             "languages" : ["common", "draconic"],
                             "features" : {"Draconic Ancestry" : "You have draconic ancestry. Your breath weapon and damage resistance are determined by the dragon type.",
                                 "Breath Weapon" : "You can use your action to exhale destructive energy. Your draconic ancestry determines the size, shape, and damage type of the exhalation. When you use your breath weapon, each creature in the area of the exhalation must make a saving throw, the type of which is determined by your draconic ancestry. The DC for this saving throw equals 8 + your Constitution modifier + your proficiency bonus. A creature takes 2d6 damage on a failed save, and half as much damage on a successful one. The damage increases to 3d6 at 6th level, 4d6 at 11th level, and 5d6 at 16th level. After you use your breath weapon, you can�t use it again until you complete a short or long rest.",
                                           "Damage Resistance" : "You have resistance to the damage type associated with your draconic ancestry."}},
             "gnome" : {"desc" : "A constant hum of busy activity pervades the warrens and neighborhoods where gnomes form their close-knit communities. Louder sounds punctuate the hum: a crunch of grinding gears here, a minor explosion there, a yelp of surprise or triumph, and especially bursts of laughter. Gnomes take delight in life, enjoying every moment of invention, exploration, investigation, creation, and play.",
                        "asi" : {"int" : 2},
                        "speed" : 25,
                        "languages" : ["common", "gnomish"],
                        "features" : {"Darkvision" : "Accustomed to life underground, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.",
                                      "Gnome Cunning" : "You have advantage on all Intelligence, Wisdom, and Charisma saving throws against magic."},
                        "subraces" : {"forest gnome" : {"desc" : "As a forest gnome, you have a natural knack for illusion and inherent quickness and stealth. In the worlds of D&D, forest gnomes are rare and secretive. They gather in hidden communities in sylvan forests, using illusions and trickery to conceal themselves from threats or to mask their escape should they be detected. Forest gnomes tend to be friendly with other good-spirited woodland folk, and they regard elves and good fey as their most important allies. These gnomes also befriend small firest animals and rely on them for information about threats that might prowl their lands.",
                                                        "asi" : {"dex" : 2},
                                                        "features" : {"Natural Illusionist" : "You know the 'minor illusion' cantrip. Intelligence is your spellcasting modifier for it.",
                                                                      "Speak with Small Beasts" : "Through sounds and gestures, you can communicate simple ideas with Small or smaller beasts. Forest gnomes love animals and often keep squirrels, badgers, rabbits, moles, woodpeckers, and other creatures as beloved pets."}},
                                      "rock gnome" : {"desc" : "As a rock gnome, you have a natural inventiveness and hardiness beyond that of other gnomes. Most gnomes in the worlds of D&D are rock gnomes, including the tinker gnomes of the Dragonlance setting.",
                                                      "asi" : {"con" : 1},
                                                      "features" : {"Artificer's Lore" : "Whenever you make an Intelligence (History) check related to magic items, alchemical objects, or technological devices, you can add twice your proficiency bonus, instead of any proficiency bonus you normally apply.",
                                                                    "Tinker" : "You have proficiency with artisan's tools (tinker's tools). Using those tools, you can spend 1 hour and 10 gp worth of materials to construct a Tiny clockwork device (AC 5, 1 hp). The device ceases to function after 24 hours (unless you spend 1 hour repairing it to keep the device functioning), or when you use your action to dismantle it; at that time, you can reclaim the materials used to create it. You can have up to three such devices active at a time.\n\nWhen you create a device, choose one of the following options:\n\nClockwork Toy. This toy is a clockwork animal, monster, or person, such as a frog, mouse, bird, dragon, or soldier. When placed on the ground, the toy moves 5 feet across the ground on each of your turns in a random direction. It makes noises as appropriate to the creature it represents.\n\nFire Starter. The device produces a miniature flame, which you can use to light a candle, torch, or campfire. Using the device requires your action.\n\nMusic Box. When opened, this music box plays a single song at a moderate volume. The box stops playing when it reaches the song�s end or when it is closed."},
                                                      "proficiencies" : {"tools" : ["artisan's tools (tinker tools)"]}}}},
             "half-elf" : {"desc" : "Walking in two worlds but truly belonging to neither, half-elves combine what some say are the best qualities of their elf and human parents: human curiosity, inventiveness, and ambition tempered by the refined senses, love of nature, and artistic tastes of the elves. Some half-elves live among humans, set apart by their emotional and physical differences, watching friends and loved ones age while time barely touches them. Others live with the elves, growing restless as they reach adulthood in the timeless elven realms, while their peers continue to live as children. Many half-elves, unable to fit into either society, choose lives of solitary wandering or join with other misfits and outcasts in the adventuring life.",
                           "asi" : {"cha" : 2, "choose two" : None},
                           "speed" : 30,
                           "features" : {"Darkvision" : "Thanks to your elf blood, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.",
                                         "Fey Ancestry" : "You have advantage on saving throws against being charmed, and magic can't put you to sleep."},
                           "proficiencies" : {"skills" : ["choose 2"]},
                           "languages" : ["common", "elvish", "choose 1"]},
             "half-orc" : {"desc" : "Whether united under the leadership of a mighty warlock or having fought to a standstill after years of conflict, orc and human tribes sometimes form alliances, joining forces into a larger horde to the terror of civilized lands nearby. When these alliances are sealed by marriages, half-orcs are born. Some half-orcs rise to become proud chiefs of orc tribes, their human blood giving them an edge over their full-blooded orc rivals. Some venture into the world to prove their worth among humans and other more civilized races. Many of these become adventurers, achieving greatness for their mighty deeds and notoriety for their barbaric customs and savage fury.",
                           "asi" : {"str" : 2, "con" : 1},
                           "speed" : 30,
                           "proficiencies" : {"skills" : ["intimidation"]},
                           "languages" : ["common", "orc"],
                           "features" : {"Darkvision" : "Thanks to your orc blood, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern colors in darkness, only shades of gray.",
                                         "Relentless Endurance" : "When you are reduced to 0 hit points but not killed outright, you can drop to 1 hit point instead. You can't use this feature again until you finish a long rest.",
                                         "Savage Attacks" : "When you score a critical hit with a melee weapon attack, you can roll one of the weapon's damage dice one additional time and add it to the extra damage of the critical hit."}},
             "tiefling" : {"desc" : "To be greeted with stares and whispers, to suffer violence and insult on the street, to see mistrust and fear in every eye: this is the lot of the tiefling. And to twist the knife, tieflings know that this is because a pact struck generations ago infused the essence of Asmodeusoverlord of the Nine Hellsinto their bloodline. Their appearance and their nature are not their fault but the result of an ancient sin, for which they and their children and their children's children will always be held accountable.",
                           "asi" : {"int" : 1, "cha" : 2},
                           "speed" : 30,
                           "resistances" : ["fire"],
                           "languages" : ["common", "infernal"],
                           "features" : {"Darkvision" : "Thanks to your infernal heritage, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.",
                                         "Infernal Legacy" : "You know the 'thaumaturgy' cantrip. When you reach 3rd level, you can cast the 'hellish rebuke' spell as a 2nd-level spell once with this trait and regain the ability to do so when you finish a long rest. When you reach 5th level, you can cast the 'darkness' spell once with this trait and regain the ability to do so when you finish a long rest. Charisma is your spellcasting ability for these spells."}}}

    temp = sheet
    if not rand:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("Please choose a race from the following options: ")
        for r in sorted(races):
            print("-----------------------------")
            print("Race: " + r)
            print("\nDescription: " + races[r]["desc"])
        print("-----------------------------")

        race = input("Which race do you want to play as?\n")
        #Check to make sure the input race is valid
        if not race in races:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("***Please enter a valid race (capitalization matters). Try again!***")
            time.sleep(3)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            return chooseRace(sheet, rand)
        else:
            #Update race
            temp["race"] = race
            #Update ability scores
            for score in races[race]["asi"]:
                if(score == "choose two"):
                    temp = chooseTwoASI(temp)
                else:
                    temp = doASI(temp, score, races[race]["asi"][score])
            #Update speed
            temp["combat info"]["speed"] = races[race]["speed"]
            #Update features
            if "features" in races[race]:
                temp["features"].update(races[race]["features"])
                if "Draconic Ancestry" in races[race]["features"]:
                    temp = chooseDraconicAncestry(temp)
            #Update languages
            for l in races[race]["languages"]:
                if(l.split(' ')[0] == "choose"):
                    temp = chooseLanguages(temp, int(l.split(' ')[1]))
                else:
                    if l in temp["languages"]:
                        temp = chooseLanguages(temp, 1)
                    else:
                        temp["languages"].append(l)
            #Update resistances
            if "resistances" in races[race]:
                temp["resistances"].extend(races[race]["resistances"])
            #Update weapon proficiencies
            if "proficiencies" in races[race]:
                if "weapons" in races[race]["proficiencies"]:
                    temp["proficiencies"]["weapons"].extend(races[race]["proficiencies"]["weapons"])
                #Update armor proficiencies
                if "armor" in races[race]["proficiencies"]:
                    temp["proficiencies"]["armor"].extend(races[race]["proficiencies"]["armor"])
                #Update skill proficiencies
                if "skills" in races[race]["proficiencies"]:
                    for s in races[race]["proficiencies"]["skills"]:
                        if(s.split(' ')[0] == "choose"):
                            temp = chooseSkills(temp, int(s.split(' ')[1]))
                        else:
                            if(temp["skills"][s]["proficient"]):
                                temp = chooseSkills(temp, 1)
                            else:
                                temp["skills"][s]["proficient"] = True
                                temp["skills"][s]["mod"] += temp["proficiency"]
                #Update tool proficiencies
                if "tools" in races[race]["proficiencies"]:
                    for t in races[race]["proficiencies"]["tools"]:
                        if(t == "choose one"):
                            chosen = chooseOneTool(races[race]["proficiencies"]["tools"][t])
                            temp["proficiencies"]["tools"].extend([chosen])
                        else:
                            temp["proficiencies"]["tools"].extend([t])
            #Choose a subrace
            if("subraces" in races[race] and races[race]["subraces"] != None):
                temp = chooseSubrace(temp, races[race]["subraces"])
        return temp

def chooseLanguages(sheet, amt):
    """Adds a number of languages to the sheet equal to amt."""
    temp = sheet
    languages = ["dwarvish",
                 "elvish",
                 "giant",
                 "gnomish",
                 "goblin",
                 "halfling",
                 "orc",
                 "abyssal",
                 "celestial",
                 "deep speech",
                 "draconic",
                 "infernal",
                 "primordial",
                 "sylvan",
                 "undercommon"]
    options = []
    for l in languages:
        if l not in temp["languages"]:
            options.append(l)

    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("Please choose a language from the following options: ")
    for o in sorted(options):
        print("-----------------------------")
        print(o)
    print("-----------------------------")

    choice = input("Which language would you like to be able to speak?\n")
    #Check to make sure the input race is valid
    if not choice in options:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("***Please enter a valid language (capitalization matters). Try again!***")
        time.sleep(3)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        return chooseLanguages(sheet, amt)
    else:
        temp["languages"].append(choice)
        if(amt > 1):
            temp = chooseLanguages(temp, amt - 1)
        return temp

def chooseSkills(sheet, amt, options=None):
    """Adds skills to the sheet equal to amt."""
    temp = sheet
    if(options == None):
        skills = ["acrobatics",
                  "animal handling",
                  "arcana",
                  "athletics",
                  "deception",
                  "history",
                  "insight",
                  "intimidation",
                  "investigation",
                  "medicine",
                  "nature",
                  "perception",
                  "performance",
                  "persuasion",
                  "religion",
                  "sleight of hand",
                  "stealth",
                  "survival"]
    else:
        skills = options

    temp_options = []
    for s in skills:
        if not temp["skills"][s]["proficient"]:
            temp_options.append(s)

    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("Please choose a skill from the following options: ")
    for o in sorted(temp_options):
        print("-----------------------------")
        print(o)
    print("-----------------------------")

    choice = input("Which skill would you like to be proficient in?\n")
    #Check to make sure the input race is valid
    if not choice in temp_options:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("***Please enter a valid skill (capitalization matters). Try again!***")
        time.sleep(3)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        return chooseSkills(sheet, amt, options)
    else:
        temp["skills"][choice]["proficient"] = True
        temp["skills"][choice]["mod"] += temp["proficiency"]
        if(amt > 1):
            temp = chooseSkills(temp, amt - 1, options)
        return temp

def chooseBackground(sheet, rand):
    """Chooses a background for the sheet"""
    backgrounds = {"acolyte" : {"desc" : "You have spent your life in the service of a temple to a specific god or pantheon of gods. You act as an intermediary between the realm of the holy and the mortal world, performing sacred rites and offering sacrifices in order to conduct worshipers into the presence of the divine. You are not necessarily a clericperforming sacred rites is not the same thing as channeling divine power.",
                                "proficiencies" : {"skills" : ["insight", "religion"]},
                                "languages" : ["choose 2"],
                                "equipment" : {"a holy symbol" : 1,
                                               "a prayer book or prayer wheel" : 1,
                                               "stick of incense" : 5,
                                               "vestments" : 1,
                                               "a set of common clothes" : 1,
                                                "gp" : 15},
                                "features" : {"Shelter of the Faithful" : "As an acolyte, you Command the respect of those who share your faith, and you can perform the religious ceremonies of your deity. You and your Adventuring companions can expect to receive free Healing and care at a temple, shrine, or other established presence of your faith, though you must provide any material Components needed for Spells. Those who share your Religion will support you (but only you) at a modest lifestyle."}},
                   "charlatan" : {"desc" : "You have always had a way with people. You know what makes them tick, you can tease out their heart�s desires after a few minutes of conversation, and with a few leading questions you can read them like they were children's books. It�s a useful talent, and one that you�re perfectly willing to use for your advantage.",
                                  "proficiencies" : {"skills" : ["deception", "sleight of hand"],
                                                     "tools" : ["disguise kit", "forgery kit"]},
                                  "equipment" : {"a set of fine clothes" : 1,
                                                 "a disguise kit" : 1,
                                                 "tools of the con of your choice (ten stoppered bottles filled with colored liquid, a set of weighted dice, a deck of marked cards, or a signet ring of an imaginary duke)." : 1,
                                                 "gp" : 15},
                                  "features" : {"False Identity" : "You have created a second identity that includes documentation, established acquaintances, and disguises that allow you to assume that persona. Additionally, you can forge documents including official papers and personal letters, as long as you have seen an example of the kind of document or the handwriting you are trying to copy."}},
                   "criminal" : {"desc" : "You are an experienced criminal with a history of breaking the law. You have spent a lot of time among other criminals and still have contacts within the criminal underworld. You're far closer than most people to the world of murder, theft, and violence that pervades the underbelly of civilization, and you have survived up to this point by flouting the rules and regulations of society.",
                                 "proficiencies" : {"skills" : ["deception", "stealth"],
                                                    "tools" : ["one type of gaming set", "thieve's tools"]},
                                 "equipment" : {"a crowbar" : 1,
                                                "a set of dark common clothes including a hood" : 1,
                                                "gp" : 15},
                                 "features" : {"Criminal Contact" : "You have a reliable and trustworthy contact who acts as your liason to a network of other criminals. You know how to get messages to and from your contact, even over great distances; specifically, you know the local messengers, corrupt caravan masters, and seedy sailors who can deliver messages for you."}},
                   "entertainer" : {"desc" : "You thrive in front of anaudience. You know how to entrance them, entertain then, and even inspire them. Your poetics can stir the hearts of those who hear you, awakening grief or joy, laughter or anger. Your music raises their spirits or captures their sorrow. Your dance steps captivate, your humor cuts to the quick. Whatever techniques you use, your art is your life.",
                                    "proficiencies" : {"skills" : ["acrobatics", "performance"],
                                                       "tools" : ["disguise kit", "one kind of musical instrument"]},
                                    "equipment" : {"a musical instrument (one of your choice)" : 1,
                                                   "the favor of an admirer (love letter, lock of hair, or trinket)" : 1,
                                                   "a costume" : 1,
                                                   "gp" : 15},
                                    "features" : {"By Popular Demand" : "You can always find a place to perform, usually in an inn or tavern but possibly with a circus, at a theater, or even in a noble's court. At such a place, you receive free lodging and food of a modest or comfortable standard (depending on the quality of the establishment), as long as you perform each night. In addition, your performance makes you something of a local figure. When strangers recognize you in a rown where you have performed, they typically take a liking to you."}},
                   "folk hero" : {"desc" : "You come from a humble social rank, but you are destined for so much more. Already the people of your hom e village regard you as their champion, and your destiny calls you to stand against the tyrants and monsters that threaten the common folk everywhere.",
                                  "proficiencies" : {"skills" : ["animal handling", "survival"],
                                                     "tools" : ["one type of artisan's tools, vehicles (land)"]},
                                  "equipment" : {"a set of artisan's tools (your choice)" : 1,
                                                 "a shovel" : 1,
                                                 "an iron pot" : 1,
                                                 "a set of common clothes" : 1,
                                                 "gp" : 10},
                                  "features" : {"Rustic Hospitality" : "Since you come from the ranks of the common folk, you fit in among them with ease. You can find a place to hide, rest, or recuperate among other commoners, unless you have shown yourself to be a danger to them. They will shield you from the law or anyone else searching for you, though they will not risk their lives for you."}},
                   "guild artisan" : {"desc" : "You are a member of an artisan�s guild, skilled in a particular field and closely associated with other artisans. You are a well-established part of the mercantile world, freed by talent and wealth from the constraints of a feudal social order. You learned your skills as an apprentice to a master artisan, under the sponsorship of your guild, until you became a master in your own right.",
                                      "proficiencies" : {"skills" : ["insight", "persuasion"],
                                                         "tools" : ["one type of artisan's tools"]},
                                      "languages" : ["choose 1"],
                                      "equipment" : {"a set of artisan's tools (one of your choice)" : 1,
                                                     "a letter of introduction from your guild" : 1,
                                                     "a set of traveler's clothes" : 1,
                                                     "gp" : 15},
                                      "features" : {"Guild Membership" : "As an established and respected member of a guild, you can rely on certain benefits that membership provides. Your fellow guild members will provide you with lodging and food if necessary, and pay for your funeral if needed. In some cities and towns, a guildhall offers a central place to meet other members of your profession, which can be a good place to meet potential patrons, allies, or hirelings. Guilds often wield tremendous political power. If you are accused of a crime, your guild will support you if a good case can be made for your innocence or the crime is justifiable. You can also gain access to powerful political figures through the guild, if you are a member in good standing. Such connections might require the donation of money or magic items to the guild�s coffers. You must pay dues of 5 gp per month to the guild. If you miss payments, you must make up back dues to remain in the guild�s good graces."}},
                   "hermit" : {"desc" : "You lived in seclusion - either in a sheltered community such as a monastery, or entirely alone - for a formative part of your life. In your time apart from the clamor of society, you found quiet, solitude, and perhaps some of the answers you were looking for.",
                               "proficiencies" : {"skills" : ["medicine", "religion"],
                                                  "tools" : ["herbalism kit"]},
                               "languages" : ["choose 1"],
                               "equipment" : {"a scroll case stuffed full of notes from your studies or prayers" : 1,
                                              "a winter blanket" : 1,
                                              "a set of common clothes" : 1,
                                              "an herbalism kit" : 1,
                                              "gp" : 5},
                               "features" : {"Discovery" : "The quiet seclusion of your extended hermitage gave you access to a unique and powerful discovery. The exact nature of this revelation depends on the nature of your seclusion. It might be a great truth about the cosmos, the deities, the powerful beings of the outer planes, or the forces of nature. It could be a site that no one else has ever seen. You might have uncovered a fact that has long been forgotten, or unearthed some relic of the past that could rewrite history. It might be information that would be damaging to the people who consigned you to exile, and hence the reason for your return to society. Work with your DM to determine the details of your discovery and its impact on the campaign."}},
                   "noble" : {"desc" : "You understand wealth, power, and privilege. You carry a noble title, and your family owns land, collects taxes, and wields significant political influence. You might be a pampered aristocrat unfamiliar with work or discomfort, a former merchant just elevated to the nobility, or a disinherited scoundrel with a disproportionate sense of entitlement. Or you could be an honest, hard-working landowner who cares deeply about the people who live and work on your land, keenly aware of your responsibility to them.",
                              "proficiencies" : {"skills" : ["history", "persuasion"],
                                                 "tools" : ["one type of gaming set"]},
                              "languages" : ["choose 1"],
                              "equipment" : {"a set of fine clothes" : 1,
                                             "a signet ring" : 1,
                                             "a scroll of pedigree" : 1,
                                             "gp" : 25},
                              "features" : {"Position of Privilege" : "Thanks to your noble birth, people are inclined to think the best of you. You are welcome in high society, and people assume you have the right to be wherever you are. The common folk and merchants make every effort to accommodate you and avoid your displeasure, and other people of high birth treat you as a member of the same social sphere. You can secure an audience with a local noble if you need to."}},
                   "outlander" : {"desc" : "You grew up in the wilds, far from civilization and the comforts of town and technology. You�ve witnessed the migration of herds larger than forests, survived weather more extreme than any city-dweller could comprehend, and enjoyed the solitude of being the only thinking creature for miles in any direction. The wilds are in your blood, whether you were a nomad, an explorer, a recluse, a hunter-gatherer, or even a marauder. Even in places where you don�t know the specific features of the terrain, you know the ways of the wild.",
                                  "proficiencies" : {"skills" : ["athletics", "survival"],
                                                     "tools" : ["one type of musical instrument"]},
                                  "languages" : ["choose 1"],
                                  "equipment" : {"a staff" : 1,
                                                 "a hunting trap" : 1,
                                                 "a trophy from an animal you killed" : 1,
                                                 "a set of traveler's clothes" : 1,
                                                 "gp" : 10},
                                  "features" : {"Wanderer" : "You have an excellent memory for maps and geography, and you can always recall the general layout of terrain, settlements, and other features around you. In addition, you can find food and fresh water for yourself and up to five other people each day, provided that the land offers berries, small game, water, and so forth."}},
                   "sage" : {"desc" : "You spent years learning the lore of the multiverse. You scoured manuscripts, studied scrolls, and listened to the greatest experts on the subjects that interest you. Your efforts have made you a master in your fields of study.",
                             "proficiencies" : {"skills" : ["arcana", "history"]},
                             "languages" : ["choose 2"],
                             "equipment" : {"a bottle of black ink" : 1,
                                            "a quill" : 1,
                                            "a small knife" : 1,
                                            "a letter from a dead colleague posing a question you have not been able to answer" : 1,
                                            "a set of common clothes" : 1,
                                            "gp" : 10},
                             "features" : {"Researcher" : "When you attempt to learn or recall a piece of lore, if you do not know that information, you often know where and from whom you can obtain it. Usually, this information comes from a library, scriptorium, university, or a sage or other learned person or creature. Your DM might rule that the knowledge you seek is secreted away in an almost inaccessible place, or that it simply cannot be found. Unearthing the deepest secrets of the multiverse can require an adventure or even a whole campaign."}},
                   "sailor" : {"desc" : "You sailed on a seagoing vessel for years. In that time, you faced down mighty storms, monsters of the deep, and those who wanted to sink your craft to the bottomless depths. Your first love is the distant line of the horizon, but the time has come to try your hand at something new.",
                               "proficiencies" : {"skills" : ["athletics", "perception"],
                                                  "tools" : ["navigator's tools", "vehicles (water)"]},
                               "equipment" : {"a belaying pin (club)" : 1,
                                              "50 feet of silk rope" : 1,
                                              "a lucky charm such as a rabbit foot or a small stone with a hole in the center" : 1,
                                              "a set of common clothes" : 1,
                                              "gp" : 10},
                               "features" : {"Ship's Passage" : "When you need to, you can secure free passage on a sailing ship for yourself and your adventuring companions. You might sail on the ship you served on, or another ship you have good relations with (perhaps one captained by a former crewmate). Because you�re calling in a favor, you can�t be certain of a schedule or route that will meet your every need. Your Dungeon Master will determine how long it takes to get where you need to go. In return for your free passage, you and your companions are expected to assist the crew during the voyage."}},
                   "soldier" : {"desc" : "War has been your life for as long as you care to remember. You trained as a youth, studied the use of weapons and armor, learned basic survival techniques, including how to stay alive on the battlefield. You might have been part of a standing national army or a mercenary company, or perhaps a member of a local militia who rose to prominence during a recent war.",
                                "proficiencies" : {"skills" : ["athletics", "intimidation"],
                                                   "tools" : ["one type of gaming set", "vehicles (land)"]},
                                "equipment" : {"an insignia of rank" : 1,
                                               "a trophy taken from a fallen enemy (a dagger, broken blade, or piece of banner" : 1,
                                               "a set of bone dice or deck of cards" : 1,
                                               "a set of common clothes" : 1,
                                               "gp" : 10},
                                "features" : {"Military Rank" : "You have a military rank from your career as a soldier. Soldiers loyal to your former military organization still recognize your authority and influence, and they defer to you if they are of a lower rank. You can invoke your rank to exert influence over other soldiers and requisition simple equipment or horses for temporary use. You can also usually gain access to friendly military encampments and fortresses where your rank is recognized."}},
                   "urchin" : {"desc" : "You grew up on the streets alone, orphaned, and poor. You had no one to watch over you or to provide for you, so you learned to provide for yourself. You fought fiercely over food and kept a constant watch out for other desperate souls who might steal from you. You slept on rooftops and in alleyways, exposed to the elements, and endured sickness without the advantage of medicine or a place to recuperate. You've survived despite all odds, and did so through cunning, strength, speed, or some combination of each.",
                               "proficiencies" : {"skills" : ["sleight of hand", "stealth"],
                                                  "tools" : ["disguise kit", "thieves' tools"]},
                               "equipment" : {"a small knife" : 1,
                                              "a map of the city you grew up in" : 1,
                                              "a pet mouse" : 1,
                                              "a token to remember your parents by" : 1,
                                              "a set of common clothes" : 1,
                                              "gp" : 10},
                               "features" : {"City Secrets" : "You know the secret patterns and flow to cities and can find passages through the urban sprawl that others would miss. When you are not in combat, you (and companions you lead) can travel between any two locations in the city twice as fast as your speed would normally allow."}}}

    temp = sheet
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("Please choose a background from the following options: ")
    if(temp["recommended"] != {}):
        print("(Suggested background based on your class is " + temp["recommended"]["background"] + ".)")
    for b in sorted(backgrounds):
        print("-----------------------------")
        print("Background: " + b)
        print("\nDescription: " + backgrounds[b]["desc"])
    print("-----------------------------")

    background = input("Which background would you like to come from?\n")
    #Check to make sure the input race is valid
    if not background in backgrounds:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("***Please enter a valid background (capitalization matters). Try again!***")
        time.sleep(3)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        return chooseBackground(sheet, rand)
    else:
        #Update background
        temp["background"] = background
        #Update features
        if "features" in backgrounds[background]:
            temp["features"].update(backgrounds[background]["features"])
        #Update languages
        if "languages" in backgrounds[background]:
            for l in backgrounds[background]["languages"]:
                if(l.split(' ')[0] == "choose"):
                    temp = chooseLanguages(temp, int(l.split(' ')[1]))
                else:
                    temp["languages"].append(l)
        #Update proficiencies
        if "proficiencies" in backgrounds[background]:
            #Update weapon proficiencies
            if "weapons" in backgrounds[background]["proficiencies"]:
                temp["proficiencies"]["weapons"].extend(backgrounds[background]["proficiencies"]["weapons"])
            #Update armor proficiencies
            if "armor" in backgrounds[background]["proficiencies"]:
                temp["proficiencies"]["armor"].extend(backgrounds[background]["proficiencies"]["armor"])
            #Update skill proficiencies
            if "skills" in backgrounds[background]["proficiencies"]:
                for s in backgrounds[background]["proficiencies"]["skills"]:
                   if(s.split(' ')[0] == "choose"):
                       temp = chooseSkills(temp, int(s.split(' ')[1]))
                   else:
                       if(temp["skills"][s]["proficient"]):
                           temp = chooseSkills(temp, 1)
                       else:
                           temp["skills"][s]["proficient"] = True
                           temp["skills"][s]["mod"] += temp["proficiency"]
            #Update tool proficiencies
            if "tools" in backgrounds[background]["proficiencies"]:
                for t in backgrounds[background]["proficiencies"]["tools"]:
                   if(t == "choose one"):
                       chosen = chooseOneTool(backgrounds[background]["proficiencies"]["tools"][t])
                       temp["proficiencies"]["tools"].extend([chosen])
                   else:
                       temp["proficiencies"]["tools"].extend([t])
        if "equipment" in backgrounds[background]:
            for e in backgrounds[background]["equipment"]:
                if e in temp["equipment"]:
                    temp["equipment"][e] += backgrounds[background]["equipment"][e]
                else:
                    temp["equipment"][e] = backgrounds[background]["equipment"][e]

        return temp

def randomScore():
    """Rolls 4 d6, drops the lowest."""
    scores = []
    for _ in range(4):
        scores.append(d6())

    my_min = min(scores)
    scores.remove(my_min)
    return sum(scores)

def doAbilityScores(sheet,  values=None):
    """Does the ability scores. Allows the user to choose between standard array and rolling for scores."""
    methods = ["standard", "roll"]
    temp = sheet

    if(values != None):
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    if(values==None):
        method = input("Would you like to use the standard array, or roll for scores? Please type 'standard' or 'roll'.\n")
        if method not in methods:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("***Please enter a valid method - either 'standard' or 'roll' (capitalization matters). Try again!***")
            time.sleep(3)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            return doAbilityScores(sheet, values)
        else:
            if(method == "roll"):
                values = sorted([randomScore(), randomScore(), randomScore(), randomScore(), randomScore(), randomScore()], reverse=True)
            else:
                values = sorted([8, 10, 12, 13, 14, 15], reverse=True)
            return doAbilityScores(temp, values)
    else:
        if(values == []):
            return sheet
        else:
            #Get current options
            options = []
            for s in temp["scores"]:
                if not temp["scores"][s]["assigned"]:
                    options.append(s)
            #Get which score they want to assign to
            current_val = values[0]
            print("Your remaining values to assign are " + str(values))
            print("Please select the ability to which you would like to assign " + str(current_val) + ".")
            if(temp["recommended"] != None and len(values) == 6):
                print("(Recommended ability based on your class is " + temp["recommended"]["first"] + ".)")
            elif(temp["recommended"] != None and len(values) == 5):
                print("(Recommended ability based on your class is " + temp["recommended"]["second"] + ".)")
            print("-----------------------------")
            current = 1
            while current < 7:
                for o in options:
                    if sheet["scores"][o]["order"] == current:
                        print(o + " (currently " + str(temp["scores"][o]["val"]) + ")")
                current += 1
            print("-----------------------------")
            choice = input("To which ability would you like to assign " + str(current_val) + "?\n")
            if choice not in options:
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                print("***Please enter a valid ability. (capitalization matters). Try again!***")
                time.sleep(3)
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                return doAbilityScores(sheet, values)
            else:
                temp["scores"][choice]["val"] += current_val
                temp["scores"][choice]["assigned"] = True
                return doAbilityScores(temp, values[1:])

def doAbilityMods(sheet):
    """Associates the appropriate modifiers with each ability score."""
    mods = {1 : -5,
            2 : -4,
            3 : -4,
            4 : -3,
            5 : -3,
            6 : -2,
            7 : -2,
            8 : -1,
            9 : -1,
            10 : 0,
            11 : 0,
            12 : 1,
            13 : 1,
            14 : 2,
            15 : 2,
            16 : 3,
            17 : 3,
            18 : 4,
            19 : 4,
            20 : 5,
            21 : 5,
            22 : 6,
            23 : 6,
            24 : 7,
            25 : 7,
            26 : 8,
            27 : 8,
            28 : 9,
            29 : 9,
            30 : 10}

    temp = sheet
    for s in temp["scores"]:
        temp["scores"][s]["mod"] = mods[temp["scores"][s]["val"]]

    return temp

def doBarbarian(sheet):
    """This is called when the Barbarian class is chosen."""
    temp = sheet

    #Update class
    temp["class"] = "barbarian"

    #Set the recommended scores and background
    temp["recommended"]["first"] = "str"
    temp["recommended"]["second"] = "con"
    temp["recommended"]["background"] = "outlander"

    _ = input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nNow, we will choose your background. This will determine what kind of life your character led before they became an adventurer. Press enter to continue.\n")
    temp = chooseBackground(temp, False)
    
    #Do Ability Scores
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nNow we will assign your ability scores. These form the basis for your character's stats.")
    temp = doAbilityScores(temp)

    #Hit Points
    temp["combat info"]["hit dice amt"] = 1
    temp["combat info"]["hit dice type"] = "d12"
    temp["combat info"]["hp"] = 12 + temp["scores"]["con"]["mod"]

    #Proficiencies
    temp["proficiencies"]["armor"].extend(["light armor", "medium armor", "shields"])
    temp["proficiencies"]["weapons"].extend(["simple weapons", "martial weapons"])
    #saving throws
    temp["saves"]["str"] += temp["proficiency"]
    temp["saves"]["con"] += temp["proficiency"]
    #skills
    temp = chooseSkills(temp, 2, ["animal handling", "athletics", "intimidation", "nature", "perception", "stealth"])

    #Equipment
    #greataxe
    temp["equipment"].update({"a greataxe" : 1})
    if(temp["scores"]["str"]["mod"] >= 0):
        temp["attacks"].update({"Greataxe" : "+" + str(temp["proficiency"] + temp["scores"]["str"]["mod"]) + " to hit, 1d12+" + str(temp["scores"]["str"]["mod"]) + " slashing"})
    else:
        temp["attacks"].update({"Greataxe" : "+" + str(temp["proficiency"] + temp["scores"]["str"]["mod"]) + " to hit, 1d12" + str(temp["scores"]["str"]["mod"]) + " slashing"})

    #handaxes
    temp["equipment"].update({"a handaxe" : 2})
    if(temp["scores"]["str"]["mod"] >= 0):
        temp["attacks"].update({"Handaxe (melee)" : "+" + str(temp["proficiency"] + temp["scores"]["str"]["mod"]) + " to hit, 1d6+" + str(temp["scores"]["str"]["mod"]) + " slashing"})
    else:
        temp["attacks"].update({"Handaxe (melee)" : "+" + str(temp["proficiency"] + temp["scores"]["str"]["mod"]) + " to hit, 1d6" + str(temp["scores"]["str"]["mod"]) + " slashing"})

    if(temp["scores"]["dex"]["mod"] >= 0):
        temp["attacks"].update({"Handaxe (ranged 20/60)" : "+" + str(temp["proficiency"] + temp["scores"]["dex"]["mod"]) + " to hit, 1d6+" + str(temp["scores"]["dex"]["mod"]) + " slashing"})
    else:
        temp["attacks"].update({"Handaxe (ranged 20/60)" : "+" + str(temp["proficiency"] + temp["scores"]["dex"]["mod"]) + " to hit, 1d6" + str(temp["scores"]["dex"]["mod"]) + " slashing"})

    #javelins
    temp["equipment"].update({"javelin" : 4})
    if(temp["scores"]["str"]["mod"] >= 0):
        temp["attacks"].update({"Javelin (melee)" : "+" + str(temp["proficiency"] + temp["scores"]["str"]["mod"]) + " to hit, 1d6+" + str(temp["scores"]["str"]["mod"]) + " piercing"})
    else:
        temp["attacks"].update({"Javelin (melee)" : "+" + str(temp["proficiency"] + temp["scores"]["str"]["mod"]) + " to hit, 1d6" + str(temp["scores"]["str"]["mod"]) + " piercing"})

    if(temp["scores"]["dex"]["mod"] >= 0):
        temp["attacks"].update({"Javelin (ranged 30/120)" : "+" + str(temp["proficiency"] + temp["scores"]["dex"]["mod"]) + " to hit, 1d6+" + str(temp["scores"]["dex"]["mod"]) + " piercing"})
    else:
        temp["attacks"].update({"Javelin (ranged 30/120)" : "+" + str(temp["proficiency"] + temp["scores"]["dex"]["mod"]) + " to hit, 1d6" + str(temp["scores"]["dex"]["mod"]) + " piercing"})
    #explorer's pack
    temp["equipment"].update({"backpack" : 1,
                              "bedroll" : 1,
                              "mess kit" : 1,
                              "tinderbox" : 1,
                              "torches" : 10,
                              "one day of rations" : 10,
                              "waterskin" : 1,
                              "50 feet of hempen rope" : 1})
    #Features
    temp["features"].update({"Rage" : "In battle, you fight with primal ferocity. On your turn, you can enter a rage as a bonus action. While raging, you gain the following benefits if you aren't wearing heavy armor:\n*You have advantage on strength checks and strength saving throws.\n*When you make a melee weapon attack using strength, you gain a +2 bonus to the damage roll. This bonus increases as you level.\n*You have resistance to bludgeoning, piercing, and slashing damage.\nIf you are able to cast spells, you can't cast them or concentrate on them while raging. Your rage lasts for 1 minute. It ends early if you are knocked unconscious or if your turn ends and you haven't attacked a hostile creature since your last turn or taken damage since then. You can also end your rage on Your Turn as a bonus action. Once you have raged the maximum number of times for your barbarian level, you must finish a long rest before you can rage again. You may rage 2 times at 1st level, 3 at 3rd, 4 at 6th, 5 at 12th, and 6 at 17th.",
                             "Unarmored Defense" : "While you are not wearing any armor, your armor class equals 10 + your dexterity modifier + your constitution modifier. You can use a shield and still gain this benefit."})
    #AC (accounting for unarmored defense)
    temp["combat info"]["ac"] += 10 + temp["scores"]["dex"]["mod"] + temp["scores"]["con"]["mod"]
    # initiative
    temp["combat info"]["initiative"] = "+" + str(temp["scores"]["dex"]["mod"] + temp["combat info"]["initiative"])
    return temp

def chooseBardCantrips(sheet, amt):
    """Adds bard cantrips equal to amt to the spellcasting section of sheet."""
    temp = sheet
    cantrips = ["Blade Ward",
            "Dancing Lights",
            "Friends",
            "Light",
            "Mage Hand",
            "Mending",
            "Message",
            "Minor Illusion",
            "Prestidigitation",
            "True Strike",
            "Vicious Mockery"]

    temp_options = []
    for c in cantrips:
        if not c in temp["spellcasting"][0]:
            temp_options.append(c)

    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("Please choose a cantrip from the following options: ")
    for o in sorted(temp_options):
        print("-----------------------------")
        print(o)
    print("-----------------------------")

    choice = input("Which cantrip would you like to learn?\n")
    #Check to make sure the input cantrip is valid
    if not choice in temp_options:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("***Please enter a valid cantrip (capitalization matters). Try again!***")
        time.sleep(2)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        return chooseBardCantrips(sheet, amt)
    else:
        temp["spellcasting"][0].append(choice)
        if(amt > 1):
            temp = chooseBardCantrips(temp, amt - 1)
        return temp
    return temp

def chooseBardFirstLevel(sheet, amt):
    """Adds bard lvl 1 spells equal to amt to the spellcasting section of sheet."""
    temp = sheet
    spells = ["Animal Friendship",
            "Bane",
            "Charm Person",
            "Comprehend Languages",
            "Cure Wounds",
            "Detect Magic",
            "Disguise Self",
            "Dissonant Whispers",
            "Faerie Fire",
            "Feather Fall",
            "Healing Word",
            "Heroism",
            "Identify",
            "Illusory Script",
            "Longstrider",
            "Silent Image",
            "Sleep",
            "Speak with Animals",
            "Tasha's Hideous Laughter",
            "Thunderwave",
            "Unseen Servant"]

    temp_options = []
    for s in spells:
        if not s in temp["spellcasting"][1]:
            temp_options.append(s)

    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("Please choose a level one spell from the following options: ")
    for o in sorted(temp_options):
        print("-----------------------------")
        print(o)
    print("-----------------------------")

    choice = input("Which spell would you like to learn?\n")
    #Check to make sure the input cantrip is valid
    if not choice in temp_options:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("***Please enter a valid spell (capitalization matters). Try again!***")
        time.sleep(2)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        return chooseBardFirstLevel(sheet, amt)
    else:
        temp["spellcasting"][1].append(choice)
        if(amt > 1):
            temp = chooseBardFirstLevel(temp, amt - 1)
        return temp
    return temp

def doBard(sheet):
    """This is called when the Bard class is chosen."""
    temp = sheet
    skills = ["acrobatics",
                  "animal handling",
                  "arcana",
                  "athletics",
                  "deception",
                  "history",
                  "insight",
                  "intimidation",
                  "investigation",
                  "medicine",
                  "nature",
                  "perception",
                  "performance",
                  "persuasion",
                  "religion",
                  "sleight of hand",
                  "stealth",
                  "survival"]
    
    #Update class
    temp["class"] = "bard"

    #Set the recommended scores and background
    temp["recommended"]["first"] = "cha"
    temp["recommended"]["second"] = "dex"
    temp["recommended"]["background"] = "entertainer"
    temp["recommended"]["spells"] = {"dancing lights" : 0,
                                "vicious mockery" : 0,
                                "charm person" : 1,
                                "detect magic" : 1,
                                "healing word" : 1,
                                "thunderwave" : 1}

    _ = input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nNow, we will choose your background. This will determine what kind of life your character led before they became an adventurer. Press enter to continue.\n")
    temp = chooseBackground(temp, False)
    
    #Do Ability Scores
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nNow we will assign your ability scores. These form the basis for your character's stats.")
    temp = doAbilityScores(temp)

    #Hit Points
    temp["combat info"]["hit dice amt"] = 1
    temp["combat info"]["hit dice type"] = "d8"
    temp["combat info"]["hp"] = 8 + temp["scores"]["con"]["mod"]

    #Proficiencies
    temp["proficiencies"]["armor"].extend(["light armor"])
    temp["proficiencies"]["weapons"].extend(["simple weapons", "hand crossbows", "longswords", "rapiers", "shortswords"])
    temp["proficiencies"]["tools"].extend(["three musical instruments of your choice."])
    #saving throws
    temp["saves"]["dex"] += temp["proficiency"]
    temp["saves"]["cha"] += temp["proficiency"]
    #skills
    temp = chooseSkills(temp, 3, skills)

    #Equipment
    #Rapier
    temp["equipment"].update({"a rapier" : 1})
    if(temp["scores"]["str"]["mod"] > temp["scores"]["dex"]["mod"]):
        better = "str"
    else:
        better = "dex"
    if(temp["scores"][better]["mod"] >= 0):
        temp["attacks"].update({"Rapier" : "+" + str(temp["proficiency"] + temp["scores"][better]["mod"]) + " to hit, 1d8+" + str(temp["scores"][better]["mod"]) + " piercing"})
    else:
        temp["attacks"].update({"Rapier" : "+" + str(temp["proficiency"] + temp["scores"][better]["mod"]) + " to hit, 1d8" + str(temp["scores"][better]["mod"]) + " piercing"})
    #dagger
    temp["equipment"].update({"a dagger" : 1})
    if(temp["scores"]["str"]["mod"] > temp["scores"]["dex"]["mod"]):
        better = "str"
    else:
        better = "dex"
    if(temp["scores"][better]["mod"] >= 0):
        temp["attacks"].update({"Dagger (melee)" : "+" + str(temp["proficiency"] + temp["scores"][better]["mod"]) + " to hit, 1d4+" + str(temp["scores"][better]["mod"]) + " piercing"})
    else:
        temp["attacks"].update({"Dagger (melee)" : "+" + str(temp["proficiency"] + temp["scores"][better]["mod"]) + " to hit, 1d4" + str(temp["scores"][better]["mod"]) + " piercing"})

    if(temp["scores"]["dex"]["mod"] >= 0):
        temp["attacks"].update({"Dagger (ranged 20/60)" : "+" + str(temp["proficiency"] + temp["scores"]["dex"]["mod"]) + " to hit, 1d4+" + str(temp["scores"]["dex"]["mod"]) + " piercing"})
    else:
        temp["attacks"].update({"Dagger (ranged 20/60)" : "+" + str(temp["proficiency"] + temp["scores"]["dex"]["mod"]) + " to hit, 1d4" + str(temp["scores"]["dex"]["mod"]) + " piercing"})
    #entertainer's pack
    temp["equipment"].update({"backpack" : 1,
                              "bedroll" : 1,
                              "costume" : 2,
                              "candle" : 5,
                              "one day of rations" : 5,
                              "waterskin" : 1,
                              "disguise kit" : 1})
    #A musical instrument
    temp["equipment"].update({"one musical instrument of your choice." : 1})
    #Leather Armor
    temp["equipment"].update({"leather armor" : 1})

    #Features
    temp["features"].update({"Bardic Inspiration" : "You can use a bonus action on your turn to choose one creature other than yourself within 60 feet of you who can hear you. That creature gains one Bardic Inspiration die, a d6. Once within the next 10 minutes, the creature can roll the die and add the number rolled to one ability check, attack roll, or saving throw it makes. The creature can wait until after it rolls the d20 before deciding to use the Bardic Inspiration die, but must decide before the DM says whether the roll succeeds or fails. Once the Bardic Inspiration die is rolled, it is lost. A creature can have only one Bardic Inspiration die at a time. You can use this feature a number of times equal to your Charisma modifier (a minimum of once). You regain any expended uses when you finish a long rest. Your Bardic Inspiration die changes when you reach certain levels in this class. The die becomes a d8 at 5th level, a d10 at 10th level, and a d12 at 15th level."})
    temp["features"].update({"Spellcasting" : "You have learned to untangle and reshape the fabric of reality in harmony with your wishes and music. Your spells are part of your vast repertiore, magic that you can tune to different situations."})
    
    #Spellcasting
    temp["spellcasting"] = {0 : [], 1 : [], "slots" : {}}
    temp = chooseBardCantrips(temp, 2)
    temp = chooseBardFirstLevel(temp, 4)
    temp["spellcasting"]["slots"].update({"1st" : 2})
    temp["spellcasting"]["dc"] = 8 + temp["proficiency"] + temp["scores"]["cha"]["mod"]
    temp["spellcasting"]["mod"] = temp["proficiency"] + temp["scores"]["cha"]["mod"]


    #AC (accounting for unarmored defense)
    temp["combat info"]["ac"] += 11 + temp["scores"]["dex"]["mod"]
    # initiative
    temp["combat info"]["initiative"] = "+" + str(temp["scores"]["dex"]["mod"] + temp["combat info"]["initiative"])
    return temp

def chooseClass(sheet, rand):
    """Chooses a class."""
    classes = {"barbarian" : "A fierce warrior of a primitive background who can enter a battle rage",
               "bard" : "An inspiring magician whose power echoes the music of creation.",
               "cleric" : "A priestly champion who wields divine magic in service of a higher power.",
               "druid" : "A priest of the Old Faith, wielding the powers of nature - moonlight and plant growth, fire and lightning - and adopting animal forms." ,
               "fighter" : "A master of martial combat, skilled with a variety of weapons and armors.",
               "monk" : "A master of martial arts, skilled with fighting hands and martial monk weapons.",
               "paladin" : "A holy warrior bound to a sacred oath.",
               "ranger" : "A master of ranged combat, one with nature.",
               "rogue" : "A scoundrel and agile warrior who uses stealth and trickery to overcome obstacles and enemies.",
               "sorceror" : "A spellcaster who draws on inherent magic from a gift or bloodline.",
               "warlock" : "A wielder of magic that is derived from a bargain with an extraplanar entity.",
               "wizard" : "A scholarly magic-user capable of manipulating the structures of reality."}
    temp = sheet

    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("Please choose a class from the following options: ")
    for c in sorted(classes):
        print("-----------------------------")
        print("Class: " + c)
        print("\nDescription: " + classes[c])
    print("-----------------------------")

    choice = input("Which class would you like to play as?\n")
    #Check to make sure the input race is valid
    if not choice in classes:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("***Please enter a valid class (capitalization matters). Try again!***")
        time.sleep(3)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        return chooseClass(sheet, rand)
    else:
        if(choice == "barbarian"):
            temp = doBarbarian(temp)
        elif(choice == "bard"):
            temp = doBard(temp)
        return temp

def updateSkillMods(sheet):
    """Takes a sheet and updates the skill modifiers."""
    temp = sheet
    for s in temp["skills"]:
        temp["skills"][s]["mod"] += temp["scores"][temp["skills"][s]["base"]]["mod"]
    return temp

def updateSaves(sheet):
    """Takes a sheet and updates the saving throws based on the ability mods."""
    temp = sheet
    for s in temp["saves"]:
        temp["saves"][s] += temp["scores"][s]["mod"]
    return temp

def updatePassives(sheet):
    """Takes a sheet and sets the passive insight, perception, and investigation."""
    temp = sheet
    for p in temp["passives"]:
        temp["passives"][p] += 10 + temp["skills"][p]["mod"]
    return temp
    
def setName(sheet):
    """Asks the player for their character's name and stores it in the sheet."""
    temp = sheet
    name = input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nLast but not least, please enter your character's name. Don't be afraid to get creative!\n")
    temp["name"] = name
    return sheet

def main():
    _ = input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nWelcome to the DnD Character Creator! We will start by choosing your character's race. Press enter to continue.")
    sheet = genSheetTemplate()
    sheet = chooseRace(sheet, False)
    _ = input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nNow, we will choose your character's class. This is the most defining aspect of your character, so choose wisely. Press enter to continue.\n")
    sheet = chooseClass(sheet, False)
    sheet = setName(updatePassives(updateSaves(updateSkillMods(doAbilityMods(sheet)))))
    printSheet(sheet)
    
if __name__ == "__main__":
    main()
