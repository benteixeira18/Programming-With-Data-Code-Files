'''

DS2001 Weekly Exercise
Benjamin Teixeira
    
Filename: cex.py
    
Description: 2D List (consumer expenditure survey)

# Acceess elements of a 2D List:
    List_1 = [[1,2,3],[4,5,6],[7,8,9]]
    List_1[0] = [1,2,3]
    List_1[0][1] = 2
    
# Create a pie chart:
    import matplotlib.pyplot as plt
    plt.pie([0.7,0.3], labels = ["Game Developer", "Apple"])
    
# Find position of "AGE" in the list ["NEWID", "AGE", "AGE_SPOUSE"]:
    age_index = ["NEWID", "AGE", "AGE_SPOUSE"].index("age")
    print(age_index)
    
# with open (filename, "r") as infile:
    csv_file = csv.reader(infile, delimiter = ",")
    
'''
# import libraries here
import matplotlib.pyplot as plt
import csv

# write functions here
def read_data(filename):
    """name: read_data
        input: filename
        returns: header and data
        as lists"""
        
    # create lists of header and data
    data = []
    
    # read in csv data
    with open (filename, "r") as infile:
        csv_file = csv.reader(infile, delimiter = ",")
        
        # for loop to append data and separate header
        for row in csv_file:
            data.append(row)
    header = data[0]
    data = data[1:]
    return header, data

def convert_to_float(header, data):
    """name: convert_to_float
        input: header (list), 
                data (list of lists)
        result: header (list), 
                data (updated l.o.l.,
                      floats)
        for improved visualization"""
        
    # create header index for total expenditure and entertainment
    total_index = header.index("TOTAL_EXPENDITURE")
    entertainment_index = header.index("ENTERTAINMENT")
    
    # convert data in floats through grouping expenditure (total_index) 
    # and entertainment (entertainment_index) columns together in a range
    for row_index in range(len(data)):
        for col_index in range(total_index, entertainment_index + 1):
            data[row_index][col_index] = float(data[row_index][col_index])
            
    return header, data

def get_food_percentage(header, data):
    """name: get_food_percentage
        input: header, data
        result: percentage of
        expenditures as food"""
    
    # create food index to calculate percentage of expenditures by food
    total_index = header.index("TOTAL_EXPENDITURE")
    food_index = header.index("FOOD")
    
    # create list to store percentage through for loop
    percentage_lst = []
    for row in data:
        percentage = row[food_index]/row[total_index]
        percentage_lst.append(percentage)
        
    return percentage_lst

def get_percentage_age50(expd_type, header, data):
    """name: get_percentage_age50
    input: expd_type, age and expenditure
    result: percent of expenditures
    over and under 50 years old"""
    
    # create age index from header
    total_index = header.index("TOTAL_EXPENDITURE")
    type_index = header.index(expd_type)
    age_index = header.index("AGE")
    
    # create expd_type lists for below/above age 50 expenditures
    above50 = []
    below50 = []
    
    for row in data:
        percentage = row[type_index]/row[total_index]
        if float(row[age_index]) >= 50:
            above50.append(percentage)
        else:
            below50.append(percentage)
            
    return [sum(above50)/len(above50), sum(below50)/len(below50)]
    
    
def main():
    # call read_data function here
    header, data = read_data("consumer_expenditure_sample.csv")
    print(header, data)
    
    # call convert_to_float function here
    header, data = convert_to_float(header, data)
    print(data)
    
    # call get_food_percentage function here
    food_lst = get_food_percentage(header, data)
    print(sum(food_lst)/len(food_lst))
    
    # call get_percentage_age50 function here 
    print(get_percentage_age50("FOOD", header, data))
    
main()
