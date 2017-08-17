"""
Date Created: June 17, 2017
Project: 4 Pics 1 Word Solution
Team Members: Huy Pham, Loc Phan, Minh Huynh
"""

def process_image(im):
    """Extracts word size, letters, and 4 pictures from the given image.
    
    im -- a screen shot of a puzzle from a phone.
    
    """
    return (None, None, None)

def generate_words(word_size, letters):
    """Generates a list of all possible words that has
    the size specified by word_size and is a valid English word.

    dictionary  (set)   -- a set of words.
    word_size   (int)   -- the size of the solution word.
    letters     (list)  -- a list of 12 letters.
    
    """
    # Read file from dictionary text
    # Make a DICTIONARY base on word size:
    f = open('English.txt')
    dictionary = dict()
    for line in f:
        line = line.strip('\n')             #get rid of \n at the end of line
        if dictionary.has_key(len(line)):        
            dictionary[len(line)].append(line)
        else:
            dictionary[len(line)] = [line]  #the line in [] is important

    # Go through the DICTIONARY with same word size
    # Check if the word has the characters in letter list:
    possible_words = []
    for word in dictionary[word_size]:
        for letter in word:
            if letter not in letters:
                correct = False
                break
            else:            
                correct = True 
        if (correct):
            possible_words.append(word)    
    return possible_words

def generate_labels(pics):
    """Makes a request to google cloud service, and gets a response
    containing labels for each picture.
    
    pics (list) -- list of 4 pictures.
    
    """
    return []

def generate_solutions(possible_words, labels):
    """Matches words cleverly between words in possible_words and
    words in labels, and return all matches.
    
    possible_words (list)   -- list of words
    labels (list)           -- list of labels

    """
    return []

def solution(im):
    """Returns a solution to the puzzle in the given image.
    
    im (grayscale image) -- the image containing the puzzle.

    """
    # Process image to extract info from the image
    word_size, letters, pics = process_image(im)

    # Generate words from the word size and the list of letters
    possible_words = generate_words(word_size, letters)

    # Generate labels from the 4 pics
    labels = generate_labels(pics)

    # Generate solutions
    possible_solutions = generate_solutions(possible_words, labels)

def input_image():
    """Returns the image containg the puzzle."""
    return None


if __name__ == "__main__":
    im = input_image()
    print solution(im)
