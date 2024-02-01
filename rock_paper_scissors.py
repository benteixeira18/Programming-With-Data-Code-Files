.'''

DS2000 Spring 2022
Benjamin Teixeira
    
Filename: rock_paper_scissors.py
    
Description: determining who will win rock, paper, scissors, shoot
for the last Khoury Dunkin' coffee!
    
'''
# import random for strategy implementation
import random as rnd

# import matplotlib for data visualization
import matplotlib.pyplot as plt

def main():
    
    # set baseline values to track games
    strange_win = 0
    rachlin_win = 0
    tie = 0
    # introducing move_r here
    move_r = "rock"
    
    # create while loop, outline strategies and establish winning structure
    while True:
        strange = rnd.randint(1,100)
        # if strange throws rock...
        if strange <= 70:
            move_s = "rock"
            if move_r == "paper":
                rachlin_win += 1
            if move_r == "scissors":
                strange_win += 1
            if move_r == "rock":
                tie += 1
            move_r = "paper"
        # if strange throws paper...
        elif 71 <= strange <= 90:
            move_s = "paper"
            if move_r == "scissors":
                rachlin_win += 1
            if move_r == "rock":
                strange_win += 1
            if move_r == "paper":
                tie += 1
            move_r = "scissors"
        # if strange throws scissors
        elif 91 <= strange <= 100:
            move_s = "scissors"
            if move_r == "rock":
                rachlin_win += 1
            if move_r == "paper":
                strange_win += 1
            if move_r == "scissors":
                tie += 1
            move_r = "rock"
            
        # break while loop once someone gets to 10,000 wins
        if rachlin_win == 10000:
            print("John wins the Khoury Coffee!")
            break
        elif strange_win == 10000:
            print("Strange wins the Khoury Coffee!")
            break
    
    # report teh final results    
    print("Rachlin Wins:", rachlin_win)
    print("Strange Wins:",strange_win)
    print("Ties:",tie)
    
    # visualize the data
    plt.figure(figsize = (6,5), dpi = 200)
    plt.bar("Rachlin Wins", rachlin_win, color = "red", label = "Rachlin")
    plt.bar("Strange Wins", strange_win, color = "blue", label = "Strange")
    plt.bar("Ties", tie, color = "green", label = "Tie")
    # label the data and save the visualization
    plt.xlabel("Outcome")
    plt.ylabel("Count")
    plt.title("Rock, Paper, Scissors, Shoot!")
    plt.legend()
    plt.savefig("rock.png")
    
main()

