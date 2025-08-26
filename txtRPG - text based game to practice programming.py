


#stats for 
attSTR = 0
attAGI = 0
attINT = 0
attCHR = 0


#my dictionary for my player stats and attributes.
Mike_dict = {
    "name": "Mike",
    "Level": 10,
    "type": "",
    "hp": 100,
    "mp": 20,
    "Location": [0, 0, 0,], #X,Y,Z
    "Skills": [],
    "Inventory": [],
    # "attributes": [0,0,0,0,0], #harder to read
    #"attributes": [attSTR, attAGI, attINT, attCHR,],
    "attributes": [10, 50, 23, 13, 18],
}

#Enemies
Enemies: list[dict] = [Orc, Troll, Goblin, Oger]
#Heroes
Heroes: list[dict] = [Mage, Fighter, Archer, Healer, Player]


#Heroes 

#npc1
Zury_dict = {
    "name": "Zury",
    "Level": 0,
    "type": "mage",
    "hp": 100,
    "mp": 20,
    "Location": [0, 0, 0,], #X,Y,Z
    "Skills": [],
    "Inventory": [],
    # "attributes": [0,0,0,0,0], #harder to read
    #"attributes": [attSTR, attAGI, attINT, attCHR,],
    "attributes": [0, 0, 0, 0, 0],
}
#npc2
Gildore_dict = {
    "name": "Gildore",
    "Level": 0,
    "type": "Fighter",
    "hp": 100,
    "mp": 20,
    "Location": [0, 0, 0,], #X,Y,Z
    "Skills": [],
    "Inventory": [],
    # "attributes": [0,0,0,0,0], #harder to read
    #"attributes": [attSTR, attAGI, attINT, attCHR,],
    "attributes": [0, 0, 0, 0, 0],
}
#npc3
Moglif_dict = {
    "name": "Moglif",
    "Level": 10,
    "type": "Archer",
    "hp": 200,
    "mp": 30,
    "Location": [0, 0, 0,], #X,Y,Z
    "Skills": [],
    "Inventory": [],
    # "attributes": [0,0,0,0,0], #harder to read
    "attributes": [attSTR, attAGI, attINT, attCHR,],
    # "attributes": [attSTR:0, attAGI:0, attINT:0, attCHR:0, attLCK:0],
}
#npc4
Smegol1_dict= {
    "name": "Smegol",
    "Level": 10,
    "type": "",
    "hp": 100,
    "mp": 50,
    "Location": [0, 0, 0,], #X,Y,Z
    "Skills": [],
    "Inventory": [],
    # "attributes": [0,0,0,0,0], #harder to read
    "attributes": [attSTR, attAGI, attINT, attCHR,],
    # "attributes": [attSTR:0, attAGI:0, attINT:0, attCHR:0, attLCK:0],
}
#npc5
Smegol2_dict= {
    "name": "",
    "Level": 0,
    "type": "",
    "hp": 100,
    "mp": 50,
    "Location": [0, 0, 0,], #X,Y,Z
    "Skills": [],
    "Inventory": [],
    # "attributes": [0,0,0,0,0], #harder to read
    "attributes": [attSTR, attAGI, attINT, attCHR,],
    # "attributes": [attSTR:0, attAGI:0, attINT:0, attCHR:0, attLCK:0],
}
#npc6
Smegol3_dict= {
    "name": "",
    "Level": 0,
    "type": "",
    "hp": 100,
    "mp": 50,
    "Location": [0, 0, 0,], #X,Y,Z
    "Skills": [],
    "Inventory": [],
    # "attributes": [0,0,0,0,0], #harder to read
    "attributes": [attSTR, attAGI, attINT, attCHR,],
    # "attributes": [attSTR:0, attAGI:0, attINT:0, attCHR:0, attLCK:0],
}
#npc7
Smegol4_dict= {
    "name": "",
    "Level": 0,
    "type": "",
    "hp": 100,
    "mp": 50,
    "Location": [0, 0, 0,], #X,Y,Z
    "Skills": [],
    "Inventory": [],
    # "attributes": [0,0,0,0,0], #harder to read
    "attributes": [attSTR, attAGI, attINT, attCHR,],
    # "attributes": [attSTR:0, attAGI:0, attINT:0, attCHR:0, attLCK:0],
}
#npc8
Smegol5_dict= {
    "name": "",
    "Level": 0,
    "type": "",
    "hp": 100,
    "mp": 50,
    "Location": [0, 0, 0,], #X,Y,Z
    "Skills": [],
    "Inventory": [],
    # "attributes": [0,0,0,0,0], #harder to read
    "attributes": [attSTR, attAGI, attINT, attCHR,],
    # "attributes": [attSTR:0, attAGI:0, attINT:0, attCHR:0, attLCK:0],
}
#npc9
Smegol6_dict= {
    "name": "",
    "Level": 0,
    "type": "",
    "hp": 100,
    "mp": 50,
    "Location": [0, 0, 0,], #X,Y,Z
    "Skills": [],
    "Inventory": [],
    # "attributes": [0,0,0,0,0], #harder to read
    "attributes": [attSTR, attAGI, attINT, attCHR,],
    # "attributes": [attSTR:0, attAGI:0, attINT:0, attCHR:0, attLCK:0],
}


#movement in x and y axsies
def Move(move):
    #from tandom import randint - add at the top of the file 
    move["location"][0] += randint (-2, 2) # x. #allows the movement on the x axies. left and right.
    move["location"][1] += randint (-2, 2) # y. #allos the movement in on the y axies. up and down.
