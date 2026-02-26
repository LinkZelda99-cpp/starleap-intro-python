word_list = ['']
def moby_remove_whitespaces_punctuation(fin):
    import string
    count = 0
    for line in fin:
        word = line.strip().lower()
        word = word.translate(str.maketrans('', '', string.punctuation))
        word = word.replace(string.punctuation, "")
        line.strip
        line = line.replace("\n", "")
        words = line.split(" ")
        for w in words:
            word_list.append(w)
            count = count + 1
        print(f"{word} ")
    
    return count

count = moby_remove_whitespaces_punctuation(open('shared\Moby_Dick.txt'))
print(f"Word list: {word_list}")
print(f"Count: {count}")

