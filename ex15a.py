from sys import argv

script, filename = argv

txt = open(filename)

print "Heres your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = ("> ")

txt_again = open(file_again)

print txt_again.read()
