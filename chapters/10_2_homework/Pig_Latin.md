# Pig Latin

Use the file *pig_latin.py* as a framework.

Create a function called *word_to_pig_latin* that takes in a single word, then converts the word to Pig Latin and returns the pig latin word. To review, Pig Latin takes the first letter of a word, puts it at the end, and appends “ay”. The only exception is if the first letter is a vowel, in which case we keep it as it is and append “hay” to the end.

E.g. “boot” → “ootbay”, and “image” → “imagehay”.

It will be useful to define a list at the top of your code file called VOWELS. This way, you can check if a letter x is a
vowel with the expression x in VOWELS. Remember - to get a word except for the first letter, you can use word[1:].

Run the provided *test_translator* function to test your function against the following:
- boot → ootbay
- image → imagehay
- pig → igpay
- latin → atinlay


Once that is working, add on the following challenges:

1 - Take user input and convert it to pig latin, printing it out for the user.

2 - Handle words that start with a blend of consonants, like chip.  It should convert to ipchay, not hipcay.

3 - Converting one word to Pig Latin is okay, but it would be more useful to be able to convert whole sentences; so for this exercise, we’ll use raw input to ask the user for a full sentence and translate it, word by word. It’s tricky for us to deal with punctuation and numbers with what we know so far, so instead, ask the user to enter only words and spaces. You can convert their input from a string to a list of strings by calling split on the string; also, you can use lower to make a string all lowercase:
```python
>>> phrase = ’My namE is JohN SmIth’
>>> word_list = phrase.split()
>>> print word_list
[’My’, ’namE’, ’is’, ’JohN’, ’SmIth’]
>>> lowercase_phrase = phrase.lower()
>>> print lowercase_phrase
’my name is john smith’
```

Using a list of words, you can go through each word and convert it to Pig Latin.

Hint: It will make your life much easier - and your code much better - if you separate tasks into functions, e.g.  have a function that converts one word to Pig Latin rather than putting it into your main program code.

4 - Handle punctuation.
"My name is Billy." → "yMay amenay ishay illyBay."

5 - Handle uppercase letters.
"My name is Billy." → "Ymay amenay ishay Illybay."
