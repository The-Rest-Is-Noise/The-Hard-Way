the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this is the first for loop
for c in the_count:
    print(f"This is count {c}")

# another for loop
for f in fruits:
    print(f"This is a {f}.")

# we can mix lists too
#
for i in change:
    print(f"I got {i} back in change.")

# we can also build lists
elements = []


for i in range(1, 6):
    print(f"Adding {i} to the list.")
    elements.append(i)



for i in elements:
    print(f"Element was: {i}")
