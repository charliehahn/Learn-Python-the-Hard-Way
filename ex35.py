from sys import exit
# sys = library or module.  exit = special function we're bringing in
# so we can defer to the function instead of defining them

def gold_room():
    print "This room is full of gold.  How much do you take? Enter a number"
    # I added Enter a number

    next = raw_input("> ")

    if "0" in next or "1" in next:
        # takes the number entered: "0" or "1" and turns it into an integer below
        # without "int", the text entered will be a string
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")
        # function "dead" is defined below

    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
        # exit is a system function that was imported at the top
        # 0 is a code for an error-free exit (vs. 2, 16, 89, etc.)
    else:
        dead("You greedy bastard! You're dead!")
        # I added "You're dead!"

def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False
    # bear_moved is a boolean variable

    while True:
        next = raw_input("> ")

        if next == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif next == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        # when would "taunt bear" and "bear_moved" occur? Ask Zed
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "open door" and bear_moved:
            gold_room()
            # function "gold_room" was defined above
        else:
            print "I got no idea what that means."
            # May want to add prompts to give ideas

def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    next = raw_input("> ")

    if "flee" in next:
        # This looks at the text you entered and if the keyword
        # "flee" appears in it anywhere, it does this command
        # if "flee" and "head" are both in text, it will execute the first word found
        start()
        # function "start" is defined below
    elif "head" in next:
        # Check for keyword "head" anywhere in entered text
        dead("Well that was tasty!")
        # function "dead" defined below
    else:
        cthulhu_room()
        # Returns user to beginning of this function

def dead(why):
    print why, "Good job!"
    exit(0)

def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"

    next = raw_input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

start()
# function "start" is defined above
# This is the only function automatically run in this code
