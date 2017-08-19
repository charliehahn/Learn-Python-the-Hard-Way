def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b
# "return" creates a value and makes it available
# so that it can then be
# assigned to a variable that calls the function.
# That is, it makes the value available but
# doesn't do anything with it on its own.
# Note that function works fine wihtout "print"

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

# all these functions above are "defined", but cannot
# run on their own.  you need to call them like below:

print "Let's do some math with just functions!"
# This is the first thing that prints because
# the print commands above are in the function
# definitions and the functions haven't been
# called yet.

# add(30, 5) calls the function and puts it into the variable "age"
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)
# By calling the functions to assign values to variables,
# two things happen: (1) the function runs, which is why
# their text appears in the console: and (2) the resulting
# value is assigned to the variable, which is why it can
# fill in the next string.

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
# Python observes the order of operations by doing the
# innermost parentheses - divide, in this case - first.
# and then working out. You can see the results in the
# console.

print "That becomes: ", what, "Can you do it by hand?"
