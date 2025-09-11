
##### Template for Chapter 5.14, Exercises 1 - 4 ######


print("********** Ch 5 Exercise 1 **********")

import time
time_epo = time.time()
sec_in_day = 24 * 60 * 60
min_in_day = 24 * 60
hours_in_day = 24
days_in_year = 365
sec_divided = time_epo / sec_in_day
min_divided = time_epo / min_in_day
hours_divided = time_epo / hours_in_day
years_divided = time_epo / (sec_in_day * days_in_year)
print("It's been", int(time_epo), "seconds since the epoch.")
print("That's about", int(sec_divided), "days, or", int(min_divided), "thousand minutes, or", int(hours_divided), "hundred hours, or roughly", int(years_divided), "years.")


print("********** Ch 5 Exercise 2 **********")

def theorum(a, b, c, n):
        boolean_t = False
        superscripts = {
            "0": "\u2070",
            "1": "\u00b9",
            "2": "\u00b2",
            "3": "\u00b3",
            "4": "\u2074",
            "5": "\u2075",
            "6": "\u2076",
            "7": "\u2077",
            "8": "\u2078",
            "9": "\u2079"
        }
        n_str = str(n)
        n_sup = "".join(superscripts.get(d, d) for d in n_str)
        print(f"Testing the theorem with {a}{n_sup} + {b}{n_sup} = {c}{n_sup}")
        if a**n + b**n == c**n:
            print("Holy smokes, Fermat was wrong!")
            boolean_t = False
        else:
            print("No, that doesn't work.")
            boolean_t = True

        if boolean_t == False:
            print("You found that Fermat was wrong when a =", a, ", b =", b, ", c =", c, ", and n =", n)
        else:
            print("You found that Fermat was right for a =", a, ", b =", b, ", c =", c, ", and n =", n)

theorum(1, 2, 3, 3)
theorum(3, 4, 5, 2)
theorum(3, 4, 6, 2)
theorum(3, 4, 5, 3)


print("********** Ch 5 Exercise 3 **********")
import turtle
def can_be_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        print(a, " ", b, " ", c, " can form a triangle.")
    else:
        print(a, " ", b, " ", c, " cannot form a triangle.")
    turtle.speed(1)
    turtle.color("white")
    turtle.bgcolor("black")
    turtle.pensize(3)
    turtle.pendown()
    turtle.forward(a)
    turtle.left(120)
    turtle.forward(b)
    turtle.left(120)
    turtle.forward(c)
    turtle.left(120)
    turtle.done()

can_be_triangle(3, 4, 5)


print("********** Ch 5 Exercise 4 **********")

# Do your work for Exercise 4 here.

print("Ch 5 Exercise 4: Not implemented") # Delete this line when you write your code!
