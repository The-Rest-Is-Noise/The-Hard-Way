prompt = "::"
print("This room is full of gold. How much gold do you take?")
choice = (input(prompt))

try:
    int(choice)
    choice_is_Int = True
    print(f"Is Integer: {choice_is_Int}")
except ValueError:
    choice_is_Int = False
    print(f"Is Integer: {choice_is_Int}")
