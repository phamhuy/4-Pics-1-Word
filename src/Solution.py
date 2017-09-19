"""
Date Created: June 17, 2017
Project: 4 Pics 1 Word Solution
Team Members: Huy Pham, Loc Phan, Minh Huynh
"""
import cv2
import numpy as np
from PIL import Image
from scipy.misc import imresize

def find_longest_lines(im):
    """Returns the longests horizontal and vertical lines.
    
    im (grayscale image) - an image containing the 4 pictures of the puzzle.
    
    """
    hor_lines = np.sum(im, 1)
    ver_lines = np.sum(im, 0)

    # Sorting
    hor_indices = np.argsort(hor_lines)[::-1]
    ver_indices = np.argsort(ver_lines)[::-1]

    return hor_indices, ver_indices, hor_lines, ver_lines

def extract_4_pics(im_rgb, im):
    """Returns the 4 pictures from the given puzzle image.
    
    im_rgb (rgb image) -- the original puzzle image.
    im (grayscale image) -- an image containing 4 puzzle pictures only. 
    
    """
    _, w = im.shape
    im_edge = cv2.Canny(im, 50, 50);
    
    # Find indices of the longest horizontal and vertical lines
    hor_indices, ver_indices, hor_counts, ver_counts = find_longest_lines(im_edge)

    # Find the 4 longest horizontal lines
    hor_indices = np.sort(hor_indices[:8])
    hor_lines = np.array([hor_indices[0], 0, 0, 0])
    
    # line 2-4
    cur = 0;
    thresholds = [0.42*w, w/50];
    for i in range(cur,8):
        if hor_indices[i] - hor_lines[cur] > thresholds[cur%2]:
            cur += 1;
            hor_lines[cur] = hor_indices[i];
        if cur == 3:
            break
    
    # vertical lines
    ver_indices = np.sort(ver_indices[:8]);
    ver_lines = np.array([ver_indices[0], 0,0,0]);
    
    # line 2-4
    cur = 0;
    for i in range(cur, 8):
        if ver_indices[i] - ver_lines[cur] > thresholds[cur%2]:
            cur += 1;
            ver_lines[cur] = ver_indices[i];
        if cur == 3:
            break
        
    im[:,ver_lines] = 255
    im[hor_lines,:] = 255
    
    # Extract images
    pic1 = im_rgb[hor_lines[0]:hor_lines[1], ver_lines[0]:ver_lines[1], :]
    pic2 = im_rgb[hor_lines[0]:hor_lines[1], ver_lines[2]:ver_lines[3], :]
    pic3 = im_rgb[hor_lines[2]:hor_lines[3], ver_lines[0]:ver_lines[1], :]
    pic4 = im_rgb[hor_lines[2]:hor_lines[3], ver_lines[2]:ver_lines[3], :]
    pics = [pic1, pic2, pic3, pic4]
    
    return pics

def extract_word_size(im):
    """Returns the word size from the given image.
    
    im (grayscale image) -- an image containing squares where 
                            the number of squares is the word size.
    
    """
    im_edge = cv2.Canny(im, 50, 100)
    
    # Find indices of the longest horizontal and vertical lines
    _, _, _, ver_counts = find_longest_lines(im_edge)
    
    # Average height of the 3 longest vertical lines
    h_avg = np.mean(np.sort(ver_counts)[::-1][:6])
    temp = ver_counts / h_avg
    temp = temp[temp > 0.8]
    
    return temp.size/2

def extract_letters(im):
    """Return a list of letters in the given image.
    
    im (grayscale image) -- an image containing letters.
    
    """
    im_edge = cv2.Canny(im, 50, 100)
    
    # Find indices of the 6 horizontal lines and 12 vertical lines of the letters
    hor_indices, ver_indices, _, _ = find_longest_lines(im_edge)
    hor_lines = sorted(hor_indices[1:7])
    ver_lines = sorted(ver_indices[:12])
    for l in hor_lines:
        im_edge[l,:] = 255
    for l in ver_lines:
        im_edge[:,l] = 255
    from scipy.misc import imsave
    imsave('im_edge.png', im_edge)
    
    # Extract each letter
    letters = []
    data = np.load('data.npy')
    z = 0
    for i in range(2):
        for j in range(6):
            im_letter = im[hor_lines[i*3]: hor_lines[i*3 + 1], ver_lines[j*2] : ver_lines[j*2 + 1]]
            if True or z == 7 or z == 8:
                imsave(str(z) + '.png', im_letter)
            im_letter = imresize(im_letter, (15, 15), 'nearest') > 127
            im_letter = im_letter.astype(int)
            print z
            z += 1
            print im_letter
            letter = chr(np.argmin(np.sum(np.sum(np.abs(data - im_letter), 1), 1)) + ord('a'))
            letters.append(letter)
    
    print 'letters =', letters
    return letters

def process_image(im):
    """Extracts word size, letters, and 4 pictures from the given image.
    
    im (RGB image) -- a screen shot of a puzzle from a phone.
    
    """
    h, _, _ = im.shape
    im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    
    # Divide the picture into 3 regions
    l1 = int(0.65*h)
    l2 = int(0.77*h)
    im1 = im_gray[:l1,:]
    im2 = im_gray[l1+1:l2,:]
    im3 = im_gray[l2+1:,:]
    
    # Extract 4 pictures
    pics = extract_4_pics(im, im1)
    
    # Extract the word size
    word_size = extract_word_size(im2)
    
    # Extract the letters
    letters = extract_letters(im3)
    

    return word_size, letters, pics

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
    
    im (RGB image) -- the image containing the puzzle.

    """
    # Process image to extract info from the image
    word_size, letters, pics = process_image(im)

    # Generate words from the word size and the list of letters
    possible_words = generate_words(word_size, letters)

    # Generate labels from the 4 pics
    labels = generate_labels(pics)

    # Generate solutions
    possible_solutions = generate_solutions(possible_words, labels)
    
    return possible_solutions

def input_image():
    """Returns the RGB image containg the puzzle."""
    im = cv2.imread('im.png')
    return im


if __name__ == "__main__":
    im = input_image()
    print solution(im)
