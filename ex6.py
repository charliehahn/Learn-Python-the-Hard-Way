x = "There are %d types of people." % 10 # x = sentence. %d = 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not) # %s1 = binary %s2 = don't

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious # replace %r with 'hilarious' aka 'False'

w = "This is the left side of..."
e = "a string with a right side."

print w + e # combines 2 strings w & e
