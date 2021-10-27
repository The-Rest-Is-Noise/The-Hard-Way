
def numbers():
    numbers = []
    i = 1
    print("By how much do you wish the count increment?")
    increment = int(input(prompt))
    i = increment

    for r in range(1, (count + 1), increment):
        print(f"At the top i is {i}")
        numbers.append(i)
        i += increment
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}\n")
        print("The numbers: ")

    for num in numbers:
        print(num)

max_num = 99
min_num = 1
num_in_range = True
prompt = "::"
print(f"Enter an integer from {min_num} to {max_num}")
count = int(input(prompt))
if (count < min_num) or (count > max_num):
    num_in_range = False

if num_in_range == True:
    numbers()
else:
    print("ERROR! Number out of range!")
    if count > max_num:
        print("The entered number is too big!")
    elif count < min_num:
        print("The entered number is too small!")
