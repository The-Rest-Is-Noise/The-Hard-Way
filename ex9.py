# Here's some new strange stuff, remember to type it exactly

# var dec for a string
days = "Mon Tue Wed Thu Fri Sat Sun"
# var dec for a string broken up with new lines commands
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

# print stmnt using the days var
print("Here are the days: ", days)
# print stmnt using the nmonths var
print("Here are the months: ", months)

print("\nWhy stop there?")
months = "\nSep\nOct\nNov\nDec"
print(months)

# this is new - a multi line
print("""
There's something going on here.
With the three double quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""
)
formatter = "{}, {}, {}, {}"
print(formatter.format(
    "It should be noted however",
    "That the above text",
    "Was each bit of it",
    "Printed on a new line.\n"
    ))
print("But that said...\n")

formatter = "{}, \n{}, \n{}, \n{}"
print(formatter.format(
    "This is also in fact",
    "Achievable that is",
    "With a brace of \\n's",
    "To .format the biz.\n"
    ))
