# 6.189 Lecture 3
# check_for_vowels.py

##### Instructions #####
# Run this program and inspect the output.  Inspect the functions.  
# Make sure you understand how they work.  Try some different inputs
# to run_is_a_vowel and run_only_vowels, and see if the output is what 
# you expect.

def is_a_vowel(c):
    # check if c is a vowel
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
        # Return True if c is a vowel
        return True
    elif c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U':
        # Also return True if c is a capital vowel
        return True
    else:
        # c must not be a vowel; return False
        return False

def run_is_a_vowel(c):
    print(c, is_a_vowel(c))

## Testing
run_is_a_vowel("u")
run_is_a_vowel("E")
run_is_a_vowel("x")

def only_vowels(phrase):
    # Takes a phrase, and returns a string of all the vowels
    # Initalize an empty string to hold all of the vowels
    vowel_string = ''
    for letter in phrase:
        # check if each letter is a vowel
        if is_a_vowel(letter):
            # If it's a vowel, we append the letter to the vowel string
            vowel_string = vowel_string + letter
        # if not a vowel, we don't care about it- so do nothing!

    return vowel_string
    # Code after a "return" doesn't print
    print("A line of code after the return!")

def run_only_vowels(phrase):
    print(phrase, only_vowels(phrase))

# Testing the functions
run_only_vowels("tim the beAver")
run_only_vowels("HeLlO wOrLd!!")
run_only_vowels("klxn") # Expect no vowels from this one!
    