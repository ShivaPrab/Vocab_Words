def read_in_words(filename, separator):
    """
    Given a csv file full of vocabulary words + Frequency,
    read in the words into a list. 
    Input: String corresponding to csv file with words
    Output: List of words from CSV file
    """
    with open(filename, newline='') as file_words: 
        word_lists = []
        reader = csv.reader(file_words, delimiter=separator, \
        quotechar = quote)
        
        for words in file_words:
            word_lists.append(words)
    return word_lists


def define_found_word():
    """
    Grabs the a given word's definition
    Input- get_word(): 
    Output- String consisting of the word's Part of Speech & Definiition
    """
    valid_word = False
    while (not valid_word):
        word = get_word()
        if (dictionary.meaning(word, disable_errors=True)):
            print(word.upper() + "\n")
            defs = dictionary.meaning(word)
            for k, v in defs.items():
                print(str(k) + ": " + str(v).strip("[]\'\"").replace("\'", "")
            valid_word = True