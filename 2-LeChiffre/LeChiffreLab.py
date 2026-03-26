# Le Chiffre
# Team Name: Hashbrowns
# Members: Brady Burns, CJ Sturiale, Rachel Dahl, Victor Kwentoh, Asante Riser
# A program that attempts to solve cipher texts that are shifted by some number.
# For the thresholds, we were able to get ciphertext-1= , ciphertext-2= , ciphertext-3= , ciphertext-4= , and the doubly encrypted=

import sys

# the alphabet
ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()-_=+[{]}\\|;:'\",<.>/? "
# ALPHABET = " -,;:!?/.'\"()[]$&#%012345789aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxyYzZ"
LEN_THRESHHOLD = 1
WORD_THRESHHOLD = 0.7
AVG_WORD_LEN = 5
DICTIONARY_PATH = "dictionary-1.txt"

# Decode vigenere
def decrypt(ciphertext: str, key: str):

    # extend key
    extended_key = []
    i = 0
    while len(extended_key) < len(ciphertext):
        extended_key.append(key[i%len(key)])
        i += 1
    
    # decrypt with key
    plaintext = []
    i = 0
    for i in range(len(ciphertext)):
        shift = ALPHABET.index(extended_key[i])
        plaintext[i] = ALPHABET[ALPHABET.index(ciphertext[i]) + shift]

    # convert to string and output
    return "".join(plaintext)

# check if output makes sense
def check_key_validity(ciphertext: str):
    words = text.split(" ")

    # check average word length
    words_per_text = len(words)/len(ciphertext)
    if words_per_text > AVG_WORD_LEN - LEN_THRESHHOLD and words_per_text < AVG_WORD_LEN - LEN_THRESHHOLD:
        recognized_words = 0
        for word in words:
            if word in dictionary and len(word) >= 1:
                recognized_words += 1
        if recognized_words / len(words) >= WORD_THRESHHOLD:
            return True
        
    return False

###MAIN###
# get input from stdin
ciphertext = sys.stdin.read()

with open(DICTIONARY_PATH, "r") as dictionary_file:
    dictionary = dictionary_file.read()

poss_plaintexts = {}

# TODO: add some preliminary filtering here?
for key in dictionary:
    candidate = decrypt(ciphertext, key)
    if check_key_validity(candidate):
        poss_plaintexts[key] = candidate

# output
for key, text in poss_plaintexts.items():
    print(f"Key: {key}\n{text}")
