tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
# \\ = only one \ wil show up
backslash_cat = "I'm \\ a \\ cat."

# triple quotations to put infinite lines of text within quotations
# \t tabs out the word that follows
# \n\t puts the word on a new line and tabs it out
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
