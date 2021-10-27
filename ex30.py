people = 30
cars = 5
trucks = 4


if (cars * 4) >= people:
    print("We could take the cars.")
else:
    print("We can't take the cars, too few!")


if (trucks * 2) >= (people):
    print("We have enough trucks.")
elif (trucks * 2) < people:
    print("We don't have enough trucks either!")

if people > (trucks * 2) + (cars * 4):
    print("Oh man, better call some taxis!")
else:
    print("Time to mix and match.")
