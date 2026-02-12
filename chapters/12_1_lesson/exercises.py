
##### Template for Chapter 12 Exercises 1 - 4 ######

print("********** Ch 12 Exercise 1 **********")
def most_frequent_letter(string):
    string = string.lower()
    letter_counts = {}
    for letter in string:
        if letter.isalpha():
            letter_counts[letter] = letter_counts.get(letter, 0) + 1
    most_frequent = max(letter_counts, key=letter_counts.get)
    print(f"The most frequent letter is '{most_frequent}' with {letter_counts[most_frequent]} occurrences.")
    return most_frequent

most_frequent_letter("Hello World!")

print("********** Ch 12 Exercise 2 **********")
def print_all_anagrams_within_file(word):
    fin = open('shared/words.txt')
    anagrams = []
    for line in fin:
        candidate = line.strip()
        if sorted(candidate) == sorted(word):
            anagrams.append(candidate)
    print(f"Anagrams of '{word}' in the file: {anagrams}")
    
print_all_anagrams_within_file("python")

print("********** Ch 12 Exercise 3 **********")
def print_all_metathesis_pairs_in_file(fin):
    words = [line.strip() for line in fin]
    metathesis_pairs = []
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if sorted(words[i]) == sorted(words[j]):
                differences = sum(1 for a, b in zip(words[i], words[j]) if a != b)
                if differences == 2:
                    metathesis_pairs.append((words[i], words[j]))
    print("Metathesis pairs found:")
    for pair in metathesis_pairs:
        print(pair)
print_all_anagrams_within_file(open('shared/words.txt'))

print("********** Ch 12 Exercise 4 **********")
def print_all_english_words_that_you_can_remove_a_letter_one_at_a_time_from_it_and_still_have_an_english_word(fin):
    words = set(line.strip() for line in fin)
    valid_words = []
    for word in words:
        if len(word) > 1:
            can_remove_letter = True
            for i in range(len(word)):
                new_word = word[:i] + word[i+1:]
                if new_word not in words:
                    can_remove_letter = False
                    break
            if can_remove_letter:
                valid_words.append(word)
    print("English words that can have a letter removed one at a time and still be an English word:")
    for word in valid_words:
        print(word)

print_all_english_words_that_you_can_remove_a_letter_one_at_a_time_from_it_and_still_have_an_english_word(open('shared/words.txt'))




