from hangman_lib import *

#
# This file is just a demo of the functions in hangman_lib.
#

help(print_hangman_image)

for i in range(7):
    print(f"Image for {i}")
    print_hangman_image(i)
    print()

print
