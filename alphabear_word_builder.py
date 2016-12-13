#!/usr/bin/env python3

import sys

def generate_letter_count(word):
    letter_count = {}
    for letter in word:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count
	
def formable(word, letter_count):
    word_letter_count = generate_letter_count(word)
    word_set = set(word)
    for l in word_set:
        if (word_letter_count[l] > letter_count.get(l, 0)):
            return False
    return True

def generate_long_words(letter_list):
    letter_count = generate_letter_count(letter_list)
    letter_set = set(letter_list)
    current_best_word = ""
    word_list = []
    with open("words", "r") as f:
        while True:
            word = f.readline()
            if word == "": #Reached the End of the file
                break
            word = word.split("\n")[0]
            if len(word) >= len(current_best_word):
                if not (set(word) - letter_set):  #The word should not contain letters other than the one present in the letter set
                    if formable(word, letter_count):
                        word_list.append(word)
                        current_best_word = word
    print("Longest Word Possible : " , current_best_word)
    print("Other Possible Words : ", sorted(word_list, reverse = True))

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Usage " + sys.argv[0] + " <letter list from which to form words>")
	else:
		generate_long_words(list(sys.argv[1]))
