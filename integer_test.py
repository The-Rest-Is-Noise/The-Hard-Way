prompt = ":> "

print("Enter an integer", prompt)
user_input = input()

def is_int(user_input):
    try:
        int(user_input)
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
