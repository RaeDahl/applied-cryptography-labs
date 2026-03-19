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
poss_plaintexts = []

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
    poss_plaintexts.append("".join(current_plaintext))

for text in poss_plaintexts:
    print(f"{text}\n")

# screen plaintexts with dictionary

# output plaintext and shift

