# this code opens a file, prints it out
# goes thru program one step
# at a time with an incrementing function

# importing code "from" the "system"
from sys import argv

script, input_file = argv
# when running this program, we need
# to specify 1. the script name and
# 2. the input_file name

# Create a function to display an entire text
# file. "f" is just a variable name for the file.
# print f.read() = displays the contents of the
# file in read only mode
def print_all(f):
    print f.read()

# Create a fucntion to go to the beginning of a file
# (i.e.. byte 0).
def rewind(f):
    f.seek(0)
# seek = go to a particular place in the file
# 0 = bytes aka go to the beginning

# Create a function to print out one line, where
# line_count is the line number we want to read,
# f is the name of the file (from above), and
# readline is a built-in function or method.
def print_a_line(line_count, f):
    print line_count, f.readline()
# print line_count, f.readline() = goes to the line count in file "f"
# and reads one line at a time, and displays that one line at a time

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)
# this doesn't display the file, just goes back to beginning of file

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)
# again print_a_line, displays one line at a time
# needs 2 arguments: 1. which line do you want to print
# 2. which file name are you reading from

# Move to next line by incrementing the
# variable current_line
current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
