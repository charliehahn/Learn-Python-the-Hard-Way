# This exercise defines variables, but no execution codes
# execution will occur in the command line (in python)
# This is not a script, per se, but a module.
# That is, this document defines several functions
# that we can then use on other objects. The
# module will be called "ex25" (without the .py
# extension). In addition, we are going to run
# this from Python, and not the command line
# (i.e., UNIX shell) that we used so far.
# I've included instructions at the bottom.

# defining variable as "break_words". it uses a single
# argument variable called "stuff" that is read internally
def break_words(stuff):
    #function 1
    """This function will break up words for us."""
    # you can break up words based on any symbol
    # this function will take the variable "stuff"
    # and split it based on ' ', aka spaces between words
    # and feed it into the variable "words"
    words = stuff.split(' ')
    # "return" stores value into "words"
    return words

# this function takes results of 1st code, and feeds into this one
def sort_words(words):
    #function 2
    """Sorts the words. """
    return sorted(words)

def print_first_word(words):
    #function 3
    """Prints the first word after popping it off."""
    # this function will find the first word, beginning of the list
    # and displays the first word in the console
    word = words.pop(0)
    print word

def print_last_word(words):
    #function 4
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    #function 5
    """Takes in a full sentence and returns the sorted words."""
    # This is a second order function.
    # It reads the "break_words" function, and sort it, and store it
    # into "sort_words"
    # it does the same thing as the first 2 codes, but does it all
    # at once
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    #function 6
    """Prints the first and last words of the sentence."""
    # another second order function
    # this takes function 1, and function 2.....
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

# Here are the instructions:

# 1. Start Python.
# $ python

# 2. Import this newly defined module.
# >>> import ex25
# Note: Don't type ".py" or you'll get an error
# When you import this it will create a new file on your
# computer called "ex25.pyc." which is a "Python Bytecode"
# Document." which helps the module load faster in the
# future. You can, however, delete it if you want to.

# 3. Create an object to work with.
# >>> sentence = "All good things come to those who wait."

# 4. Run "break_words" and show results
# >>> words = ex25.break_words(sentence)
# >>> words
# Note: you can also print without the intermediate variable:
# >>> print ex25.break_words(sentence)

# 5. Run "sort_words" and show results
# >>> sorted_words = ex25.sort_words(words)
# >>> sorted_words

# 6. Run "print_first_word" (display automatically)
# >>> ex25.print_first_word(words)

# 7. Run "print_last_word" (displays automatically)
# >>> ex25.print_last_word(words)

# 8. Run "sort_sentence" and show results
# >>> sorted_sentence = ex25.sort_sentence(sentence)
# >> sorted_sentence
# Note: Zed used the object "sorted_words" for these
# but that may be a mistake because he used that earlier
# and all his variables so far use the function name, so
# I'm calling the object "sorted_sentence."
# The output looks the same as "sorted_words" but used
# a different process to get there.

# 9. Run "print_first_and_last" (displays automatically)
# >>> ex25.print_first_and_last(sentence)

# 10. Run "print_first_and_last_sorted" (displays automatically)
# >>> ex25.print_first_and_last_sorted(sentence)
# This code goes to sorted list and shows the first and last word.

# If you type help(ex25) you'll see the first block of
# text I wrote at the top and the text in triple quotes
# for each function below.

# If you type help(ex25.break_words) you'll see just
# the triple quote text for that function.  That's called
# a "documentation comment."

# Finally, you can avoid typing "ex25" at the beginning
# of everything if you import the module like this instead:
# >>> from ex25 import *
# Then you can run the commands like this:
# print break_words(sentence)
