
##### Template for Chapter 7 Exercises 1 - 2 ######

print("********** Ch 7 Exercise 1 **********")

# Do your work for Excercise 1 here.

print("Ch 7 Exercise 1: Not implemented") # Delete this line when you write your code!


print("********** Ch 7 Exercise 2 **********")
def eval_loop():
    """Loop that repeatedly prompts for input and evaluates it."""
    while True:
        user_input = input("Enter an expression (or 'done' to quit): ")
        if user_input.lower() == 'done':
            break
        print(eval(user_input))
eval_loop()
