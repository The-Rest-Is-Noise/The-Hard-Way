# this version tries to use def to tidy up the code and make some callable routines
prompt = ":> "

def door_1():
    print("Door 1")
    print("Pick: 1 or 2")
    bear = input(prompt)
    if bear == "1":
        print("Bear 1")
    elif bear == "2":
        print("Bear 2")
    else:
        print("Not Bear")

def door_2():
    print("Door 2")
    print("Pick: 1 or 2")
    insanity = input(prompt)
    if insanity == "1" or insanity == "2":
        print(f"Insanity {insanity}")
    else:
        print("Not insanity")

def door_3():
    print("Door 3")
    print("Pick: 1 or 2")
    hotel = input(prompt)
    if hotel == "1":
        print("Hotel 1")
    elif hotel == "2":
        print("Hotel 2")
    elif hotel == "3":
        print("You are taken to see the bear.")
        door_1()
    else:
        print("You are taken to see the bear.")
        door_1()

print("""Pick: 1, 2 or 3""")
door = input(prompt)

if door == "1":
    door_1()

elif door == "2":
    door_2()

elif door == "3":
    door_3()

else:
    print("You stumble around in the dark and fall on a knife and die. Are you happy with the choices you made in life?")
