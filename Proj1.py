# Project 1: Adventure game
# Checkpoint 1 due Sept. 26, final version due Oct. 10. 

# open the text file into program
gamefile = open('game1.txt')

# numpy for matrix 
import numpy as np 

# init game info and map dictionaries
gameinfo = {}
mapdict = {}
npc_dict = {}

# build a dictionary containing game info
def gamebuild(gamefile):
    current_r = 0 # current room counter
    for line in gamefile:
        line = line.rstrip()
        if line != '---':
            lineparts = line.split(':')
            # following lines from in class example
            k = lineparts[0]
            v = lineparts[1].lstrip()
            if 'game_' in lineparts[0]:
                k1, k2 = k.split('_')
                gameinfo[k2] = v
                # end class example
            if 'r_id' in lineparts[0]:
                mapdict[lineparts[1]] = {'desc': '', 'id': str(lineparts[1]),'obj': []}
                current_r += 1 # adds to current_r counter 
            if 'r_desc' in lineparts[0]:
                mapdict[str(current_r)]['desc'] = lineparts[1][1:]
            if 'r_obj' in lineparts[0]:
                mapdict[str(current_r)]['obj'].append(lineparts[1][1:])
            if 'r_hiddenobj' in lineparts[0]:
                mapdict[str(current_r)]['hiddenobj'] = lineparts[1][1:]
            if 'r_hiddenpath' in lineparts[0]:
                mapdict[str(current_r)]['hiddenpath'] = lineparts[1]
            if 'r_north' in lineparts[0]:
                mapdict[str(current_r)]['north'] = lineparts[1]
            if 'r_east' in lineparts[0]:
                mapdict[str(current_r)]['east'] = lineparts[1]
            if 'r_south' in lineparts[0]:
                mapdict[str(current_r)]['south'] = lineparts[1]
            if 'r_west' in lineparts[0]:
                mapdict[str(current_r)]['west'] = lineparts[1]
            if 'npc_' in lineparts[0]: 
                k1, k2 = k.split('_', maxsplit = 1) # ex: k1 = npc_,  k2 = timmytarheel_1
                k3, k4 = k2.split('_') # ex: k3 = timmytarheel, k4= 1
                if k3 not in npc_dict: # if k3 is not a key in npc dict
                    npc_dict[k3] = {k4: v, 'count': 0} # add it as a key, populate with key value pairs for talking and 0-indexed counter key value pair
                else:
                    npc_dict[k3][k4] = v

    return gameinfo, mapdict

# build game 
gamebuild(gamefile)


# function that will enable user inputs and map movement
class Gamerun:
    def __init__(self, x, y, mapdict):
        self.mapdict = mapdict
        self.x = x 
        self.y = y
    def move(self, direction):
        global player_position
        current_x, current_y = self.get_coord(player_position)
        # check for movement overrides
        if str(player_position) in mapdict and direction in self.mapdict[str(player_position)]:
            new_position = int(self.mapdict[str(player_position)][direction])
            player_position = new_position
        # normal movement
        else:
            if direction == 'north':
                current_y = (current_y - 1) % self.y
            elif direction == 'south':
                current_y = (current_y + 1) % self.y
            elif direction == 'west':
                current_x = (current_x - 1) % self.x 
            elif direction == 'east':
                current_x = (current_x + 1) % self.x 
            else:
                print("Invalid direction!")
                return
            player_position = self.get_position(current_x, current_y)
        # update position
        print(f"You are {mapdict[str(player_position)]['desc']}")
        if mapdict[str(player_position)]['obj'] != []: # if obj list in mapdict is not empty
            print(f"There is a {mapdict[str(player_position)]['obj'][0]} here.") # print first indexed obj

    def get_coord(self, position):
        position -= 1 # 0-indexed
        x = position % self.x
        y = position // self.x 
        return x, y
    
    def get_position(self, x, y):
        return y * self.x + x + 1

# set game run variable for use below
game_run = Gamerun(int(gameinfo['xsize']), int(gameinfo['ysize']), mapdict)

# init inventory and starting location
player_position = int(gameinfo['start'])
inv = []

# Print welcome message to the game 
print('')
print(f"Welcome to {gameinfo['name']}! Good luck, traveler.")
print('')
print(f"Your goal is to {gameinfo['goal'].lower()}")
print('')
print(f"You are {mapdict[str(player_position)]['desc']}")

while True:
    print('')
    if gameinfo['goalobj'] in mapdict[str(gameinfo['goalloc'])]['obj']:
        print('Congratulations! You have won the game. Thanks for playing!')
        break
    cmd = input("What next? ")
    if cmd == 'exit': 
        break
    else:
        if cmd == "inv":
            print(f"Your inventory: {inv}")
        elif cmd == "goal":
            print(gameinfo['goal'])
        elif cmd == "search":
            if 'hiddenobj' in mapdict[str(player_position)]:
                print(mapdict[str(player_position)]['hiddenobj'])
            elif 'hiddenpath' in mapdict[str(player_position)].keys():
                print("You've found a hidden path!")
            else: 
                print('Nothing found!')
        elif cmd == "move path":
            if 'hiddenpath' in mapdict[str(player_position)]:
                player_position = int(mapdict[str(player_position)]['hiddenpath'])
                print(f"You are {mapdict[str(player_position)]['desc']}")
            else:
                print('No paths!')
        elif cmd == "check location":
            print(player_position)
        # taking and dropping objects 
        elif 'take' in cmd or 'drop' in cmd:
            cmd_parts = cmd.split()
            c1 = cmd_parts[0]
            c2 = cmd_parts[1]
            if c1 == 'take':
                if c2 in mapdict[str(player_position)]['obj']:
                    print(f"Added {mapdict[str(player_position)]['obj'][0]}")
                    inv.append(mapdict[str(player_position)]['obj'][0])
                    del mapdict[str(player_position)]['obj'][0]
                elif 'hiddenobj' in mapdict[str(player_position)]:
                    if c2 in mapdict[str(player_position)]['hiddenobj']:
                        print(f"Added {mapdict[str(player_position)]['hiddenobj']}")
                        inv.append(mapdict[str(player_position)]['hiddenobj'])
                        del mapdict[str(player_position)]['hiddenobj']
                else:
                    print(f"Can't take {c2}!")
            elif c1 == 'drop':
                if c2 in inv:
                    print(f"Dropped {c2}")
                    mapdict[str(player_position)]['obj'].append(c2)
                    inv.remove(c2)
                else:
                    print(f"Can't drop {c2}!")
        elif 'move' in cmd:
            cmd_parts = cmd.split()
            c1 = cmd_parts[0]
            c2 = cmd_parts[1]
            if c2 == 'north':
                game_run.move('north')
            elif c2 == 'south':
                game_run.move('south')
            elif c2 == 'west':
                game_run.move('west')
            elif c2 == 'east':
                game_run.move('east')
            else:
                print('Invalid direction!')
        elif 'talk' in cmd:
            cmd_parts = cmd.split()
            c1 = cmd_parts[0]
            c2 = cmd_parts[1]
            if c2 in npc_dict.keys():
                if str(player_position) == npc_dict[c2]['loc']:
                    if npc_dict[c2]['count'] + 2 < len(npc_dict[c2]):
                        print(npc_dict[c2][str(npc_dict[c2]['count'] + 1)])
                        npc_dict[c2]['count'] += 1
                    else:
                        print(npc_dict[c2][str(npc_dict[c2]['count'])])
                else:
                    pass
        