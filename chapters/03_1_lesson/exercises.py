
##### Template for Chapter 3.14, Exercises 1 - 3 ######


print("********** Ch 3 Exercise 1 **********")

def right_justify(input):
    """(prints the length of the input, then 70 spaces, followed by input)\n
    input: takes input"""
    l = len(input)
    print("l =", l)
    target = 143
    spaces = target - l
    space_string = ' '*spaces
    print(space_string + input)

right_justify("monty")


print("********** Ch 3 Exercise 2 **********")

def print_spam():
    print('spam')

def do_twice(func, arg):
    func(arg)
    func(arg)


def print_twice(arg):
    print(arg)
    print(arg)


def do_four(func, arg):
    do_twice(func, arg)
    do_twice(func, arg)


do_twice(print, 'spam')
print('')

do_four(print, 'spam')


print("********** Ch 3 Exercise 3 **********")


def grid():
    print("""+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - + """)

grid()