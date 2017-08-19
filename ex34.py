animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']
print animals
# for every item "i" in "animals", print that item on a single line
for i in animals:
    print i

print ""
print "First, second, third are ordinal numbers we"
print "need to count by cardinal nubers: 1, 2, 3."
print "With lists, you start at 0."
print ""

# To access a particular item in a list, put the list
# name and then the index number in square brackets.

# go to the list "animals" ,see how long (len) it is, and do it that many times
# useful, bc no specification required for length of list
# and if list changes, the for loop range will change automatically
for i in range(len(animals)):
    print "Index %d in the list is %s." % (i, animals[i])

# to view one item at a time
print animals[4]
