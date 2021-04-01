'''
Project Overview: 

This simple project aims to create usable sets of FlashCards, complete with
the definition of a word, it's synonyms, and it's antonyms. The user should be
able to randomly group these flashcards and create their own sets. 

Objectives: 
1.) More Experience Writing a Well Formatted Python Project and Script
2.) Help Create usable material to study for the GRE 

This Script: 
Attempts to create sets. Each set will be exported to a csv

Col 1: Word 
Col 2: Word's Part of Speech 
Col 3: Word's Definition
Col 4: Set of Synonymns 
Col 5: Set of Antonymns 
''' 

import random
import regex
from PyDictionary import PyDictionary
dictionary=PyDictionary() #necessary from documentation

file = open(r"Vocab_Words\Data\Words_Initial.txt") 
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