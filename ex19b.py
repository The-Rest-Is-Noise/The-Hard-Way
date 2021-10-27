# def keyword: deifining a new function that takes two arguements as named
def punnets_cherries(num_punnets, num_cherries):
    # prints a new line for formatting
    print("\n")
    # uses an f-print to print some info
    print(f"You have {num_punnets} punnets to fill.")
    # uses an f-print to print some info
    print(f"And {num_cherries} cherries with whcih to fill them.")
    print(f"That leaves you {full_punnets} punnets filled and {leftovers} left over.")
    # prints a new line for formatting
    print("\n")

cherries_per_punnet = 45
full_punnets = round(num_cherries / cherries_per_punnet)
leftovers = num_cherries % cherries_per_punnet
# calls the new function and the call itself passes the two arguments
punnets_cherries(10, 300)

# uses an f-print to print some info
print("Or, we can use variables from our script: ")
# sets a var of type int
amount_of_cheese = 10
# sets a var of type int
amount_of_crackers = 50
# calls the function but using the variabel we just declared as a representation of the values
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# now he's just showing off
print("We can even do math inside too: ")
# calls the new function but does some arithmetic on some values
cheese_and_crackers(10 + 20, 5 + 6)

# prints some info
print("And we can combine variables and maths:")
# cals the function using the vars and some some math
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
