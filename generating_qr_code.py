'''

DS2000 Spring 2022
Benjamin Teixeira
    
Filename: qr.py
    
Description: generating a QR code
    
'''
# import main libraries
import csv
import matplotlib.pyplot as plt

# write qr_code function
def read_positions(filename):
    """name: read_positions
        input: positions.csv
        result: qr code values"""
        
    # read in positions.csv, append posiitons list
    positions = []
    
    with open (filename, "r") as infile:
        csv_file = csv.reader(infile, delimiter = ",")
        for row in csv_file:
            positions.append(row)     
    
    return positions
   
# write int_conversion function
def int_conversions(positions):
    """name: int_conversions
        input: positions (list of strings)
        result: lists of int (rows, position)"""
    
    # create lists to store positions values
    positions_int = []
    for row in positions:
        row_lst = []
        
        # convert values to int and append for tracking
        for value in row:
            value = int(value)
            row_lst.append(value)
        positions_int.append(row_lst)
        
    return positions_int

def qr_code(positions_int):
    """name: qr_code
        input: data (posiitons (list of ints))
        result: qr color code green vs. white"""
    
    # create counters for tracking data
    qr = 0
    x = 0
    
    # create lists to compare data, set counters to track cols/rows
    match = []
    value = list(range(0,37))
    for x in value:
        x += 1
    for row in positions_int:
        qr += 1
        match.append(row)
    
    # for loop to parse data and plot qr code
    for row in range(len(match)): 
        # second for loop, turn row into list, iterate by each value
        for x in match[row]: 
           plt.scatter(x, row, marker = "s", s = 50, color = "green")
        if qr == "":
           break
        
# write main function
def main():
    
    # call read_positions function
    positions = read_positions("positions.csv")
    
    # call float_conversion function
    positions_int = int_conversions(positions)
    
    # call qr_code function, visualize data
    plt.figure(figsize = (5,5), dpi = 500)
    plot = qr_code(positions_int)
    plt.title("Celtics-Colored Qr Code")
    plt.xlabel("Columns")
    plt.ylabel("Rows")
    plt.savefig("qr.png")
    plt.show(plot)
  
main()
    

 
