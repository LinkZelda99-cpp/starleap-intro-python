
##### Template for Chapter 7 Exercises 1 - 2 ######

print("********** Ch 7 Exercise 1 **********")

# Pads an input value with spaces to a specified target length
def pad_str(value, target):
    in_str = str(value)
    l = len(in_str)
    diff = target - l
    return in_str + ' '*diff

# Prints a formatted table row with consistent spacing of columns
def print_table_row(a, b, c, d, length=20):
    print(pad_str(a, length), pad_str(b, length), pad_str(c, length), pad_str(d, length))

# Do your work for Excercise 1 here.  
# Make use of the provided functions above.

print("Ch 7 Exercise 1: Not implemented") # Delete this line when you write your code!


print("********** Ch 7 Exercise 2 **********")

# Do your work for Excercise 2 here.

print("Ch 7 Exercise 2: Not implemented") # Delete this line when you write your code!
