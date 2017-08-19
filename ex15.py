from sys import argv
#argv = argument vector. an argument variable passing code through command line
#script = ex15.py script name,  filename = txt file name
script, filename = argv

#opens the txt file once name is entered in command line
txt = open(filename)

#prints file name and prints what's inside the txt file
print "Heres your file %r:" % filename
print txt.read()
#asks to type the name of the txt file
print "Type the filename again:"
file_again = raw_input("> ")
#opens file
txt_again = open(file_again)
#prints out whats inside the txt file again
print txt_again.read()
