from sys import exit
prompt = "> "

def gold_room():
    print("This room is full of gold. How much gold do you take?")
    choice = (input(prompt))

    try:
        int(choice)
        choice_is_Int = True
    except ValueError:
        choice_is_Int = False

    if choice_is_Int == True:
        how_much_gold = int(choice)
    else:
        dead("Man, learn to type a number!")

    if choice_is_Int and how_much_gold < 50:
        print("Nice, you're not so greedy my friend, looks like you win!")
        exit(0)
    else:
        dead("You Greedy bastard!")

def bear_room():
    print("There is a bear in here!")
    print("The bear has a bunch of honey.")
    print("That fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input(prompt)
        if choice == "take honey.":
            dead("The bear looks at you then slaps your face clean off!")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear moved from the door")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear is pissed and chews your leg off!")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I huvnae got a clue whit yer on aboot ya prick!")

def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever, stares at you and you go insane.")
    print("Do you flee for your life or eat yor own head?")

    choice = input(prompt)

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well i hope that was tasty!")
    else:
        cthulhu_room()

def dead(why):
    print(why, "Good Job!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to the right and the left of you.")
    print("Which one do you go through?")
    choice = input(prompt)
    if choice == "left":
        bear_room()
    elif choice == "right":
         cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

start()
