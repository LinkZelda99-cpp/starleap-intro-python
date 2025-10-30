
##### Template for Chapter 8 Exercises 1 - 5 ######

print("********** Ch 8 Exercise 1 **********")
one = str.capitalize("hello world")
print(one)
two = str.isupper("HELLO")
print(two)
three = str.isupper("Hello")
print(three)
four = str.lower("Hello")
print(four)
five = str.lower("HELLO")
print(five)
print("********** Ch 8 Exercise 2 **********")

def count_letters(word, letter):
    count = 0
    for l in word:
        if l == letter:
            count = count + 1
    print(count)
count_letters("banana", "a")


print("********** Ch 8 Exercise 3 **********")

w = "racecar"
print(w == w[::-1], "for ", w)

print("********** Ch 8 Exercise 4 **********")

def any_lowercase1(s): # This function is incorrect. It only checks the first character of the string and returns whether it is lowercase or not.
    for c in s:
        if c.islower():
            return True
        else:
            return False

def any_lowercase2(s): # This function is incorrect. It always returns 'True' because it checks if the string 'c' is lowercase, which it always is.
    for c in s:
        if 'c'.islower(): 
            return 'True'
        else:
            return 'False'

def any_lowercase3(s): #This function is incorrect. It only checks the last character of the string and returns whether it is lowercase or not.
    for c in s:
        flag = c.islower()
        return flag

def any_lowercase4(s): # This function is correct. It checks each character in the string and sets the flag to True if any character is lowercase.
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s): # This function is incorrect. It checks if all characters in the string are lowercase and returns False if it finds any character that is not lowercase.
    for c in s:
        if not c.islower():
            return False
    return True

print('''
The correct function is any_lowercase4(s) because it accurately checks if there is at least one lowercase letter in the string by using a flag that is updated with the logical OR operation for each character's lowercase status.
''')
#test line
print("********** Ch 8 Exercise 5 **********")

def rotate_word(word, n):
    """Rotate each letter in 'word' by 'n' positions in the alphabet."""
    rotated = ""
    for char in word:
        if char.isalpha():  # Check if the character is a letter
            shift = n % 26  # Ensure the shift wraps around the alphabet
            new_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a')) if char.islower() else chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            rotated += new_char
        else:
            rotated += char  # Non-alphabetic characters are added unchanged
    return rotated
print(rotate_word("cheer", 7))  # Expected output: "jolly"
print(rotate_word("melon", -10))  # Expected output: "cubed"
print(rotate_word("Hello, World!", 3))  # Expected output: "Khoor, Zruog!"
print(rotate_word("abcXYZ", 2))  # Expected output: "cdeZAB"