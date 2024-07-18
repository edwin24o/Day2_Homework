#task number one

place = input("Choose a place: forest or cave? ")

if place == "forest":  #added =
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":  #added =
        print("You found a bird's nest!") 
    elif action == "cross a river": #added = and changed else to elif
        print("You found a boat!")
    else:
        pass 
elif place == "cave":  #added =
    print("You find a hidden treasure!")
    action = input("light a torch or proceed in the dark? ") #Task2 added input action of torch
    if action == "light a torch":
        print("You find a hidden treasure!")
    elif action == "proceed in the dark":
        print("You are blind sided by a goblin!")
    else:
        pass