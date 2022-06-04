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

from random import randint as roll

player_choices = {'f', 'b', 'l', 'r', 'a', 't', 's', 'i', 'h'}
choice = ""
inventory = []
equipped = []
dragon = {"hp":50, "hit":5, "damage":4, "AC":15}
health = 20
equippable = ("rusty sword", "diamond sword", "shield")
dungeon_inventory = ["key", "rusty sword", "lichen", "diamond sword", "shield"]

def manage_inv():
    """Function to allow player to manage inventory,
    equip items, or drops items.

    Returns:
        str: returns player to current location in the dungeon.
    """

    back = "You pull you head out of your bag..."
    print(f"Inventory: {inventory}\n")
    choice = input("Would you like to manage your inventory? [y/n]: ")
    if choice == "n":
        return print(back)
    if choice == "y":
        manage = True
        while manage == True:
            choice = input("You can [d]rop, [e]quip, [u]neqip, [c]onsume an item, or [r]eturn to game: ")
            if choice == "d":
                drop = input("Enter the item to drop: ")
                inventory.remove(drop)
                dungeon_inventory.append(drop)
                print(f"{drop} is no longer in your inventory. As soon as it hits the floor, "
                "a strange magic zips the {drop} away toward where you first found it.")
            if choice == "e":
                equip = input("Enter the item to equip: ")
                if len(equipped) < 2 and equip in equippable:
                    inventory.remove(equip)
                    equipped.append(equip)
                    print(f"You are now holding {equip} in your hand.")
                    continue
                elif len(equipped) > 2:
                    print("Your hands are full. Try unequipping an item first.")
                    continue
                else:
                    print("That item is not equippable.")
                    continue
            if choice == "u":
                print(f"You are currently equipped with the following: {equipped}")
                unequip = input("Enter the item to unequip: ")
                equipped.remove(unequip)
                inventory.append(unequip)
                print(f"{unequip} is back in your inventory.")
                continue
            if choice == "c":
                consume = input("Enter item to consume: ")
                if consume == "lichen":
                    health = health + 5
                    inventory.remove(consume)
                    print(f"That tasted gross, but you feel much better! Your health is now: {health}")
                    continue
                else:
                    print("You can't consume that item.")
                    continue
            if choice == "r":
                manage = False
                return print(back) 
               
def combat(enemy, enemy_name):
    player_hp = health
    if "rusty sword" in equipped:
        player_hit = 1 
        player_dmg = 2
    if "diamond sword" in equipped:
        player_hit = 5
        player_dmg = 10
    else:
        player_hit = 0
        player_dmg = 0
    if "shield" in equipped:
        player_ac = 15
    else:
        player_ac = 12

    enemy_hp = enemy["hp"]
    enemy_ac = enemy["AC"]
    enemy_hit = enemy["hit"]
    enemy_dmg = enemy["damage"]
   
    while player_hp > 0 and enemy_hp > 0:
        player_turn = True
        while player_turn == True:
            choice = input("Press ENTER to roll your attack, or go [b]ack: ")
            if choice == "b":
                player_turn = False
                return player_hp
            player_roll = roll(1,20) + player_hit
            if player_roll > enemy_ac:
                p_damage = roll(1,10) + player_dmg
                enemy_hp -= p_damage
                print(f"You hit the {enemy_name} for {p_damage} points of damage!")
                player_turn = False
                continue
            else:
                print(f"You miss the {enemy_name}.")
                player_turn = False
                continue

        input("Press ENTER to continue...")

        enemy_turn = True
        while enemy_turn == True:
            print(f"The {enemy_name} attacks!")
            enemy_roll = roll(1,20) + enemy_hit
            if  enemy_roll > player_ac:
                e_damage = roll(1,10) + enemy_dmg
                player_hp -= e_damage
                print(f"The {enemy_name} hit you for {e_damage} points of damage!")
                enemy_turn = False
                continue
            else:
                print(f"The {enemy_name} missed!")
                enemy_turn = False
                continue
    
    if player_hp <= 0:
        return False

    if enemy_hp <= 0:
        return True

        

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
                            manage_inv()
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
            print("You enter a cavernous room. In the center of the room on a mountain of gold and treasure sleeps a dragon. "
            f"The dragon cracks one eye open as you walk in. {name}, you hesitate, but maybe you can take a little gold from "
            "the edge of the pile? You take another step forward and the dragon opens its other eye and lifts its head.\n")
            choice = input(what_do).lower()

            if choice == "f":
                print(f"{name}, you stand a few feet away from the dragon's powerful jaws. It lunges forward with "
                "frightening speed. You barely dodge out of the way. You are now in combat.")
                dragon_fight = combat(dragon, "dragon")
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
                dragon_cave = False
                continue

            if choice == "i":
                manage_inv()
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
        continue

    if choice == "s":
        print("You look around but don't see anything else of interest.")
        continue
    
    if choice == "i":
        manage_inv()
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
