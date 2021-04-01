# Vocab_Words
 
'''
Project Overview: 
This simple project aims to create usable sets of FlashCards, complete with
the definition of a word, it's synonyms, and it's antonyms. The user should be
able to randomly group these flashcards and create their own sets. 
Objectives: 
1.) More Experience Writing a Well Formatted Python Project and Script
2.) Help Create usable material to study for the GRE 

''' 

Code Quirks: 

1.) The word generated from "get_word()" is not the same as the word from "define_word()"
	in R, we can "set_seed" to keep the randomly generated word. But I'm unsure how to do that in Python

2.) There are several things that need to be done to clean up the print statements to make them look nice. 
	i.e. The synonyms list that we get back have brackets. Gross. 

3.) Is it legal for me to index the list by using "len(words)-1"? I'm unsure that is doing what I want it to

4.) Shiva is really, like really bad at reading in files. See "Test.py -> read_in_words. 
	I want to learn how to read in files using a function instead of just using a variable 

Changes needed to be made: 
1.) Attempt to unify "get_word()" & "define_word():" so the code is not repetitive. 

2.) Export a csv file with: word, part of speech, definition, syns, ants 
	if a word has 2 parts of speech, make 2 entries 



