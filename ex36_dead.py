def dead(why):
    print("\n", why, "\n")
    import random
    x = random.randrange(1,10)
    if x == 1:
        print("Sad to say, you are now dead!")
    elif x == 2:
        print("You're not going to want to hear this, but you are now dead!")
    elif x == 3:
        print("You have expired and left this mortal coil.")
    elif x == 4:
        print("Such a shame, you acheived so little, but you're with the angels now!")
    elif x == 5:
        print("You gone done it now buster! You have joined the choir invisible.")
    elif x == 6:
        print("Such a short life you led, and to to so little effect.")
    elif x == 7:
        print("You have been upgraded to Heaven or Hell class. So sorry to see you go.")
    elif x == 8:
        print("Bye-bye, bye-bye, bye-byeeee. Farewell, you are no longer with us.")
    elif x == 9:
        print("Your dust has been returned to the Cosmos.")
    elif x == 10:
        print("Life was merely a fleeting dream. You are awake now and a part of the Great Conciousness.")
    exit(0)
