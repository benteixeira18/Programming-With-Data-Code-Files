'''

DS2000 Spring 2022 Homework 6
Benjamin Teixeira 04/01/22
    
Filename: wheel.py
    
Description: Helping professor cheat on Wheel! Of! Fortune!
    
'''
# importing libraries, letter constants for cheat_sheat
import random as rnd
CON = ["B", "C", "D", "F", "G", "H", "J", "K", 
       "M", "P", "Q", "V", "W", "X", "Y", "Z"]
VOW = ["A", "I", "O", "U"]

def read_puzzles(filename):
    """name: read_puzzles
        input: filename (puzz.txt)
        result: list of puzzles from file, reading by row"""
   
    puzz_lst = []
    with open(filename, "r") as file:
        puzz_txt = file.readlines()
            
        # cleaning data for presenting in game
        for row in puzz_txt:
            puzz_clean = row.replace("\n", "")
            puzz_uppercase = puzz_clean.upper()
            puzz_lst.append(puzz_uppercase)
            
    return puzz_lst
    
def read_letters(filename):
    """name: read_letters
        input: filename
        result: reading in file in one text to count letters one by one"""
    
    letter_lst = []
    with open(filename, "r") as file:
        letter_txt = file.read()
        
        # cleaning data for counting in dictionaries
        for row in letter_txt:
            letter_clean = row.replace("\n", "")
            letter_uppercase = letter_clean.upper()
            letter_lst.append(letter_uppercase)
    
    return letter_lst
            
def letter_frequency(letter_lst):
    """name: letter_frequency
        input: puss_lst, letter_lst
        result: count, order of letters in puzz.txt
        stored in dictionaries for organization"""
    
    # creating dictionaries, labeling non_given letters
    con_dict = {}
    vow_dict = {}
    con_lst = ["B", "C", "D", "F", "G", "H", "J", "K", 
               "M", "P", "Q", "V", "W", "X", "Y", "Z"]
    vow_lst = ["A", "I", "O", "U"]
                
    # labeling non-given consonants, vowels in dictionarries
    for letters in con_lst:
        letter_count = letter_lst.count(letters)
        con_dict[letters] = letter_count
        
    for letters in vow_lst:
        letter_count = letter_lst.count(letters)
        vow_dict[letters] = letter_count
    
    # sorting & returning most common consonants & vowels
    con_sort = sorted(con_dict, key = con_dict.get, reverse = True)
    vow_sort = sorted(vow_dict, key = vow_dict.get, reverse = True)
    most_con = con_sort[:3]
    most_vow = vow_sort[0]
          
    return most_con, most_vow
    
def play_game(puzz_lst, most_con, most_vow):
    """name: play_game
        input: puzz_lst, most common consonants, most common vowel
        result: random puzzle, displayed letters, game played"""
    
    # selecting random puzzle from puzz.txt
    random_puzzle = rnd.choice(puzz_lst)
    puzz_fortune = ""
    
    # gathering given letters in puzzle
    for letter in random_puzzle:
        if letter not in (VOW + CON):
            puzz_fortune += letter + ""
        else:
            puzz_fortune += "_"
    
    # labeling non_given common letters in consideration
    cheat_letters = most_vow, most_con[0], most_con[1], most_con[2]
    puzz_cheat = ""
    
    # gathering non_given common letters in puzzle
    for letter in random_puzzle:
        if letter in (CON + VOW) and letter not in cheat_letters:
            puzz_cheat += "_"
        else:
            puzz_cheat += letter + ""
    
    # letting professor guess the puzzle once 
    print("Wheel! Of! Fortune! Puzzle:", puzz_fortune)
    print("Don't tell anyone... Here's some help!:", puzz_cheat)
    print("Enter in all-caps, with spaces and punctuation if necessary.")
    
    prof_guess = str(input("What's your guess, professor? "))
    
    # revealing if professor's guess was right or wrong
    if prof_guess == random_puzzle:
        print("Congrats! You struck fortune today, professor!")
    else:
        print("No fortune today! The answer is.....")
        
    return random_puzzle

def main():
    
    # reading puzzles and letters
    puzzles = read_puzzles("puzz.txt")
    letters = read_letters("puzz.txt")
    
    # calling letter_frequency function
    freq = letter_frequency(letters)
    most_consonants = freq[0]
    most_vowels = freq[1]
    print("Most Common Consonants:", most_consonants)
    print("Most Common Vowel:", most_vowels)
    
    # calling play_game function
    game = play_game(puzzles, most_consonants, most_vowels)
    print(game, "!!!!!!!")
    
main()
