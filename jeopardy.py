'''

DS2000 Spring 2022
Benjamin Teixeira
    
Filename: jeopardy.py
    
Description: plotting and comparing jeopardy earnings
between correct and incorrect final questions

Creating a bar graph
    
'''
'''
Test Case 1:
    In Schenider's 41 games, she won $1,384,800 total
    She won approximately $33,775.61 per game
    In Schenider's 41 final questions, she got 68% correct
    She earned $1,173,800 in games with correct final questions
    She earned $211,000 in games with incorrect final questions
'''
# import matplotlib for visualizing jeopardy earnings
import matplotlib.pyplot as plt

# start main function
def main():
    
    # establish baselines
    full_earnings = 0
    game_count = 0
    incorrect_q = 0
    correct_earnings = 0
    incorrect_earnings = 0
    
    # open schneider file data and create while loop
    filename = "schneider.txt"
    with open (filename, "r") as infile:
        while True:
            
            # read file data and end while loop
            earnings = infile.readline()
            question = infile.readline()
            if earnings == "" and question == "":
                break
            
            # convert earnings to float and strip question
            earnings = float(earnings)
            question = question.strip()
            
            # add up and report total earnings, find average
            full_earnings = full_earnings + earnings
            game_count = game_count + 1
            avg_earnings = round(full_earnings/game_count, 2)
            
            # separate correct and incorrect final questions
            if question == "Yes":
                color_c = "Blue"
                correct_earnings += earnings
            elif question == "No":
                color_nc = "Red"
                incorrect_earnings += earnings
                incorrect_q += 1
             
    # visualize the data
    plt.figure(figsize = (5,5), dpi = 200)
    plt.bar("Correct", correct_earnings, color = color_c)
    plt.bar("Incorrect", incorrect_earnings, color = color_nc)
    plt.xlabel("Final Question")
    plt.ylabel("Earnings [$ Mil.]")
    plt.ylim([0,1200000])
    plt.title("41-Game Jeopardy Run")
    plt.savefig("jeopardy.png")
                
    # find avgerage of correct questions using game
    correct = game_count - incorrect_q
    percent_cq = (round(correct / game_count, 2)) * 100
            
    # report findings to the user
    print("In Schneider's 41 games, she won $",full_earnings)
    print("On average, she won $",avg_earnings, "per game")
    print("She got",percent_cq,"% of her final questions correct")
    print("She earned $",correct_earnings, "with correct final questions")
    print("She earned $",incorrect_earnings,"with incorrect final questions")
       
main()