'''

DS2001 Weekly Exercise 8
Benjamin Teixeira
    
Filename: starbucks.py
    
Description:
    
'''
# import libraries here
import csv
import matplotlib.pyplot as plt

# write read_data function here
def read_data(filename):
    """name: read_data
        input: filename
        result: header (list of strings)
                menu (list of lists)"""
    
    # create starbucks_menu list from reading in file
    starbucks_menu = []
    with open (filename, "r") as infile:
        csv_file = csv.reader(infile, delimiter = ",")
        for row in csv_file:
            starbucks_menu.append(row)
    
    # separate header
    header = starbucks_menu[0]
    data = starbucks_menu[1:]
    
    return header, data

def retrieve_smoothies(header, data):
    """name: retrieve_smoothies
        input: header, data (lists of strings)
        result: list of smoothie products"""
    
    # report beverage column from header, append values into smoothie list
    beverage_index = header.index("Beverage_category")
    smoothies_lst = []
    
    for row in data:
        if row[beverage_index] == "Smoothies":
            smoothies_lst.append(row)
        
    return smoothies_lst

def count_beverage_category(header, data):
    """name: count_beverage_category
        input: header, data
        result: int, num. of distinct categories
                ex: Coffee, Smoothie, Espresso, etc."""
                
    # use header.index, type_lst to separate beverage column
    beverage_index = header.index("Beverage_category")
    type_lst = []
    
    # if ___ not in statement to seperate categories of beverages
    for row in data:
        if row[beverage_index] not in type_lst:
            type_lst.append(row[beverage_index])
            
    return len(type_lst)
    
def main():
    
    # call read_data function here
    header, data = read_data("starbucks_menu.csv")
    
    # call retrieve_smoothies function here
    print(len(retrieve_smoothies(header, data)))
    
    # call count_beverage_category function here
    print(count_beverage_category(header, data))

main()