print("I will now count my chickens: ")
# prints the string

print("Hens", 25 + 30 / 6)
# prints the string Hens then the solves the equation and prints the result. Note that
# the order of operators (BIDMAS) means that the division is done first so the answer is
# 30 ( and not 9.166)

print("Roosters", 100 - 25 * 3 % 4)
# prints the string then the solves the equation and prints the result
# BIDMAS means it is: (100 - ((25 * 3)%4)) = (100-3) = 97

print("I will now count the eggs: ")
# prints the string
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)
# evaluates the equation: (3+2+1-5) = 1, so (1 + 4 % 2 - 1 / 4 +6) =
# (1 + 4 % 2 - 0.25 + 6) = (1 + 0 - 0.25 + 6) = 6.75

print("Is it true that 3 + 2 < 5 -7?")
# prints the string

print(3 + 2 < 5 - 7)
# evaluates the equation (is: 5 < -2), which is false, so it prints: False

print("What is 3 + 2?", 3 + 2)
# prints the string then the solves the equation and prints the result

print("What is 5 - 7?", 5 - 7)
# prints the string then the solves the equation and prints the result

print("Oh, that's why it's False.")
# prints the string

print("How about some more.")
# prints the string

print("Is it greater?", 5 > -2)
# prints the string then the solves the equation and prints the result

print("Is it greater or equal?", 5 >= -2)
# prints the string then the solves the equation and prints the result

print("Is it less or equal?", 5 <= -2)
# prints the string then the solves the equation and prints the result
