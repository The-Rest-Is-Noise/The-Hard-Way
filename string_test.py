prompt = ":> "

print("Enter an string of text", prompt)
user_input = input()

def is_str(user_input):
    try:
        str(user_input)
        input_is_str = True
    except ValueError:
        input_is_str = False
    return input_is_str

valid_value = is_str(user_input)
if valid_value == True:
    print("That was some fine text, thank your Ser.")
else:
    print("Man, you don't know words from non-words!")
    exit(0)
