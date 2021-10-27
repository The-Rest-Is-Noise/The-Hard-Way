# uses the sys library to accept an argument from
# the command line (in this case the name of a file to work on)
from sys import argv

# unpacks argv
script, filename = argv

# prints a user prompt warning user a file is to be overwritten
print(f"We're going to erase {filename}.")
# user prompt giving an option
print("If you don't want that hit Ctrl-C (^C).")
# user prompt giving an option
print("If you do want that hit RETURN.")
# reads user input and displays '?'
input("?")

# NB: if Ctrl-C is selected a keyboard interupt message is
# displayed and the script quits.
# otherwise the file presented in argv is opended with "w" (write) permissions

print("Opening the file...")

target = open(filename, "w")

# the file is truncated
# the truncate command can be passed an arg. which is a byte size -
# everythign after that is deleted. Default is the current pos. in the file
# as we have only just open the file default means dlete everythiing from the start (all)
# print("Truncating the file. Goodbye!")
# target.truncate()

# user info. is printed
print("Now I'm going to ask you for three lines.")
# input reuested (three times) at the command line
line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

# user info printed
print("I'm going to write these to the file.")
all_text = (line1 + "\n" + line2 + "\n" + line3)
# the input given at the command line is then written to the file
target.write(all_text)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

print("And finally, we close it.")
target.close()
