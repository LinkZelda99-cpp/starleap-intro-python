##### Recursion Example #####

# Run this file and inspect the output.  

def countdown(n, verbose = False):
    if verbose:
        print('countdown() called with argument: n = ', n)

    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1, verbose)

    if verbose:
        print('Ending countdown() called with argument: n = ', n)

print("\nCountdown:")
countdown(10)

print("\nCountdown with details:")
countdown(5, verbose=True)