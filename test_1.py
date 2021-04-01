'''
Project Overview: 
This simple project aims to create usable sets of FlashCards, complete with
the definition of a word, it's synonyms, and it's antonyms. The user should be
able to randomly group these flashcards and create their own sets. 
Objectives: 
1.) More Experience Writing a Well Formatted Python Project and Script
2.) Help Create usable material to study for the GRE 
This Script: 
Picking a Random GRE word from our Txt File
    Note, this script will only generate a random word and find the following: 
    1.) The word's definition
    2.) Synonymns (words with similiar meaning)
    3.) Antonymns (words with opposite meaning)
''' 

import random
import regex
from PyDictionary import PyDictionary
dictionary=PyDictionary() #necessary from documentation

file = open(r"Vocab_Words\Data\Words_Initial.txt") # Assume a well formatted txt file 
words = file.read().split("\n")


def get_word():
    """
    Finds a random word from our created list and spit is out
    """
    valid_word = False
    while (not valid_word):
        index = random.randint(0,len(words)-1)
        word = words[index]
        if (word[0]):
            valid_word = True
            return word

print(get_word())

def define_word():
    """
    Using the get_word function, we grab that word's corresponding definition, synonymns, and antonymns 
    """
    valid_word = False
    while (not valid_word):
        word = get_word()
        if (dictionary.meaning(word, disable_errors= True)):
            print(word.upper() + "\n")
            good_words = dictionary.meaning(word)
            for k, v in good_words.items():
                print(str(k) + ": " + str(v).strip("[]"))
            
            syns = dictionary.synonym(word)
            if syns:
                s = ""
                for syn in syns:
                    s += syn + ", "
                print("\n Synonyms: " + s[:-2] + "\n")

            ants = dictionary.antonym(word)
            if ants:
                a = ""
                for ant in ants:
                    a += ant + ", "
                print("\n Antonyms: " + a[:-2] + "\n")

            valid_word = True

print("Finding a random word out out:", len(words), "words")

print(define_word())