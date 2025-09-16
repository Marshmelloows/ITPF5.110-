from copy import deepcopy
from random import randint














}

#data structureof enimey types
enemies:dict ={
    "names":
    "toontype": []
    "HP":
    "MP":
    "weapions": ["club"]
    "skills":
    "attributes": [[100,]
                   [200,]
                   [200,]
                   [500,]
                   [200,10, 1, 1, 5],
                   ]
}

def makeToon():
    ndx = randint(0,4)
    toon["name"] = enemies["names"][ndx]
    toon["location"] = [randint(0,30), randint(0,28),1]
    toon["HP"] = enemies["HP"][ndx]
    toon["MP"] = enemies["MP"][ndx]
    toon["toontype"] = enemies["toontype"][ndx]
    #add other attributes to coppy over
    return toon


enemies =[]
for _ in range(10):
    enemies.append(deepcopy(makeToon))
        
for i,v in enumerate(enemies):
    print(f"{i}: {v["name"] = }, {v["location] = } ")
sys.exit()





















#create a list with on of each hero, including the player
for i in range(5:)




























#create a list of 10 random enimeyses