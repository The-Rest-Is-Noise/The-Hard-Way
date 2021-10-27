from sys import exit
import time
prompt = "> "

def is_int(user_input):
    try:
        int(user_input)
        input_is_valid = True
    except ValueError:
        input_is_valid = False
    return input_is_valid


def gold_room():
    print("This room is full of gold. How much gold do you take?")
    choice = (input(prompt))

    choice_is_int = is_int(choice)

    if choice_is_int == True:
        how_much_gold_taken = int(choice)
    else:
        dead("Man, learn to type a number!")

    if (choice_is_int) and (how_much_gold_taken < 50):
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
        if choice == "th":
            dead("The bear looks at you then slaps your face clean off!")
        elif choice == "tb" and not bear_moved:
            print("The bear moved from the door")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "tb" and bear_moved:
            dead("The bear is pissed and chews your leg off!")
        elif choice == "od" and bear_moved:
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


def start_room():
    print("It is a dark and stormy night.")
    print("You find yourself in a room, dimly lit.")
    print("There is one door to the right of you, and one door to the left.")
    print("Which one do you go through, *left* or *right*?")
    choice = input(prompt)
    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        print("You stumble around the room wet, cold and hungry.")
        print("Will you take the call to adventure?")
        print("Will you choose *left* or *right*?")
        choice = input(prompt)
        if choice == "left":
            bear_room()
        elif choice == "right":
            cthulhu_room()
        else:
            dead("You die from boredom, so sad your life!")

#------------------------------------------------------------

start_room()
