"""
Date Created: June 17, 2017
Project: 4 Pics 1 Word Solution
Team Members: Huy Pham, Loc Phan, Minh Huynh
"""


"""
Function solution
Argument:
    im - a screenshot of a puzzle from a phone
Return:
    the solution to the puzzle
    
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

def process_image(im):
    return (None, None, None)

def import_dictionary():
    return None

def generate_words(dictionary, word_size, letters):
    return []

def generate_labels(pics):
    return []

def generate_solutions(possible_words, labels):
    return []

def input_image():
    return None

if __name__ == "__main__":
    im = input_image()
    print solution(im)
