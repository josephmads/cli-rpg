# A simple, text-based game to demonstrate the use of for and while loops.
# v.2: Adding on to demonstrate sets, lists, tuples, dicts, and functions.

from random import randint as roll
import rpg_functions as rf


player_choices = {'f', 'b', 'l', 'r', 'a', 't', 's', 'i', 'h'}
choice = ""
inventory = []
equipped = []
dragon = {"hp":50, "hit":5, "damage":4, "AC":15}
health = 20
equippable = ("rusty sword", "diamond sword", "shield")
dungeon_inventory = ["key", "rusty sword", "lichen", "diamond sword", "shield"]
        

name = input("Greetings, Adventurer! What is your name?: ")

print(f"Welcome, {name}! You have entered the dungeon of the dragon. " 
    "The only ways to escape are defeating the dragon in combat or death.\n"
    "You can make the following choices in the game:\n"
    "[f]oward, [b]ack, [l]eft, [r]ight, [a]ttack, [t]ake, [s]earch, [i]nventory, [h]ealth,\n"
    "Enter the letter in brackets to perform the action.\n")

what_do = (f"{name}, what do you do?: ")

choose_again = (f"That doesn't seem to do anything here. Try another option:\n"
               "[f]oward, [b]ack, [l]eft, [r]ight, [a]ttack, [t]ake, [s]earch, [i]nventory, [h]ealth\n")

invalid_cmd = (f"Invalid command. Try one of these:\n"
              "[f]oward, [b]ack, [l]eft, [r]ight, [a]ttack, [t]ake, [s]earch, [i]nventory, [h]ealth\n")

win = None
game = True

while game == True:
    print("You stand in the entrance of the dungeon. The gate you came through has vanished. "
        "A layer of dust coats the floor. There are two doors leading out of this room. "
        "One to the left, and one to the right.")
    choice = input(what_do).lower()

    if choice == "l":
        hallway = True
        while hallway == True:
            print("You enter a long hallway. You can see a door on the left and another on the right. "
            "You will need to walk forward if you want to see what's at the end of the hallway.\n")
            choice = input(what_do).lower()

            if choice == "r":
                skel_rm = True

                while skel_rm == True and "rusty sword" not in inventory:
                    print("This room appears to be pretty much empty. The far corners are too dim to see clearly. " 
                    "The only door is the one back to the hallway.\n")
                    choice = input(what_do).lower()

                    if choice == "s":
                        print("You search the room. In one corner you find a skeleton. "
                        "The skeleton grasps a rusty sword in its bony fingers. "
                        f"{name}, will you disturb the dead and take the sword? "
                        "Or do old bones frighten you back to the hallway?\n")
                        choice = input(what_do).lower()

                        if choice == "t":
                            inventory.append("rusty sword")
                            dungeon_inventory.remove("rusty sword")
                            print(f"Several fingers snap off as you pry the sword loose. {name}, that is gross. "
                            "But you have a rusty sword now. You make your way back to the hallway...\n")
                            equip = input("Would you like to equip your rusty sword? [y/n]: ")
                            if equip == "y":
                                equipped.append("rusty sword")
                                inventory.remove("rusty_sword")
                                print("You now hold the rusty sword in your right hand.")
                            if equip == "n":
                                pass
                            skel_rm = False
                            continue

                        if choice == "b":
                            print("You say a quick prayer for the dead. {name}, you're a nice person. "
                            "You make your way back to the hallway...\n")
                            skel_rm =False
                            continue

                        if choice == "i":
                            rf.manage_inv()
                            continue

                        if choice == "h":
                            print(f"Health: {health}\n")
                            continue

                        elif choice in player_choices:
                            print(choose_again)
                            continue

                        else:
                            print(choose_again)
                            continue
                    
                    if choice == "b":
                        print("Nothing to see here. You return to the hallway...\n")
                        skel_rm = False
                        continue

                    if choice == "i":
                        print(f"Inventory: {inventory}\n")
                        continue

                    if choice == "h":
                        print(f"Health: {health}\n")
                        continue

                    elif choice in player_choices:
                        print(choose_again)
                        continue

                    else:
                        print(invalid_cmd)
                        continue

                while skel_rm == True and "rusty sword" in inventory:
                    print(f"This room appears to be empty, but you know about the bones in the shadows. "
                    "You've seen everything in here, {name}. Let the dead rest. You return to the hallway...\n")
                    skel_rm = False
                    continue

            if choice == "l":
                pit_rm = True
                while pit_rm == True:
                    if "lichen" not in inventory:
                        print("You enter a small room. In the center of the room taking up most of the space "
                        "is a round pit. A faint glow coming from the pit iluminates the room.")
                        choice = input(what_do).lower()
                    
                    if "lichen" in inventory:
                        print("You enter a small room. In the center of the room taking up most of the space "
                        "is a round pit. It is kind of dark in here.")
                        choice = input(what_do).lower()

                    if choice == "f":
                        print(f"{name}, you step forward and fall into the pit. You fall for a long time. "
                        "You have time to wonder why you did this. Eventually you hit the bottom...")
                        game = False
                        win = False
                        break

                    if choice == "s" and "lichen" not in inventory:
                        print("You lay on the floor and crawl toward the edge of the pit. A foot below the edge "
                        "you see a patch of glowing lichen on the wall of the pit.")
                        pit = input(what_do).lower()

                    if pit == "t":
                        print("You scrape off as much of the glowing lichen as you can reach. It has a very pleasant smell.\n"
                        "You put the lichen in your bag.")
                        inventory.append("lichen")
                        dungeon_inventory.remove("lichen")
                        continue

                    if choice == "s":
                        print("You look around but don't see anything else of interest.")
                        continue

                    if choice == "b":
                        print("")
                        hallway = False
                        continue

                    if choice == "i":
                        rf.manage_inv()
                        continue 

                    if choice == "h":
                        print(f"Health: {health}\n")
                        continue
                    
                    elif choice in player_choices:
                        print(choose_again)
                        continue

            else:
                print(invalid_cmd)
                continue

            if choice == "b":
                print("Too many choices! You go back...")
                hallway = False
                continue

            if choice == "i":
                rf.manage_inv()
                continue 

            if choice == "h":
                print(f"Health: {health}\n")
                continue
            
            elif choice in player_choices:
                print(choose_again)
                continue

            else:
                print(invalid_cmd)
                continue
    
    if choice == "r":
        dragon_cave = True
        while dragon_cave == True:
            print("You enter a cavernous room. In the center of the room on a mountain of gold and treasure sleeps a dragon. "
            f"The dragon cracks one eye open as you walk in. {name}, you hesitate, but maybe you can take a little gold from "
            "the edge of the pile? You take another step forward and the dragon opens its other eye and lifts its head.\n")
            choice = input(what_do).lower()

            if choice == "f":
                print(f"{name}, you stand a few feet away from the dragon's powerful jaws. It lunges forward with "
                "frightening speed. You barely dodge out of the way. You are now in combat.")
                dragon_fight = rf.combat(dragon, "dragon")
                if dragon_fight == False:
                    win = False
                    game = False
                    break
                if dragon_fight == True:
                    win = True
                    game = False
                    break
                else:
                    health = dragon_fight
                    dragon_cave = False
                    continue
            
            if choice == "a":
                print("You charge dragon. You seem to take it by surprise!")
                dragon_fight = rf.combat(dragon, "dragon")
                if dragon_fight == False:
                    win = False
                    game = False
                    break
                if dragon_fight == True:
                    win = True
                    game = False
                    break
                else:
                    health = dragon_fight
                    dragon_cave = False
                    continue
            
            if choice == "b":
                print("You slowly back out of the room. The dragon lowers its head and closes its eyes.")
                dragon_cave = False
                continue

            if choice == "i":
                rf.manage_inv()
                continue

            if choice == "h":
                print(f"Health: {health}\n")
                continue

            elif choice in player_choices:
                print(choose_again)
                continue

            else:
                print(invalid_cmd)
                continue

    if choice == "s" and "key" not in inventory:
        print("You kick the dusty floor in the entrance area. Something small clatters across the floor. You pick it up. "
        "You have found a key.\n")
        inventory.append("key")
        dungeon_inventory.remove("key")
        continue

    if choice == "s":
        print("You look around but don't see anything else of interest.")
        continue
    
    if choice == "i":
        rf.manage_inv()
        continue 

    if choice == "h":
        print(f"Health: {health}\n")
        continue
    
    elif choice in player_choices:
        print(choose_again)
        continue

    else:
        print(invalid_cmd)
        continue

if win == False:
    print(f"{name}, you have died...")

if win == True:
    print(f"Way to go, {name}! You won!!!")
