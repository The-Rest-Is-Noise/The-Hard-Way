from random import *
prompt = ':>'

def punnets_cherries(num_punnets, num_cherries):
    cherries_per_punnet = 45
    needed_punnets = 0
    full_punnets = 0
    punnets_needed = int(num_cherries / cherries_per_punnet)
    if punnets_needed <= num_punnets:
        full_punnets = int(num_cherries / cherries_per_punnet)
        left_over_cherries = num_cherries % cherries_per_punnet
        left_over_punnets = num_punnets - full_punnets
    else:
        full_punnets = num_punnets
        left_over_cherries = num_cherries - (full_punnets * cherries_per_punnet)
        left_over_punnets = 0
        needed_punnets = -(num_punnets - punnets_needed)


    print(f"""
    You have {num_punnets} punnets to fill, and {num_cherries} cherries with which to fill them.
    At {cherries_per_punnet} cherries per punnet that leaves you:
    \t - {full_punnets} punnets filled and...
    \t - {left_over_cherries} cherries left over.
    \t - Left over punnets: {left_over_punnets}.
    \t - Punnets needed: {needed_punnets}.
    """)
    #print(f"""
    #TEST ONLY:
    #cherries_per_punnet = {cherries_per_punnet}
    #num_punnets = {num_punnets}
    #num_cherries = {num_cherries}
    #punnets_needed = {punnets_needed}

    #full_punnets = {full_punnets}
    #left_over_cherries = {left_over_cherries}
    #left_over_punnets = {left_over_punnets}
    #""")

# No. 1
punnets_cherries(34, 459)

num_punnets = 36
num_cherries = 800
# No. 2
punnets_cherries(num_punnets, num_cherries)

# No. 3
punnets_cherries((num_punnets + 12), (num_cherries - 23))

extra_punnets = 23
extra_cherries = 567
# No. 4
punnets_cherries((num_punnets + extra_punnets), (num_cherries + extra_cherries))



print(f"You have {num_punnets} punnets. Please enter the number of cherries (as an integer)")
user_input_num_cherries = int(input(prompt))
# No. 5
punnets_cherries(num_punnets, user_input_num_cherries)


print(f"You have {num_cherries} cherries. How many punnets do you have? (as an integer)")
user_input_num_punnets = int(input(prompt))
# No. 6
punnets_cherries(user_input_num_punnets, num_cherries)


print("We need to gather some data.")
print(f"We have {num_cherries} cherries so far. How many extra cherries do you have?")
user_input_num_cherries = int(input(prompt))
print(f"We have {num_punnets} punnets set aside. How many extra punnets do you have?")
user_input_num_punnets = int(input(prompt))
# No. 7
punnets_cherries((num_punnets + user_input_num_punnets), (num_cherries + user_input_num_cherries))


num_cherries = randint(100, 9999)
num_punnets = randint(1, 999)
print(f"We have {num_cherries} cherries.")
print(f"We have {num_punnets} punnets set aside.")
# No. 8
punnets_cherries(num_punnets, num_cherries)
