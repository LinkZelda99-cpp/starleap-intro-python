print("********** Ch 9.2 Exercise 7***********")
def has_3_double_letters(word):
    count = 0
    previous = ''
    for letter in word:
        if letter == previous:
            count += 1
            if count == 3:
                return True
        else:
            count = 0
        previous = letter
    return False
fin = open('shared/words.txt')
for line in fin:
    word = line.strip()
    if has_3_double_letters(word)==True:
        print(word)