'''

DS2000 Spring 2022
Benjamin Teixeira
    
Filename: running.py
    
Description: reporting which Khoury professor ran the most amount 
of days in January and how many days they ran
    
'''
# import matplotlib for visualization
import matplotlib.pyplot as plt

def main():
    # establish constants to track days ran
    strange_days = 0
    rachlin_days = 0
    muzny_days = 0
    mosca_days = 0
    
    # read in the runner_data.txt data
    with open("runner_data.txt", "r") as infile:
        infile.readline()
        strange = infile.readline().split()
        rachlin = infile.readline().split()
        muzny = infile.readline().split()
        mosca = infile.readline().split()
        
    # establish lists for each runner's days & miles
    strange_lst = [i for i in strange[2:33]]
    rachlin_lst = [i for i in rachlin[2:33]]
    muzny_lst = [i for i in muzny[2:33]]
    mosca_lst = [i for i in mosca[2:33]]
    
    # convert runner's data into floats
    strange_float = []
    for i in strange_lst:
        strange_float.append(float(i))
    rachlin_float = []
    for i in rachlin_lst:
        rachlin_float.append(float(i))
    muzny_float = []
    for i in muzny_lst:
        muzny_float.append(float(i))
    mosca_float = []
    for i in mosca_lst:
        mosca_float.append(float(i))
     
    # calculate each runners' days ran 
    for i in strange_float:
        if i > 0:
            strange_days += 1
    for i in rachlin_float:
        if i > 0:
            rachlin_days += 1
    for i in muzny_float:
        if i > 0:
            muzny_days += 1
    for i in mosca_float:
        if i > 0:
            mosca_days += 1
            
    # create a list of cumulative days run & report the max
    days_lst = [strange_days, rachlin_days, muzny_days, mosca_days]
    if max(days_lst) == strange_days:
        print("Laney Strange ran the most in Jan w/", strange_days, "days!")
    elif max(days_lst) == muzny_days:
        print("Felix Muzny ran the most in Jan w/", muzny_days, "days!")
    elif max(days_lst) == rachlin_days:
        print("John Rachlin ran the most in Jan w/", rachlin_days, "days!")
    else:
        print("Ab Mosca ran the most in Jan w/", mosca_days, "days!")
    
    # establish the bar graph details
    rank = ["gold", "silver", "brown", "black"]
    plt.figure(figsize = (6,4), dpi = 500)
    plt.title("Khoury Running Metrics in January")
    plt.xlabel("Runner")
    plt.ylabel("# of Days Ran")
    plt.ylim(0,30)
    
    # plot the bar graph and save it for reference
    plt.bar("Ab Mosca", mosca_days, color=rank[0])
    plt.bar("Laney Strange", strange_days, color = rank[1])
    plt.bar("Felix Muzny", muzny_days, color = rank[2])
    plt.bar("John Rachlin", rachlin_days, color = rank[3])
    plt.savefig("running.png")

main()