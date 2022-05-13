# A simple, text-based game to demonstrate the use of for and while loops.
# v.2: Adding on to demonstrate sets, lists, tuples, and dicts.

# - Save the user input options you allow e.g. in a set that 
# you can check against when your user makes a choice.
# - Create an inventory for your player, where they can add and remove items.
# - Players should be able to collect items they find in rooms and add them to their inventory.
# - If they lose a fight against the dragon, then they should lose their inventory items.
# - Add more rooms to your game and allow your player to explore.
# - Some rooms can be empty, others can contain items, and yet others can contain an opponent.
# - Implement some logic that decides whether or not your player can beat the opponent 
# depending on what items they have in their inventory
# - Use the random module to add a multiplier to your battles, similar to a dice roll in a real game. 
# This pseudo-random element can have an effect on whether your player wins or loses when battling an opponent.

name = input("Greetings, Adventurer! What is your name?: ")
player_choices = {'f', 'b', 'l', 'r', 'a', 't', 's', 'i', 'h'}
choice = ""
inventory = []
health = 10

entry = ("You stand in the entrance of the dungeon. The gate you came has vanished. "
        "There are two doors leading out of this room. One to the left, and one to the right.")
what_do = (f"{name}, what do you do?: ")
choose_again = (f"That doesn't seem to do anything here. Try another option:\n"
               "[f]oward, [b]ack, [l]eft, [r]ight, [a]ttack, [t]ake, [s]earch, [i]nventory, [h]ealth\n")
invalid_cmd = (f"Invalid command. Try one of these:\n"
              "[f]oward, [b]ack, [l]eft, [r]ight, [a]ttack, [t]ake, [s]earch, [i]nventory, [h]ealth\n")
game = True

print(f"Welcome, {name}! You have entered the dungeon of the dragon. " 
    "The only ways to escape are defeating the dragon in combat or death.\n"
    "You can make the following choices in the game:\n"
    "[f]oward, [b]ack, [l]eft, [r]ight, [a]ttack, [t]ake, [s]earch, [i]nventory, [h]ealth,\n"
    "Enter the letter in brackets to perform the action.\n")



while game == True:
    print(entry)
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
                            print(f"Several fingers snap off as you pry the sword loose. {name}, that is gross. "
                            "But you have a rusty sword now. You make your way back to the hallway...\n")
                            skel_rm = False
                            continue

                        if choice == "b":
                            print("You say a quick prayer for the dead. {name}, you're a nice person. "
                            "You make your way back to the hallway...\n")
                            skel_rm =False
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
    
    if choice == "r":
        dragon_cave = True
        while dragon_cave == True:
            print(f"You enter a cavernous room. In the center of the room on a mountain of gold and treasure sleeps a dragon. "
            "The dragon cracks one eye open as you walk in. {name}, you hesitate, but maybe you can take a little gold from "
            "the edge of the pile? You take another step forward and the dragon opens its other eye and lifts its head.\n")
            choice = input(what_do).lower()

    if choice == "s" and "key" not in inventory:
        print("You kick the dusty floor in the entrance area. Something small clatters across the floor. You pick it up. "
        "You have found a key.\n")
        inventory.append("key")
        continue

    if choice == "s":
        print("You look around but don't see anything else of interest.")
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

