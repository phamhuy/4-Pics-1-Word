"""
Date Created: June 17, 2017
Project: 4 Pics 1 Word Solution
Team Members: Huy Pham, Loc Phan, Minh Huynh
"""

if __name__ == "__main__":
    im = input_image()
    print solution(im)

"""
Function: solution
Argument:
    im (3-d numpy array) - a screenshot of a puzzle from a phone
Return:
    answer (string) - The solution to the puzzle
    
Description:
    This function takes an input as an rgb image screenshot
    of a puzzle in the game 4-pics-1-word and give a solution
    to the puzzle
"""
def solution(im):
    # Process image to extract info from the image
    word_size, letters, pics = process_image(im)

    # Generate words from the word size and the list of letters
    dictionary = import_dictionary()
    possible_words = generate_words(dictionary, word_size, letters)

    # Generate labels from the 4 pics
    labels = generate_labels(pics)

    # Generate solutions
    possible_solutions = generate_solutions(possible_words, labels)

"""
Function: process_image
Argument:
    im (3-d numpy array) - a screen shot of a puzzle from a phone
Return:
    word_size (int) - the size of the solution word
    letters (list)  - the 12 letters given by the puzzle
    pics (list)     - the 4 pictures given by the puzzle
Description:
    Extracting word size, letters, and 4 pictures given by the puzzle
    from the input screenshot image
"""
def process_image(im):
    return (None, None, None)

"""
Function: import_dictionary
Argument: None
Return:
    dictionary (set) - a set of words in a dictionary
Description:
    Input a dictionary text file, parse all words in the dictionary
    to a set, and return the set.
"""
def import_dictionary():
    return None

"""
Function: generate_words
Argument:    
    word_size   (int)   - the size of the solution word 
    letters     (list)  - a list of 12 letters
Return:
    possible_words (list) - a list of possible words
Description:
    dictionary  (list)   - a set of words
    This function generates a list of all possible words that has
    the size specified by word_size and is a valid English word
"""
#Loc's
def generate_words(word_size, letters):
    #1. Read file from dictionary text
    with open('English.txt') as f:
        {int(size): word for line in f for (size, word) in (line.strip().split(None, 1),)}
    #2. Make a DICTIONARY type base on word size

    #3. Go through the DICTIONARY with same word size, check if the word has
    #the characters in letters list
    
    return []


"""
Function: generate_labels
Argument:
    pics (list): list of 4 pictures
Return:
    labels (list): list of labels
Description:
    This function takes the 4 pictures and makes a request to google cloud service,
    which returns a json objects containing labels for each picture, then parses
    the json objects into a list of labels
"""
def generate_labels(pics):
    return []

"""
Function: generate_solutions
Argument:
    possible_words (list)   - list of words
    labels (list)           - list of labels
Return:
    solutions (list) - list of solutions
Description:
    This function cleverly matches words in possible_words and labels,
    and return all matches.
"""
def generate_solutions(possible_words, labels):
    return []

"""
Function: input_image
Argument: None
Return:
    im (3-d numpy array) - an in input image
Description:
    This function inputs a screenshot of the puzzle and return the input image
"""
def input_image():
    return None


