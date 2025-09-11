# 6.189 Lecture 2
# conditional_examples.py
 
##### Instructions #####
# Run this program and inspect the output.  Inspect the sections.  
# Make sure you understand how they work.  You can change "True" to "False"
# to disable sections and focus on others.


# Boolean math

# Examples of if statements
# General format:
# if <condition is True>:
#     <code to execute if condition is True>
if (True):
    if 9 > 5:
        print("Yes, 9 greater than 5")

    if 9 != 5:
        print("Yes, 9 not equal to 5")


# An example of an if/else statemet
if (True):
    # General format:
    # if <condition is True>:
    #     <code to execute if condition is True>
    # else:
    #     <code to execute if condition is False>

    if 9 < 5:
        print("Yes, 9 less than 5")
    else:
        print("No, 9 is not less than 5")


# An example using "not" and "and" keywords
if (True):
    if not (10 == 4) and 9 > 5:
        print("Yay, basic math competency achieved!")
    else:
        print(":(")

# Traffic light example
if (True):
    light_color = input("What color is the traffic light? ")
    light_color = light_color.lower()
    print(light_color)
    if light_color == "red":
        print("You should stop")
    elif light_color == "yellow":
        print("Slow down!")
    elif light_color == "green":
        print("Go ahead!")
    else:
        print("What country are you in??")