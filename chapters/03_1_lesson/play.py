def print_lyrics():
    print("Boots")
    print("cats")

def lyrics_repeat():
    print_lyrics()

def print_twice(input):
    print(input)
    print(input)

# print_twice('Spam '*2)

def is_it_even(input):
    if input % 2==0:
        print(str(input) + " is even.")
    else:
        print(str(input) + " is odd.")

# is_it_even(4)
# is_it_even(5)

x = 33
y = 23

def compare(x, y):
    if x < y:
        print(str(x) + " is less than " + str(y))
    elif x > y:
        print(str(x) + " is greater than " + str(y))
    else:
        print(str(x) + " is " + str(y))

compare(6, 5)
print("x is " + str(x) + ", and y is " + str(y))