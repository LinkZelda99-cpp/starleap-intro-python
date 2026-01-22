# 11.10  Exercises

## Exercise 1  
Write a function that reads the words in words.txt and stores them as keys in a dictionary. It doesn’t matter what the values are. Then you can use the in operator as a fast way to check whether a string is in the dictionary.

If you did Exercise 10, you can compare the speed of this implementation with the list in operator and the bisection search.

## Exercise 2  
Read the documentation of the dictionary method setdefault and use it to write a more concise version of invert_dict. Solution: https://thinkpython.com/code/invert_dict.py.

## Exercise 3
You can skip this one

## Exercise 4  
If you did Chapter 10 Exercise 7, you already have a function named has_duplicates that takes a list as a parameter and returns True if there is any object that appears more than once in the list.

Use a dictionary to write a faster, simpler version of has_duplicates. Solution: https://thinkpython.com/code/has_duplicates.py.

## Exercise 5  
Two words are “rotate pairs” if you can rotate one of them and get the other (see rotate_word in Exercise 5).

Write a program that reads a wordlist and finds all the rotate pairs. Solution: https://thinkpython.com/code/rotate_pairs.py.

## Exercise 6  
Here’s another Puzzler from Car Talk (http://www.cartalk.com/content/puzzlers):

This was sent in by a fellow named Dan O’Leary. He came upon a common one-syllable, five-letter word recently that has the following unique property. When you remove the first letter, the remaining letters form a homophone of the original word, that is a word that sounds exactly the same. Replace the first letter, that is, put it back and remove the second letter and the result is yet another homophone of the original word. And the question is, what’s the word?
Now I’m going to give you an example that doesn’t work. Let’s look at the five-letter word, ‘wrack.’ W-R-A-C-K, you know like to ‘wrack with pain.’ If I remove the first letter, I am left with a four-letter word, ’R-A-C-K.’ As in, ‘Holy cow, did you see the rack on that buck! It must have been a nine-pointer!’ It’s a perfect homophone. If you put the ‘w’ back, and remove the ‘r,’ instead, you’re left with the word, ‘wack,’ which is a real word, it’s just not a homophone of the other two words.

But there is, however, at least one word that Dan and we know of, which will yield two homophones if you remove either of the first two letters to make two, new four-letter words. The question is, what’s the word?


You can use the dictionary from Exercise 1 to check whether a string is in the word list.

To check whether two words are homophones, you can use the CMU Pronouncing Dictionary. You can download it from http://www.speech.cs.cmu.edu/cgi-bin/cmudict or from https://thinkpython.com/code/c06d and you can also download https://thinkpython.com/code/pronounce.py, which provides a function named read_dictionary that reads the pronouncing dictionary and returns a Python dictionary that maps from each word to a string that describes its primary pronunciation.

Write a program that lists all the words that solve the Puzzler. Solution: https://thinkpython.com/code/homophone.py.