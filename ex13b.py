from sys import argv
# read the WYSS section for how to run this
happy, var1, var2 = argv

one_last = input("Can you provide me something for one for variable? Pleeease? ")

print("Currently running:", happy)
print("The first variable is called:", var1)
print("The second variable is called:", var2)
print(f"That's {var1} {var2} and {one_last} for you?")
