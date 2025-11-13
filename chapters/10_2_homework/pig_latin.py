
# Define your global variables and constants here



# word_to_pig_latin: Converts the input string to pig latin and returns the pig latin string
# Input: one string - the word in English
# Return: one string - the word in Pig Latin
def word_to_pig_latin(word):
    """Convert a single English word to Pig Latin and return it."""
    if not word:
        return ''
    w = word.lower()
    vowels = 'aeiou'
    for letter in w:
        if letter not in vowels:
            vowels = 'aeiouy'
        else:
            vowels = 'aeiou'
            break
    
    for i, ch in enumerate(w):
        if ch in vowels:
            if i == 0:
                return w + 'hay'
            return w[i:] + w[:i] + 'ay'
    return w + 'ay'

def sentence_to_pig_latin():
    """Convert a sentence of English words to Pig Latin and return it."""
    sentence = input("Enter a sentence in English: ")
    words = sentence.split()
    pig_latin_words = [word_to_pig_latin(word) for word in words]
    pig_latin_words = ' '.join(pig_latin_words)
    pig_latin_words = pig_latin_words.capitalize()
    append_punctuation = sentence[-1] if sentence[-1] in '.!?' else ''
    return pig_latin_words + append_punctuation

print(sentence_to_pig_latin())

def test_translator():
    pairs = [
        ['boot', 'ootbay'],
        ['image', 'imagehay'],
        ['pig', 'igpay'],
        ['latin', 'atinlay'],
    ]
    errors = 0
    for pair in pairs:
        english = pair[0]
        answer = pair[1]
        pl = word_to_pig_latin()
        if (pl != answer):
            print(f"Oops!  {english} should translate to {answer}, not {pl} !")
            errors += 1
    if errors == 0:
        print('Congrats!  Your translator is working well.')

#test_translator()