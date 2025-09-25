##### Template for Homework 1, Exercises 1-3 ######


print("********** Homework 1 Exercise 1 **********")
tictactoe_board = """
  |  | 
--------
  |  |  
--------
  |  |  """
print(tictactoe_board)

print("********** Homework 1 Exercise 2 **********")
print("Enter your first name: ")
first_name = input()
print("Enter your last name: ")
last_name = input()
print("Enter your date of birth: ")
print("Month?: ")
month = input()
print("Day?: ")
day = input()
print("Year?: ")
year = input()
if type(day) == int:
    str(day)
else:
    day = day
str(year)

print(first_name, last_name, "was born on", month, day, year + ".")

print("********** Homework 1 Exercise 3 **********")
import math
def square_root():
    print("Enter a number to find the square root of: ")
    a = float(input())
    if a < 0:
        return "Error: Cannot compute square root of negative number."
    else:
      b = math.sqrt(a) 
      print("The square root of", a, "is", b)
        
square_root()