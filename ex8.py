# a text string that contains only spaces and four vars
formatter = "{} {} {} {}"

# print statement that passes four integers as it's arguements
print(formatter.format(1, 2, 3, 4))
# print statement that passes four strings as it's arguements
print(formatter.format("one", "two", "three", "four"))
# print statement that passes four Booleans as it's arguements
print(formatter.format(True, False, False, True))
# this is interesting! It passes the text of the formatter var to itself
print(formatter.format(formatter, formatter, formatter, formatter))
# prints a multiple strings
print(formatter.format(
    "Type yer",
    "Ain text here,",
    "Mibbes a poem,",
    "Or a song about beer."
    ))
