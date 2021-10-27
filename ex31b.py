print("""You enter a dark room with two doors.
Do you go through door #1, door #2 or door #3?""")
prompt = ":> "
door = input(prompt)

if door == "1":
    print("There's a giant bear here eating a cheese cake and wearing a bowler hat.")
    print("What do you do?")
    print("1 Put on a record by The Levellers")
    print("2 Scream at the bear?")
    print("3 Run you fool! Run!")

    bear = input(prompt)

    if bear == "1":
        print("""The bear listen intently to the record until 'What a Beutifull Day' comes on.
        He tells you familarity has very much bred contempt for the simplistic pseudo-Marxist ramblings of these crusty songsmiths.
        He ambles over to you very casually and proceeds to eat your face right off of your skull.
        Sorry, you look utterly horiffic as you slowly bleed to death.""")
    elif bear == "2":
        print("The bear eats your legs off, great work!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("The bear has runs away.")

elif door == "2":
    print("""You stare into the endless abyss of Cthulhu's retina.
    On the ground is a blueberry bush and a yellow jacket.
    """)
    print("1 Eat some blueberries.")
    print("2 Wear the Yellow jacket and revel in arcane conspiracy.")
    print("3 Understanding revolvers yelling melodies. Burn the bush down and return Cthulhu's jacket to him.")

    insanity = input(prompt)

    if insanity == "1" or insanity == "2":
        print("Your body survives but powered by a mind of jello.")
        print("You go on to run a crypto hedge fund.")
    else:
        print("The insanity rots your eyes from the inside out.")
        print("""You gain deep insights into things deeply hidden since the beginning of time.
        You travel back in time to 1985 and have a hit single about these insights and collapse after appearing on Top of the Pops.
        You die alone in the Green Room at BBC Television Centre while everyone else gyrates to the latest warblings from Shaking Stevens. """)

elif door == "3":
    print("You find yourself in the lobby of a luxuary hotel somewhere in the high Alps.")
    print("You are offered a tray of drinks and chocolates. Do you:")
    print("1 Select a warming cognac and a fine cigar from the tray.")
    print("2 Select a negroni and some milk chocolates.")
    print("3 Ignore the proffered comestables and ask to speak to the manager.")

    hotel = input(prompt)

    if hotel == "1":
        print("""You put the cigar in your pocket for later and sitting yourself
        in a large leather armchair you drink the cognac and fall asleep.
        When you awake you realise to your consternation that you have been
        turned into a human fly (though you don't know why).
        You think your name may be Gregor Samsa, but you're not sure.
        """)
    elif hotel == "2":
        print("""You drink the negroni and eat the chocolates while checking in.
        You have a lovely stay and never know just how lucky you are.
        """)
    elif hotel == "3":
        print("You are taken to see the bear.")
    else:
        print("You are taken to see the bear.")

else:
    print("You stumble around in the dark and fall on a knife and die. Are you happy with the choices you made in life?")
