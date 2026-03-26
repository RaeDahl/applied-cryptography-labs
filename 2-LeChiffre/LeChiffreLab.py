# Le Chiffre
# Team Name: Hashbrowns
# Members:
# A program that attempts to solve cipher texts that are shifted by some number.
# For the thresholds, we were able to get ciphertext-1= , ciphertext-2= , ciphertext-3= , ciphertext-4= , and the doubly encrypted=

import sys

# the alphabet
ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()-_=+[{]}\\|;:'\",<.>/? "
# ALPHABET = " -,;:!?/.'\"()[]$&#%012345789aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxyYzZ"
THRESHHOLD = 0.7

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