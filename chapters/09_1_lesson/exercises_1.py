
##### Template for Chapter 9.2 Exercises 1 - 6 ######

print("********** Ch 9.2 Exercise 1 **********")
fin = open('shared\words.txt')
for line in fin:
    word = line.strip()
    if len(word) > 20:
        print(word)
        
print("********** Ch 9.2 Exercise 2 **********")
def has_no_e(word):
    for letter in word:
        if letter == 'e':
            return False
    return True

total = 0
count = 0
with open('shared/words.txt', 'r') as fin:
    for line in fin:
        word = line.strip()
        total += 1
        if has_no_e(word):
            count += 1
if total > 0:
   percent = (count / total) * 100
else:
    percent = 0.0

print(count)
print(f"{percent:.2f}% of words have no 'e'.")

print("********** Ch 9.2 Exercise 3 **********")
def avoids(word, forbidden):
    for letter in word:
        if letter in forbidden:
            return False
    return True
fin = open('shared/words.txt')
for line in fin:
    word = line.strip()
    if avoids(word, 'aeiouy'):
        print(word)

print("********** Ch 9.2 Exercise 4 **********")
def uses_only(word, available):
    for letter in word:
        if letter not in available:
            return False
    return True
fin = open('shared/words.txt')
for line in fin:
    word = line.strip()
    if uses_only(word, 'aeiouy'):
        print(word)

print("********** Ch 9.2 Exercise 5 **********")
def uses_all(word, required):
    for letter in required:
        if letter not in word:
            return False
    return True
fin = open('shared/words.txt')
for line in fin:
    word = line.strip()
    if uses_all(word, 'aeiouy'):
        print(word)

print("********** Ch 9.2 Exercise 6 **********")
def is_abecedarian(word):
    previous = word[0]
    for letter in word:
        if letter < previous:
            return False
        previous = letter
    return True
fin = open('shared/words.txt')
for line in fin:
    word = line.strip()
    if is_abecedarian(word):
        print(word)