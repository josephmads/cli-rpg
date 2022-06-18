# Functions for dragon_rpg.py


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

