# 6.11  Exercises

## Exercise 1  
Draw a stack diagram for the following program. What does the program print?

```python
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
```


## Exercise 2  
The Ackermann function, A(m, n), is defined:
| A(m, n) | | | |
| ----------- | ----------- | ----------- | ----------- |
| | ⎧ | | |
| | ⎪ | n+1	| if  m = 0 |
| A(m, n) = | ⎨ | A(m−1, 1)	| if  m > 0  and  n = 0 |
| | ⎪ | A(m−1, A(m, n−1)) | if  m > 0  and  n > 0. |
| | ⎩ | | |

        See http://en.wikipedia.org/wiki/Ackermann_function. 

Write a function named *ack* that evaluates the Ackermann function. Use your function to evaluate ack(3, 4), which should be 125. What happens for larger values of m and n?


## Exercise 3  
A palindrome is a word that is spelled the same backward and forward, like “noon” and “redivider”. Recursively, a word is a palindrome if the first and last letters are the same and the middle is a palindrome.

The following are functions that take a string argument and return the first, last, and middle letters:
``` python
def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]
```
We’ll see how they work in Chapter 8.

1. Type these functions into a file named *palindrome.py* and test them out. What happens if you call middle with a string with two letters? One letter? What about the empty string, which is written '' and contains no letters?
2. Write a function called is_palindrome that takes a string argument and returns True if it is a palindrome and False otherwise. Remember that you can use the built-in function len to check the length of a string.



## Exercise 4   
A number, a, is a power of b if it is divisible by b and a/b is a power of b. Write a function called *is_power* that takes parameters a and b and returns True if a is a power of b.
Note: you will have to think about the base case.


## Exercises 5
The greatest common divisor (GCD) of a and b is the largest number that divides both of them with no remainder.

One way to find the GCD of two numbers is based on the observation that if r is the remainder when a is divided by b, then gcd(a, b) = gcd(b, r). As a base case, we can use gcd(a, 0) = a.

Write a function called *gcd* that takes parameters a and b and returns their greatest common divisor.

Credit: This exercise is based on an example from Abelson and Sussman’s Structure and Interpretation of Computer Programs.
