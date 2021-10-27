#Uses a lib to import an argument var.
from sys import argv
# splits arg. into input file
script, input_file = argv

current_line = 1
current_char = 0
# defines a new func. with an argument 'f' and prints the spec. file
def print_all(f):
    print(f.read())

# defines a new function with argument 'f' and find the startnof the specified file
def rewind(f, current_char):
    f.seek(current_char)

# defines a new function that has 2 arg: file and line-num. Func prints one line of text
def print_a_line(line_count, f):
    print(line_count, f.readline())

def print_crement (line_to_print, char_to_start_at):
    rewind(current_file, current_char)
    print_a_line(current_line, current_file)
    current_line = current_line + 1; current_char = current_char + 1

# declares a new var = contents of file in argv
current_file = open(input_file)

# prints out user text
print("First let us print the whole file:\n")
# prints  out the contents of the file specified by input_file
print_all(current_file)

# prints out user text
print("Now let us rewind, kind of like a tape.")
print("Let us print three lines: ")
# moves us back to the start of the specified file
#rewind(current_file, current_char)
#print_a_line(current_line, current_file)
#current_line = current_line + 1; current_char = current_char + 1

#rewind(current_file, current_char)
#print_a_line(current_line, current_file)
#current_line = current_line + 1; current_char = current_char + 1

#rewind(current_file, current_char)
#print_a_line(current_line, current_file)
#current_line = current_line + 1; current_char = current_char + 1

print_crement(current_line, current_char)
