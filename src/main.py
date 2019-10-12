# Author: Louis-Clément LEROUX
# File: main.py
# Date: 05/09/19
# Desc: Main file

### IMPORTS ##

import re
from operator import itemgetter
import reader as r

### NOTES ###

#TODO:

### CODE ###

def encode(message, key):
    """Encode a message using shilf encryption, with a specific key.

    Parameters :
    message -- the plaintext sentence
    key -- number of letter used of the shift

    Output :
    message -- the encrypted message

    """
    base = ord("A") # Get the number which correspond to A, for the base
    message = list(message.upper())
    for indice, letter in enumerate(message):
        if re.match("[A-Z]", letter) is not None: # We encode only letter
            newletter = ((ord(letter) + int(key) - base) % 26) + base  
            message[indice] = chr(newletter)
    
    return "".join(message)

def decode(message, key):
    """Decode a message using shilf encryption, with a specific key.

    Parameters :
    message -- the cipher sentence
    key -- number of letter used of the shift

    Output :
    message -- the decrypted message

    """
    base = ord("A") # Get the number which correspond to A, for the base
    message = list(message.upper())
    for indice, letter in enumerate(message):
        if re.match("[A-Z]", letter) is not None: # We encode only letter
            newletter = ord(letter) - key - base
            if newletter < 0:
                newletter += 26
            newletter += base
            message[indice] = chr(newletter)
    
    return "".join(message)


def decodeShilf(message):
    """Print an encrypted message with all the keys.

    Parameters :
    message -- the plaintext sentence

    """
    for i in range (26):
        print("Key {}: {}".format(i, decode(message, i)))


def getStat(message):
    """Get the frequency of every letter in a message.

    Parameters :
    message -- the plaintext sentence

    Output :
    tableMessage -- dictionary with letter - frequency (in %)

    """
    tableMessage = {}
    nbLetter = 0
    
    for letter in message:
        if re.match("[A-Z]", letter) is not None:
            nbLetter += 1
            if letter not in tableMessage:
                tableMessage[letter] = 1
            else:
                tableMessage[letter] += 1

    for key, value in tableMessage.items():
        tableMessage[key] = round(value*100/nbLetter,4) # Calcul the pourcentage of each letter

    return tableMessage


def totalVariationDistance(message):
    """Calcul the total variation distance for the letters in a message.

    Parameters :
    message -- the plaintext sentence

    Output :
    distance -- the total variation distance
    """
    message = message.upper()
    table = r.readTableStat() # Table with the frequency of each letter in english words
    tableMessage = getStat(message) # Table with the frequency of each letter in our message
    distance = 0

    for key, value in table.items():
        if key in tableMessage:
            distance += abs(float(value) - tableMessage[key])
        else:
            distance += float(value)
    
    distance = round(distance/2,4)

    return distance
    
def decodeShilfStat(message):
    """Decode and find the key of a encrypted message using statistics.

    Parameters :
    message -- the plaintext sentence

    Output :
    couple[1] -- the decrypted message

    """
    originalMessage = message
    listDistance = [[0, totalVariationDistance(message)]]
    key = 0
    while key < 25:
        message = decode(message, 1)
        key += 1
        listDistance.append([key, totalVariationDistance(message)])

    couple = min(listDistance, key=itemgetter(1))

    print("Coded with key {}, the message is:\n{}".format(couple[0], decode(originalMessage, couple[0])))
    return couple[1]



if __name__=="__main__":

    print("\n\n\t###  WELCOME TO MY SHIFT CIPHER PROGRAM ###\n\n")

    exitChoice = 0
    while exitChoice == 0:

        choice = input("\nWhat do you want to do?\n1: Encryption\n2: Decryption\n3: Exit\n")
        while (re.match("[123]", choice) is None):
            choice = input("Wrong entry.\nWhat do you want to do?\n1: Encryption\n2: Decryption\n3: Exit\n")
        
        if choice == "1":

            message = input("What is the message you want to encrypt?\n")
            key = input("Which key do you want to use?\n")
            print("Here the message encoded:\n")
            print(encode(message, key))

        elif choice == "2":

            message = input("What is the message you want to decrypt?\n")
            decodeShilfStat(message)
            choiceDecryp = input("Is it not the message expected?\n1: Print the message for all keys\n2: Back to the menu\n")

            while (re.match("[12]", choiceDecryp) is None):
                choice = input("Wrong entry.\nWhat do you want to do?\n1: Print the message for all keys\n2: Back to the menu\n")

            if choiceDecryp == "1":

                decodeShilf(message)

            elif choiceDecryp == "2":

                pass
        
        elif choice == "3":

            exitChoice = 1
            print("\nThank you for testing my program! See you soon!\n")