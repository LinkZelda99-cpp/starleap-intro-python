
##### Template for Chapter 10 Exercises 1 - 7, 9 - 12 ######

print("********** Ch 10 Exercise 1 **********")
def nested_sum(nested_list):
    total = 0
    for sublist in nested_list:
        for item in sublist:
            total += item
    return total
print(nested_sum([[1, 2, 3], [4, 5], [6]]))

print("********** Ch 10 Exercise 2 **********")
def cumsum(numbers):
    total = 0
    result = []
    for num in numbers:
        total += num
        result.append(total)
    return result
print(cumsum([1, 2, 3, 4]))

print("********** Ch 10 Exercise 3 **********")
def middle(numbers):
    return numbers[1:-1]

print(middle([1, 2, 3, 4, 5]))

print("********** Ch 10 Exercise 4 **********")
def chop(numbers):
    del numbers[0]
    del numbers[-1]
    return numbers
print(chop([1, 2, 3, 4, 5]))

print("********** Ch 10 Exercise 5 **********")
def is_sorted(numbers):
    return numbers == sorted(numbers)

print(is_sorted([1, 2, 3, 4, 5]))
print(is_sorted([1, 3, 2, 4, 5]))

print("********** Ch 10 Exercise 6 **********")
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

print(is_anagram("listen", "silent"))
print(is_anagram("hello", "world"))

print("********** Ch 10 Exercise 7 **********")
def has_duplicates(numbers):
    return len(numbers) != len(set(numbers))

print(has_duplicates([1, 2, 3, 4, 5]))
print(has_duplicates([1, 2, 2, 3, 4]))

print("********** Ch 10 Exercise 9 **********")
import bisect
import time

method_used = "start"

start_time = time.time()  # Record the start time


def ap_write_file_as_list():
    global method_used
    method_used = "append"
    words = []
    fin = open('shared/words.txt')
    for line in fin:
        word = line.strip()
        words.append(word)
    fin.close()
    return words
    

def idiom_write_file_as_list():
    global method_used
    method_used = "idiom"
    words = []
    fin = open('shared/words.txt')
    for line in fin:
        word = line.strip()
        words += [word]
    fin.close()
    return words
#Always keep one of the two lines below commented out.
print(ap_write_file_as_list())
#print(idiom_write_file_as_list())

for i in range(1000000):
    pass

end_time = time.time()  # Record the end time
execution_time = end_time - start_time  # Calculate the duration

print("Execution time: " + str(execution_time) + " seconds for " + method_used + " method")


print("********** Ch 10 Exercise 10 **********")
import bisect

def in_bisect(word, words=None):
    if words is None:
        with open('shared/words.txt', 'r') as fin:
            words = [w.strip() for w in fin]
        words.sort()
    index = bisect.bisect_left(words, word)
    return index != len(words) and words[index] == word

print(in_bisect("batman"))
print(in_bisect("i"))

print("********** Ch 10 Exercise 11 **********")
def list_all_reverse_sorted(show_sample=False):
    with open('shared/words.txt', 'r') as fin:
        words = [w.strip() for w in fin]
    is_rev_sorted = words == sorted(words, reverse=True)
    if show_sample and is_rev_sorted:
        print("First 50 words (reverse-sorted):", words[:50])
    return is_rev_sorted

print(list_all_reverse_sorted())

print("********** Ch 10 Exercise 12 **********")
def is_interlock():
    file = open('shared/words.txt')
    words = set(word.strip() for word in file)
    if words + words == words:
        print("Interlocked words found")
    file.close()

