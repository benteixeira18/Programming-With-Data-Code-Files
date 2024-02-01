'''

DS2000 Spring 2022
Benjamin Teixeira
    
Filename: tottenham_stats.py
    
Description:  reporting tottenham's 5 season stats (revision)
    
'''
def tottenham(filename):
    """name: tottenham
        input: hotspurs.txt, containing goals and outcomes over
                the last 5 seasons for tottenham hotspurs football club
        result: structured metrics of matches and performance"""
            
    # placeholders to substitute min wins, max goals if new max/min occur
    min_wins = [0, 100000000]
    max_goals = [1000000, 0]
    
    # reading in data, pulling goals and outcome
    with open (filename, "r") as file:
        while True:
            
            # establishing season-wide consistent metrics, reset each season
            wins = 0
            losses = 0
            draws = 0
            wins_1 = 0
            first_10 = 0
            final_10 = 0
            
            # pulling goals and outcome from file, breaking when empty
            goals = file.readline()
            outcome = file.readline()
            if goals == "":
                break
            
            # splitting data to analyze individually, separate season
            goals = goals.split()
            outcome = outcome.split()
            season = goals[0]
            
            # comprehension to store data 1 by 1, report matches
            goals = [goal for goal in goals[1:39]]
            outcome_lst = [game for game in outcome[1:39]]
            matches = len(outcome_lst)
           
            # converting goals to int to count
            goals_lst = []
            for goal in goals:
                goals_lst.append(int(goal))
        
            # calculating seasonal records
            for game in outcome_lst:
                if game == "W":
                    wins += 1
                elif game == "L":
                    losses += 1
                else:
                    draws += 1
            
            # calculating wins with 1 goal
            for i in range(len(goals_lst)):
                if goals_lst[i] == 1 and outcome_lst[i] == "W":
                    wins_1 += 1
            
            # calculating season goals and goals in first & final 10 games
            first_10 = sum(goals_lst[0:10])
            final_10 = sum(goals_lst[-10:])
            sum_goals = sum(goals_lst)
            
            # calculating seasons with fewest wins, most goals
            if wins < min_wins[1]:
                min_wins = [season, wins]
            if sum_goals > max_goals[1]:
                max_goals = [season, sum_goals]
                
            # reporting tottenham season metrics
            print("Season:", season)
            print("Goals:", sum_goals)
            print("Matches:", matches)
            print("Record:", wins, "wins,", losses, "losses,", draws, "draws")
            print("Wins with 1 Goal:", wins_1)
            print("Start vs Finish:", first_10, "goals in 1st 10 games,", 
                  final_10, "goals in final 10 games")
            print()

    print("Worst Season:", min_wins[0], "with", min_wins[1], "wins")
    print("Highest Scoring Season:", max_goals[0], 
          "with", max_goals[1], "goals")

def main():
    
    # calling tottenham function
    data = tottenham("hotspurs.txt")
                           
main()
