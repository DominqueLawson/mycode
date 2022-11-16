#!/usr/bin/python3
"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""

import time 

def showInstructions():
    """Show the game instructions when called"""
    # print a main menu and the commands
    print('''
    RPG Game
    ========
    Get to the Garden with a key and a potion to win! But first you must kill the monster! 
    Commands:
      go [direction]
      get [item]
    ''')


def showStatus():
    """determine the current status of the player"""
    # print the player's current location
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print what the player is carrying
    print('Inventory:', inventory)
    # check if there's an item in the room, if so print it
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")

def trapDoor():
    """ lets player know they just enter a trap and only way out is to answer a riddle correctly"""
    #print out that they are trapped in the room
    print('---------------------------')
    print('''You are trapped in the ' + currentRoom + 'the only way to get out the room is to answer the riddle correctly. You have 3 attempts at getting the riddle correct. If you get it correct you will be teleported to the Hall. If you get it incorrect, you will be teleported to the monster\s location. ''')
    print('---------------------------')
    
    #count for each attempt
    count = 0
    #keep track of the attempts 
    while count < 3:
        count += 1
        #present the riddle as input
        answer = input(" What is so fragile that saying its name breaks it? ")
        #make sure the answer is lowercase and stripped of spaces
        answer = answer.lower().strip()
        #how to treat the answers
        if answer == 'silence':
            print('You are correct. You will now be teleported to the Hall')
            return 'Hall' 
        # if attempted 3 times send to monster
        elif count == 3 :
            print('That was your 3rd try. You will be sent to the monster. Good Luck!!!')
            return 'Kitchen' 
        else :
            print('Wrong, try again!')

# an inventory, which is initially empty
inventory = []

# A dictionary linking a room to other rooms
rooms = {

    'Hall': {
        'north': 'Bedroom',
        'south': 'Kitchen',
        'east': 'Dining Room',
        'item': 'key'
    },

    'Kitchen': {
        'north': 'Hall',
        'item': 'monster',
    },

    'Bedroom': {
        'north': 'Attic',
        'south': 'Hall',
        'east': 'Patio',
        'item' : 'sword'
    },

    'Attic': {

    },

    'Patio': {
        'west': 'Bedroom',
        'south': 'Dining Room'
    },

    'Dining Room': {
        'north': 'Patio',
        'west': 'Hall',
        'south': 'Garden',
        'item': 'potion'
    },

    'Garden': {
        'north': 'Dining Room'
    }
}


# start the player in the Hall
currentRoom = 'Hall'

showInstructions()

# breaking this while loop means the game is over
while True:
    showStatus()

    # the player MUST type something in
    # otherwise input will keep asking
    move = ''
    while move == '':
        move = input('>')

    # normalizing input:
    # .lower() makes it lower case, .split() turns it to a list
    # therefore, "get golden key" becomes ["get", "golden key"]
    move = move.lower().split(" ", 1)

    # if they type 'go' first
    if move[0] == 'go':
        # check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            # set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # if they aren't allowed to go that way:
        else:
            print('You can\'t go that way!')

    # if they type 'get' first
    if move[0] == 'get':
        # make two checks:
        # 1. if the current room contains an item
        # 2. if the item in the room matches the item the player wishes to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            # add the item to their inventory
            inventory.append(move[1])
            # display a helpful message
            print(move[1] + ' got!')
            # delete the item key:value pair from the room's dictionary
            del rooms[currentRoom]['item']
        # if there's no item in the room or the item doesn't match
        else:
            # tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    #if they type 'fight' first
    if move[0] == 'fight':        
        # make two checks:
        # 1. if the current room contains an item
        # 2. if the item in the room matches is a monster
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item'] and move[1] == 'monster':
           
            # display the battle in a message
            print('You draw your sword to fight the monster')
            time.sleep(2)
            print('Oh no!! You have just been knocked to the ground')
            time.sleep(2)
            print('In one swift agile move you are able to get to your feet and cut off the monster\s head. YOU ARE VICTORIOUS!!!!') 
            # add the item to their inventory
            inventory.append('monsterhead')
            # delete the item key:value pair from the room's dictionary
            del rooms[currentRoom]['item']
        # if there's no item in the room or the item doesn't match
        else:
            # tell them they can't fight it
            print('Can\'t fight ' + move[1] + '!')

        #if a player enters the Attic
    if currentRoom == 'Attic' :
        currentRoom = trapDoor()         

        # If a player enters a room with a monster
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item'] and 'sword' in inventory:
        print('A monster is coming towards you!!!! Rooooaaaarrrr!!! Use your sword to fight by entering: fight monster')   
    elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item'] :    
        print('A monster has got you... GAME OVER!')
        break

        # Define how a player can win
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory and 'monsterhead' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break
