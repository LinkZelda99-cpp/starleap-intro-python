
# Chapter 1 - More Math

Work along in your interactive Python interpreter as you go.

## Math Operations
Addition (+), subtraction (-), multiplication (*), division (/), modulo (%) and power (**) operators are built into the Python language. This means you can use them right away. If you want to use a square root in your calculation, you can either raise something to the power of 0.5 or you can import the math module. Do not worry about what it means right now, we will cover this later during the course. Below are two examples of square root calculation:

>>> 16**0.5
4.0
>>> import math
>>> math.sqrt(16)
4.0

The math module allows you to do a number of useful operations:

>>> math.log(16, 2)
4.0
>>> math.cos( 0 )
1.0

Note that you only need to execute the import command once after you start your Python shell; however you will need to execute it again if you restart the shell, as restarting resets everything back to how it was when you opened your codespace. Don't worry too much about this right now; we'll cover it more in depth soon!

Exercise
(this is just for practice, solutions will not be graded or collected in class)

Use the Terminal to calculate:
1. 6+4*10

2. (6+4)*10 (Compare this to #1, and note that Python uses parentheses just like you would in normal math to determine order of operations!)

3. 23.0 to the 5th power

4. 23 to the 5th power

5. Positive root of the following equation:
34*x^2 + 68*x - 510
Recall:
a*x^2 + b*x + c
x1 = ( - b + sqrt ( b*b - 4*a*c ) ) / ( 2*a)


#Hello!