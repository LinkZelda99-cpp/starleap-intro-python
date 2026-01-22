
##### Template for Chapter 10 Exercises 1 - 7, 9 - 12 ######

print("********** Ch 11 Exercise 1 **********")
import time

start = time.perf_counter()

words = {}
with open("shared/words.txt") as file:
    for line in file:
        word = line.strip()
        words[word] = words.get(word, 0) + 1

end = time.perf_counter()
print(words)


# for word, count in words.items():
#     print(f"{word}: {count}")

print(f"Runtime: {end - start:.9f} seconds for the dictionary method")


start = time.perf_counter()
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

end = time.perf_counter()
print(f"Runtime: {end - start:.9f} seconds for append method")

start = time.perf_counter()
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

end = time.perf_counter()
print(f"Runtime: {end - start:.9f} seconds for idiom method")


print("********** Ch 11 Exercise 2 **********")





print("********** Ch 11 Exercise 3 **********")





print("********** Ch 11 Exercise 4 **********")





print("********** Ch 11 Exercise 5 **********")





print("********** Ch 11 Exercise 6 **********")




