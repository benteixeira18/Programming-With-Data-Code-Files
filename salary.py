'''

DS2000 Spring 2022
Benjamin Teixeira
    
Filename: salary.py
    
Description: reporting and determining favored 
NBA team based on historical salaries
    
'''
# import libraries
import matplotlib.pyplot as plt

def main():
    # read in data
    with open ("salary.txt", "r") as infile:
        infile.readline()
        data = infile.readlines()
    
    # parse the data
    for i in range(len(data)):
        data[i] = int(data[i])
    
    # visualize the data 
    plt.figure(figsize = (10,5), dpi = 200)
    plt.xticks([0,5000000,10000000,15000000,20000000,25000000,30000000],
               ["$0", "$5 Mil", "$10 Mil", "$15 Mil", "$20 Mil", 
                "$25 Mil", "$30 Mil"])
    plt.title("Distribution of Celtics Salaries between 1985 and 2018")
    plt.xlabel("Salaries")
    plt.ylabel("Team Data")
    
    # flip axis, add percentiles for readability
    plt.boxplot(data, vert = False, patch_artist = True)
    plt.text(0, 1.45, "Sources: Data World, RunRepeat")
    plt.text(-1500000, 0.80, "Min 25th Med 75th")
    plt.text(6250000,0.80, "Max   Outliers -------->")
    plt.text(6250000,1.20, "Avg: $7.90 Mil")
    plt.savefig("salary.png")
    plt.show()
    
main()
    

