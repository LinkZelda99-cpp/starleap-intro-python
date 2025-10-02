import math
def newt_sqrt(x, a, debug=False):
    """Compute square root of x using Newton's method, starting from a."""
    correct = math.sqrt(x)
    y = a
    while abs(y - correct) >= 0.000000000000000000000000001:
        y = (y + x/y) / 2
        print("Current guess:", y)
        if debug:
            print(y)
    return y
# Call newt_sqrt to compute the square root of 25 starting from guess 1
result = newt_sqrt(25, 1)
print(result)
