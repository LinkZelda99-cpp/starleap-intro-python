
##### Template for Chapter 5.14, Exercises 1 - 4 ######


print("********** Ch 6 Exercise 1 **********")

def b(z):
    prod = a(z, z)
    print(z, prod)
    return prod

def a(x, y):
    x = x + 1
    return x * y

def c(x, y, z):
    total = x + y + z
    square = b(total)**2
    return square

x = 1
y = x + 1
print(c(x, y+3, x+y))
#Prints 8 90
#       8100

print("********** Ch 6 Exercise 2 **********")

def ackermann(m, n):
    if m == 0:
        return n + 1
    elif m == 1:
        return n + 2
    elif m == 2:
        return 2 * n + 3
    elif m == 3:
        return 2**(n + 3) - 3
    else:
        return ackermann(m - 1, ackermann(m, n - 1))
print(ackermann(1, 10))  # Should print 12



print("********** Ch 6 Exercise 3 **********")

# Exercise 3 should be worked in a new file called palindrome.py



print("********** Ch 6 Exercise 4 **********")

# Do your work for Exercise 4 here.

print("Ch 6 Exercise 4: Not implemented") # Delete this line when you write your code!



print("********** Ch 6 Exercise 5 **********")

# Do your work for Exercise 5 here.

print("Ch 6 Exercise 5: Not implemented") # Delete this line when you write your code!
