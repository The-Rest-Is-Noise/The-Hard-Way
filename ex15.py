# this is an import (argv = argument variable and it holds the arguments passed to it)
from sys import argv

# unpacks what been passed to argv into it constituent parts
script, filename = argv

# we call a function on txt and pass to it...
# what we get back from open(filename)...
# and filename was nupckaed from argv.
txt = open(filename)

# print some user text
print(f"Here is file {filename}: ")
# print the contens of the txt vairlable - which was prev. set to filename
print(txt.read())

# prompts the user to re-enter the filename for some reason
#print("Type the filename again:")
# creates a new var file_again and sets it to the provide file name
#file_again = input("> ")

# sets the text_again variable to equal the contents of file_again
# txt_again = open(file_again)
# prints out the value of txt_again
# print(txt_again.read())

txt.close()

#print(f"txt_again = {txt_again}")
