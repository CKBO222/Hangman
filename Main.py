"""
This is an attempt at a Hangman game.
"""
from random import *
from functions import *

def main():
    
    num_misses = 0
    star_found = True
    word_file = open("word_list.txt", 'r')          # Read in the file
    word_list = word_file.read().splitlines()       # eliminate newline chars       
    word_file.close()                               # close the file
    
    chosen_word = word_selection(word_list)         #This chooses the word
    num_letters = letter_count(chosen_word)         #Then finds the amount of letters
    displayed_word = ["*"] * num_letters            #Then initializes the list
    letters_guessed = []
    
    while star_found == True and num_misses < 6:    #The conditions are 6 misses to lose
        star_found = False                          # or not having any blanks remaining to win
        display_word(displayed_word)
        print("\n")
        display_letters_guessed(letters_guessed)    #Display the letters you have guessed
        letter_guess = ask_for_letter(letters_guessed)  #Ask for another letter
        t_or_f = check_for_letter(chosen_word, letter_guess, displayed_word) #Check for letter
        if t_or_f == False:                          #If letter not found, add a miss
            num_misses = misses(num_misses)
        for i in range(num_letters):
            if displayed_word[i] == "*":            #Display the word you are trying to guess
                star_found = True
        if num_misses == 6:                         #When you lose
            print("You have lost!")
            print("The word was",chosen_word)
        if star_found == False:                     #When you win
            print(chosen_word)
            print("You have won!")
        display_hangman(num_misses)                 #Draws the hangman
main()