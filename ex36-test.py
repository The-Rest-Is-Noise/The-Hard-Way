prompt = ":> "

print("Enter an integer", prompt)
user_input = input()

def is_int(value):
    try:
        int(value)
        input_is_int = True
    except ValueError:
        input_is_int = False
    return input_is_int

valid_value = is_int(user_input)
if valid_value == True:
    print("That was some good integer, thank your Ser.")
else:
    print("Man, that was some bad integer Ian!")
    exit(0)

#if choice_is_Int and how_much_gold < 50:
    #print("Nice, you're not so greedy my friend, looks like you win!")
    #exit(0)
#else:
    #dead("You Greedy bastard!")

print(valid_value)
