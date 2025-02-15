import time
from random import randint
from newline import newline
# import rng module
# import [socket] when making servers
def rng():
    global rnglist
    rnglist = []
    i = 50
    while i > 0:
        rnglist.append('Common')
        i -= 1
    i = 24
    while i > 0:
        rnglist.append('Uncommon')
        i -= 1
    i = 15
    while i > 0:
        rnglist.append('Rare')
        i -= 1
    i = 7
    while i > 0:
        rnglist.append('Epic')
        i -= 1
    i = 3
    while i > 0:
        rnglist.append('Legendary')
        i -= 1
    i = 1
    while i > 0:
        rnglist.append('Mythical')
        i -= 1
    newline()
    result = rnglist[randint(0, 99)]
    return result
#make trading server
collection = []
action = ""
while action.upper() != 'END':
    action = input("Choose an action: ")
    if action.upper() == 'ROLL': 
        rolls = int(input("How many times do you want to roll for Crystals? "))
        while rolls > 0:
            collection.append(rng()) 
            print(f"You got: {collection[-1]}")
            time.sleep(1)
            rolls -= 1
        newline()
        print(collection)
        newline()
    elif action.upper() == 'CHANCES':
        print(f"Chance to get Common Crystals: {rnglist.count('Common')}")
        print(f"Chance to get Uncommon Crystals: {rnglist.count('Uncommon')}")
        print(f"Chance to get Rare Crystals: {rnglist.count('Rare')}")
        print(f"Chance to get Epic Crystals: {rnglist.count('Epic')}")
        print(f"Chance to get Legendary Crystals: {rnglist.count('Legendary')}")
        print(f"Chance to get Mythical Crystals: {rnglist.count('Mythical')}")
        newline()
    elif action.upper() == 'COLLECTION':
        print(f"Here is your Crystal collection: \n{' '.join(collection)}")
        newline()
        print(f"You have {collection.count('Common')} Common Crystals")
        print(f"You have {collection.count('Uncommon')} Uncommon Crystals")
        print(f"You have {collection.count('Rare')} Rare Crystals")
        print(f"You have {collection.count('Epic')} Epic Crystals")
        print(f"You have {collection.count('Legendary')} Legendary Crystals")
        print(f"You have {collection.count('Mythical')} Mythical Crystals")
        newline()
    elif action.upper() == 'CRAFT':
        print("Action not yet made")
        newline()
    elif action.upper() == 'SAVE':
        print("Saving, please be patient...")
        #save in a savegame file
        time.sleep(1)
        print("Saving complete")
        newline()
    elif action.upper() == 'LOAD':
        print("Loading, please be patient...")
        #load from the savegame file
        time.sleep(1)
        print("Loading complete")
        newline()
    elif action.upper() == 'TRADE':
        print("Action not yet made")
        #find players in trading queue
        newline()
    elif action.upper() == 'END':
        print("\nProgram closed")
    elif action.upper() == 'HELP':
        print("Here are the list of actions:\n\nroll - roll for Crystals\nchances - see chances to roll Crystal rarities\n")
        newline()
    else: 
        print("That action does not exist. Use 'help' to see a list of actions")
        newline()


