
print("********** Ch 13 Exercise 1, 2, and 3**********")
import random
import string
from operator import itemgetter

def sort(num):
    for j in range(len(num) - 1):
        for i in range(len(num) - 1 - j):
            if num[i] > num[i + 1]:
                num[i], num[i + 1] = num[i + 1], num[i]

def random_numbers(n):
    nums = []
    for i in range(n):
        nums.append(random.randint(1, 10000))
    return nums

def moby_remove_whitespaces_punctuation(fin):
    import re
    d = {}
    for line in fin:
        line = line.lower()
        line = re.sub(r'[^a-zA-Z\s]', ' ', line)
        words = line.split()
        for w in words:
            if w:
                if w not in d:
                    d[w] = 1
                else:
                    d[w] += 1
    return d

f_name = 'shared/Moby_Dick.txt'
word_list = 'shared/words.txt'

with open(f_name, 'r', encoding='utf-8') as f:
    d = moby_remove_whitespaces_punctuation(f)

sorted_words = sorted(d.items(), key=itemgetter(1), reverse=True)

print("Top 20 most common words:")
for word, count in sorted_words[:20]:
    print(word, count)
    
print("********** Ch 13 Exercise 4 **********")

def not_in():
    with open(f_name, 'r', encoding='utf-8') as f:
        d = moby_remove_whitespaces_punctuation(f)

    with open(word_list, 'r', encoding='utf-8') as f:
        word_set = set()
        for line in f:
            word_set.add(line.strip().lower())

    not_in_list = []

    for w in d:
        if w not in word_set:
            not_in_list.append(w)

    print(not_in_list)

not_in()
    
print("********** Ch 12 Exercise 5 **********")
import random

