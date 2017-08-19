people = 30
cars = 40
buses = 15

# "elif" is short for "else if" and it is used for
# additional conditions, while "else" is used to
# cover anything not specifically addressed.

if cars > people:
    # 40 > 30 is true so this will print and
    # skip the "elif" and "else"
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."

if buses > cars:
    # 14 > 40 is false, so the first line is skipped
    print "That's too many buses."
elif buses < cars:
    # 14 < 40 is true, so this line will print and
    # the "else" eill be skipped
    print "Maybe we could take the buses."
else:
    print "We still can't decide."

if people > buses:
    # 30 > 15, so this will print and skip the "else"
    print "Alright, let' just take the buses."
else:
    print "Fine, let's stay home then."
