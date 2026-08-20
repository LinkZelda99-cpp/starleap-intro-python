import math
# print("Hello, World!")
# print(type(2))
# print(type("2"))
# name = "Austin"
# print(name)
# age = 15
# print(age)
# print(name, "is", age)
# print(name, "is", age*100)
# answer = 72 * (3 + 2) * 100
# print(answer)
price = 23
tax_rate = 0.07
#total = price + price times tax rate
total = price + price * tax_rate
print("Total: " + str(total))
degrees = 45
radians = degrees / 180 * math.pi
print(math.sin(radians))
value = math.sqrt(4)
print(value)
print(5/2)
print(5//2)
print(5%2)
class_min = 90
hours = class_min//60
min = class_min - (hours * 60)
print(f"Class is {hours} hour(s) and {min} minutes long.")
