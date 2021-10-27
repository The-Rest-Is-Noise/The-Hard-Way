print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cheese cake?")
    print("2. Scream at the bear?")

    bear = input("> ")

    if bear == "1":
        print("The bears eats your face off, Dummass!")
    elif bear == "2":
        print("The bear eats your legs off, great work!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("The bear has runs away.")

elif door == "2":
    print("You stare into the endless abyss of Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket conspiracy.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job numb nuts!")
    else:
        print("The insanity rots your eyes from the inside out.")
        print("Good luck with that!")

else:
    print("You stumble around in the dark and fall on a knife and die. Are you happy with the choices you made in life?")
