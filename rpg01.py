#!/usr/bin/python3

"""RPG Game
   Author: Clinton Robertson"""
import os

import requests
import time


def clear_screen():
    # Creating function to clear screen
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def show_instructions():
    # print a main menu and the commands
    print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
''')


def passport_status():
    """This function will grab directions from the current room so, your passport will display the directions you can
    travel in """

    passport = []
    for item in rooms[currentRoom]:
        if item == "north" or item == "south" or item == "east" or item == "west":
            passport.append(item.title())

    if len(passport) == 1:
        print(f"Passport: You can travel {passport[0]}")
    elif len(passport) == 2:
        print(f"Passport: You can travel {passport[0]} or {passport[1]}")
    elif len(passport) == 3:
        print(f"Passport: You can travel {passport[0]}, {passport[1]} or {passport[2]}")
    else:
        print(f"Passport: You can travel {passport[0]}, {passport[1]}, {passport[2]} or {passport[3]}")


def show_status():
    # print the player's current status
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print the current inventory
    print('Inventory : ' + str(inventory))
    # displays directions you allowed to travel in
    passport_status()
    # print an item if there is one
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")


# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other rooms
rooms = {

    'Hall': {
        'south': 'Kitchen',
        'west': 'Bathroom',
        'east': 'Dining Room',
        'item': 'key'
    },

    'Bathroom': {
        'east': 'Hall',
        'south': 'Bedroom',
        'item': 'mirror'
    },

    'Bedroom': {
        'north': 'Bathroom',
        'item': 'statue',
    },

    'Kitchen': {
        'north': 'Hall',
        'item': 'monster',
    },
    'Dining Room': {
        'west': 'Hall',
        'south': 'Garden',
        'item': 'potion',
        'north': 'Pantry',
    },
    'Garden': {
        'north': 'Dining Room'
    },
    'Pantry': {
        'south': 'Dining Room',
        'item': 'cookie',
    }
}

# start the player in the Hall
currentRoom = 'Hall'

show_instructions()

# loop forever
while True:
    show_status()

    # get the player's next 'move'
    # .split() breaks it up into an list array
    # eg typing 'go east' would give the list:
    # ['go','east']
    move = ''
    while move == '':
        move = input('>')
        clear_screen()

    # split allows an items to have a space on them
    # get golden key is returned ["get", "golden key"]
    move = move.lower().split(" ", 1)

    # if they type 'go' first
    if move[0] == 'go':
        # check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            # set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    # if they type 'get' first
    if move[0] == 'get':

        # If you are in the bedroom and try to get the statue you will activate the 'All Knowing Spinx and receive a
        # random cat fact
        if currentRoom == 'Bedroom' and move[1] in rooms[currentRoom]['item']:
            print("You have activated the All-knowing Sphinx")
            r = requests.get("https://the-cat-fact.herokuapp.com/api/randomfact")
            facts = r.json()
            print(facts["data"][0]["fact"])
        # If current room is the Bathroom and you try to get the mirror you activate a portal that allows you to
        # teleport
        if currentRoom == 'Bathroom' and move[1] in rooms[currentRoom]['item']:
            clear_screen()
            print("You are bending time itself")
            print("Loading...")
            time.sleep(2)
            clear_screen()
            print("Traveling through the wormhole...")
            print("Loading......")
            time.sleep(2)
            clear_screen()
            print("Almost there.....")
            print("Loading............")
            time.sleep(2)
            clear_screen()
            num = 0
            while num == 0:
                try:
                    print("Teleportation Activated")
                    num = float(input("Pick a number from 1 - 7\n> "))
                    num = int(num)
                    if num < 1 or num > 7:
                        num = 0
                    else:
                        time.sleep(3)
                        break
                except:
                    print("Invalid number!")
                    num = 0

            if num == 1:
                currentRoom = "Pantry"
            elif num == 2:
                currentRoom = "Garden"
            elif num == 3:
                currentRoom = "Dining Room"
            elif num == 4:
                currentRoom = "Kitchen"
            elif num == 5:
                currentRoom = "Bedroom"
            elif num == 6:
                currentRoom = "Bathroom"
            elif num == 7:
                currentRoom = "Hall"

        # if the room contains an item, and the item is the one they want to get
        elif "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            # add the item to their inventory
            inventory += [move[1]]
            # display a helpful message
            print(move[1] + ' got!')
            # delete the item from the room
            del rooms[currentRoom]['item']
        # otherwise, if the item isn't there to get
        else:
            # tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    # Define how a player can win
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break

    # If a player enters a room with a monster
    elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A monster has got you... GAME OVER!')
        break

