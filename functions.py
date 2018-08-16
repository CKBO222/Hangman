from random import *

def word_selection(list_of_words):
    """
    This function randomly selects a word from the list that was read in.  That 
    will be the word the player tries to guess.
    """
    
    index = randrange(0, len(list_of_words))
    return list_of_words[index]

def letter_count(word):
    """
    This function will count the amount of letters in the chosen word.
    """
    
    word_chars = list(word)
    i = 0
    for i in range(len(word_chars)):
        i = i + 1
    return i

def ask_for_letter(letters_guessed):
    """
    This function asks the user to guess a letter.
    """
    letter = str(input("Guess a letter: "))
    letters_guessed.append(letter)
    return letter

def hits(num):
    """
    This function adds to and returns the current number of hits
    """
    
    num = num + 1
    return num

def misses(num):
    """
    This function adds to and returns the current number of misses
    """
    
    num = num + 1
    return num

def check_for_letter(chosen_word, letter_guess, display_list):
    """
    The function checks the letter the user guessed to see if it is in the word
    """
    letter_found = False
    
    word_as_list = list(chosen_word)                   #Break word up into a list
    
    for i in range(0, len(word_as_list)):              #If the letter is found in list
        if word_as_list[i].lower() == letter_guess:    #Change letter_found to true
            letter_found = True
            display_list[i] = letter_guess                   # Change the list that is displayed
            
    return letter_found

def display_word(display_list):
    """
    This function is for displaying the word
    """
    
    for i in range(len(display_list)):
        print(display_list[i], end="")
        
def display_letters_guessed(letters_guessed):
    """
    This function will display the letters the user has guessed
    """
    print("Letters guessed: ", end='')
    for i in range(len(letters_guessed)):
        print(letters_guessed[i], end='')
    
    print("\n")
def display_hangman(miss_count):
    """
    This function draws the hangman.
    """
    if miss_count == 0:
        print("-------------------")
        print("|                  |")
        print("                   |")
        print("                   |")
        print("                   |")
        print("                   |")
        print("             ______|_____")
    elif miss_count == 1:
        print("-------------------")
        print("  |                |")
        print("(x x)              |")
        print("                   |")
        print("                   |")
        print("                   |")
        print("             ______|_____")   
    elif miss_count == 2:
        print("-------------------")
        print("  |                |")
        print("(x x)              |")
        print("  |                |")
        print("                   |")
        print("                   |")
        print("             ______|_____")  
    elif miss_count == 3:
        print("-------------------")
        print("  |                |")
        print("(x x)              |")
        print(" /|                |")
        print("                   |")
        print("                   |")
        print("             ______|_____")   
    elif miss_count == 4:
        print("-------------------")
        print("  |                |")
        print("(x x)              |")
        print(" /|\               |")
        print("                   |")
        print("                   |")
        print("             ______|_____")  
    elif miss_count == 5:
        print("-------------------")
        print("  |                |")
        print("(x x)              |")
        print(" /|\               |")
        print(" /                 |")
        print("                   |")
        print("             ______|_____")
    elif miss_count == 6:
        print("-------------------")
        print("  |                |")
        print("(x x)              |")
        print(" /|\               |")
        print(" / \               |")
        print("                   |")
        print("             ______|_____")
    
    