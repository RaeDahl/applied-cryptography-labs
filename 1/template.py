# Et tu, Brute?
#
# Team Name: Hashbrowns
# Members: 
# A program that attempts to solve cipher texts that are shifted by some number.

import sys

# the alphabet
ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()-_=+[{]}\\|;:'\",<.>/? "

# read ciphertext
ciphertext = sys.stdin.read()

# generate candidate plaintexts
poss_plaintexts = {}

for shift in range(len(ALPHABET)):

    current_plaintext = []

    for char in ciphertext:
        print(char)

        #find char in alphabet
        try:
            position = ALPHABET.index(char)

            #shift
            if position + shift >= len(ALPHABET):
                position = (position + shift) - len(ALPHABET)
            else:
                position += shift

            # add char to plaintext
            current_plaintext.append(ALPHABET[position])
        except ValueError: # append chars not in alphabet directly
            current_plaintext.append(char)
    
    # add plaintext to list of possibilities
    poss_plaintexts[shift] = current_plaintext

# screen plaintexts with dictionary
likely_plaintexts = {}

# load dictionary file
with open("dictionary.txt", "r") as dictionary:

    for shift, text in poss_plaintexts:

        # Split into words by spaces
        words = text.split(" ")

        # find how many words are in dictionary
        recognized_words = 0

        for word in words:
            

            # check proportion of recognized words to total words
            if recognized_words / words >= 0.75:
                likely_plaintexts[shift] = text

# output plaintext and shift

