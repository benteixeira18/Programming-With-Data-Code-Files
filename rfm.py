'''

DS2001 Spring 2022
Benjamin Teixeira
    
Filename: rfm.py
    
Description: identifying high-value customers using for loops

Helpful techniques:

.split("\t"): split a string into a list, separator inside parantheses

for loop vs. while loop: auto-incrementing for the iteration value

# for loop iteration by value:
    mylist = ["hi", "mango", "cat"]
    for i in list:
        print(i)
    hi
    mango
    cat
# for loop iteration by position:
    mylist = [1,30,29,28,27]
    for i in range(2,len(mylist)):
        print(mylist[i])
    29
    28
    27   
RFM: Recency, frequency, monetary value
    
'''
# import libraries
import matplotlib.pyplot as plt

# main exercise
def main():
    
    # initialize constants
    
    expenditure_lst = []
    trips_lst = []
    
    # read in rfm.txt data
    with open ("rfm.txt", "r") as infile:
        expenditure = infile.readline().split("\t")
        trips = infile.readline().split("\t")
        
        # for loops: iterate expenditures & trips by value
        for i in expenditure:
            expenditure_lst.append(float(i))
        for i in trips:
            trips_lst.append(int(i))
        
        # for loops: iterate by position (BONUS)
        for i in range(len(expenditure)):
            expenditure[i] = float(expenditure[i])
            trips[i] = int(trips[i])
    
    # quality assurance    
    print("Expenditures per Month:", expenditure_lst)
    print("Trips per Month:", trips_lst)
    
    # visualize the data
    plt.figure(figsize = (7,5), dpi = 200)
    plt.bar(range(1,25), expenditure)
    plt.xlabel("Month")
    plt.ylabel("Spending Amount ($) ")
    plt.title("Monthly Expenditures over 24 Month Period")
    plt.savefig("rfm.png")
    
    # iterate by value to report monthly expenditure
    for i in expenditure_lst:
        print(round(i))
        
    # iterate by position to report monthly expenditure
    for i in range(len(expenditure_lst)):
        print(round(expenditure_lst[i]))
        
    # while loop to report expenditure by month
    month = 0
    while month < len(expenditure_lst):
        print(round(expenditure_lst[month]))
        month += 1
        
    # create and report monetary value list with for loop
    average_value = []
    monetary_spending = 0
    month = 0
    for i in range(len(expenditure_lst)-1):
        if expenditure_lst[i] > 0:
            # add total expenditures together
            monetary_spending += expenditure_lst[i]
            month += 1
        # calculate final average monetary value at month 24
        monetary_value = monetary_spending / month
        # append average_value to create list of average monetary values
        average_value.append(round(monetary_value))
    print("Monetary Spending over 24 Months: $", round(monetary_spending))
    print("Changing Avg. Monetary Value over 24 Months: $", average_value)
    print("Final Avg. Monetary Value: $", round(monetary_value))
            
main()
        
