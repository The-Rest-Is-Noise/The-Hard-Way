# variable declaration (int) and assigment (10)
types_of_people = 10
# variable dec. (f"string) and assigment of a string with one var. in it
x = f"There are {types_of_people} types of people."

# var dec (string) and assign.
binary = "binary"
# var dec (string) and assign.
do_not = "don't"
# var dec (f"string) and assign. with two vars..
y = f"Those who know {binary} and those who {do_not}."

# print command with a string as the argument
print(x)
# print command with a string as the argument
print(y)

# print command with an f"string as the argument - the f" string takes one arguemnt...
# which is the variable 'x'
print(f"I said: {x}")
# print command with an f"string as the argument - the f" string takes one arguemnt...
# which is the variable 'y'
print(f"I also said: '{y}'")

# var. dec. of a binary ste to False
hilarious = False
# var. dec. of a string with one argument
joke_evaluation = "Isn't that joke so funny? {}"

# print a string using .format method with the binary var. hilarious
print(joke_evaluation.format(hilarious))

# another var. dec. - a string
w = "This is the left side of..."
# another var. dec. - a string
e = "a string with a right side."
# print the prev. two strings concat togther
print(w + e)
