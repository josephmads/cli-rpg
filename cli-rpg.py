# A simple, text-based game to demonstrate the use of for and while loops.

name = input("Greetings, Adventurer! What is your name?: ")

text1 = (f"There are two doors leading out of this room. "
        "One to the [l]eft and one to the [r]ight. Where to?: ")
text2 = "Now what? Do you go [b]ack, or [l]ook around?: "
text3 = ("You search the room. In one corner you find a skeleton. "
        "The skeleton grasps a shiny sword in its bony fingers. "
        f"Will you disturb the dead, {name}, and [t]ake the sword, " 
        "or [l]eave it be?: ")
text4 = (f"What will you do, {name}? You could [r]un away like a coward, "
        "or stand and [f]ight like a warrior!")
sword = False
choice = ""
choose_again = "You can't do that. Try a [letter].\n"

print(f"Welcome, {name}! You have been drugged and awaken in this dungeon! Can you escape?\n")

while choice != "r" or "l":
    choice = input(text1)
    if choice == "l":
        print("This room appears to be empty. ")
        while choice != "b" or "l":
            choice = input(text2)
            if choice == "b":
                choice = input(text1)
            elif choice == "l":
                while choice != "t" or "l":
                    choice = input(text3)
                    if choice == "t":
                        print(f"Several fingers snap off as you pry the sword loose. {name}, that is gross. "
                            "But you have a sword now. You make your way back to the room where you woke up.\n")
                        sword = True
                        choice = input(text1)
                    elif choice == "l":
                        print(f"You say a quick prayer for the dead. {name}, you are a nice person. "
                            "As you make your way back to the room where you woke up you can't shake the "
                            "feeling that nice people don't always end up well.\n")
                        choice = input(text1)
                    else:
                        print(choose_again)
            else:
                print(choose_again)                

    elif choice == "r":
        print(f"Watch out, {name}! There is a terrible dragon in here!!!")
        choice = input(text4)
        while choice != "r" or "f": 
            if choice == "r":
                choice = input(text1)
            elif choice == "f" and sword == True:
                print(f"{name}, you fight the dragon. It is an epic battle. I don't have the time to go into "
                    "all the details. At the end, you dodge a blast of fire and plunge the shiny sword into "
                    "the dragon's soft underbelly. You win!!!")
                break
            elif choice == "f" and sword == False:
                print("You try to fight the dragon with your bare hands. You get burnt to a crisp "
                    f"and the dragon eats you for a snack. {name}, what did you think would "
                    "happen without a sword? You lose...")
                break
            else:
                print(choose_again)

    
    

