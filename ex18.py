# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)
#def = define the function
# "print_two" is an arbitrary name for the function
# You could use anything you wanted, as long as it
# is one word with only letters, numbers, and
# underscores (but it can't start with a number).
# Make sure to put a colon at the end of the first
# line and then indent (four spaces) after that
# (the colon indicates the function is done being written
# and now moving onto the contents of the function)
# You can "run." "call." or "use" a function.  These terms are synonymous

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument, whereas the top code takes 2
def print_one(arg1):
    print "arg1: %r" % arg1

# this one takes no arguments
def print_none():
    print "I got nothin'."
# NB: A function with no arugments still does
# something. It just doesn't need any variables
# added to do its job.
# meaning it doesn't need any variables that
# user has to input in order for it to run.

# call (aka run) all 4 functions below
print_two("Charlie", "Hahn")
print_two_again("Charlie", "Hahn")
print_one("First!")
print_none()
# don't need to specify variables for
# "print_none", but do need to have
# paranthesis for it to work
