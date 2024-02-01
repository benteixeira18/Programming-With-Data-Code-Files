'''

DS2000 Spring 2022
Benjamin Teixeira
    
Filename: mbta_report.py
    
Description: reporting information of mbta patterns overtime
    
'''

# importing libraries
import csv
import matplotlib.pyplot as plt

# labeling constants and filename
MBTA_FILE = "mbta_data.csv"
LINE_COL = 3
TOTAL_ON = 12
TOTAL_OFF = 13
TIME_OF_DAY = 8

############################################################
#
# For HW5 -- fill in the functions below!
#
############################################################

def read_file(filename):
    ''' Function: read_file
        Parameters: filename (string) for a CSV file
        Returns: 2d list of what the file contains, w/o the header
    '''
    # creating all_data list from reading in file, seperate header
    all_data = []
    with open (filename, "r") as infile:
        csv_file = csv.reader(infile, delimiter = ",")
        next(csv_file)
        
        # appending data in csv_file to mbta_data list
        for row in csv_file:
            all_data.append(row)
            
    return all_data
    
def get_col(data, col):
    ''' Function: get_col
        Parameters 2d list of anything, a column number (int)
        Returns: one column of the 2d list, turned into a list of its own
    '''
    # col_lst for line & time functions
    col_lst = []
    for row in data:
        col_lst.append(row[col])
        
    return col_lst

def riders_per_line(all_data, line, line_col, on_col):
    ''' Function: riders_per_line
        Parameters: 2d list of strings (original data from csv), the line to 
                    look for (a string), the column number where the line is,
                    and column number where the # of riders getting on is
        Returns: the average number of riders on that line
    '''       
    # counting total_ons and number of trains
    trains = 0
    total_on = 0
    for row in all_data:
        if line == row[line_col]:
            total_on += float(row[on_col])
            trains += 1
    
    # calculating and reporting average
    average = total_on/trains
        
    return average

def split_by_time(all_data, time, timecol):
    ''' Function: split_by_time
        Parameters: 2d list of strings (original data from csv),
                    time we care about (string), and column where the time is
        Returns: New 2d list that contains the data just for that time
    '''
    # time list to append time_col data
    time_lst = []
    for row in all_data:
        if time == row[timecol]:
            time_lst.append(row)
        
    return time_lst

############################################################
#
# Don't modify the code below here! 
# You should definitely read it though :)
# 
# It'll call the functions you wrote, and print out 
# some info about the T, and make a couple of plots
#
############################################################

def plot_ridership(ridership, lines):
    ''' Function: plot_ridership
        Parameters: one list of ints: t-riders getting on,
                    one list of strings: the lines we care about
        Returns: nothing, just generates a plot
    '''
    pos = [i for i in range(len(lines))]    
    plt.bar(pos, ridership, color = lines)
    plt.title("MBTA average ridership")
    plt.xticks(pos, lines)


def plot_time_ridership(ridership_by_time, lines):
    ''' Function: plot_time_ridership
        Parameters: 2d list of floats; each sublist is the ridership of
                    all 4 lines at a certain time of day
                    [[greenam, blue-am, red-am, orange-am], [green-pm,...]]
                    plus
        Returns: nothing, just creates a plot
    '''
    for i in range(len(lines)):
        curr_line = get_col(ridership_by_time, i)
        plt.plot(curr_line, color = lines[i])
    plt.title("Ridership on all lines over the day")
    plt.xticks([i for i in range(0, len(ridership_by_time), 3)],
               ["Early morning", "Midday", "PM Peak", "Night"])
    

def main():
    # Step One: Gathering data
    # Get the data as a 2d list of ints
    data = read_file(MBTA_FILE)

    # Step Two: Computations 
    # Compute the average number of riders getting on each line
    lines = ["Green", "Blue", "Red", "Orange"]
    ridership = []
    for i in range(len(lines)):
        on_riders = riders_per_line(data, lines[i], LINE_COL, TOTAL_ON)
        ridership.append(on_riders)
    
    # Step Two: Computations
    # Count the average number of total riders at each time of day
    # We can reuse the ridership functions above, but first we
    # split the data into each separate part of day
    ridership_time = []
    for i in range(1, 12):
        time_period = "time_period_{:02d}".format(i)
        time_data = split_by_time(data, time_period, TIME_OF_DAY)
        curr_riders = []
        for j in range(len(lines)):
            riders = riders_per_line(time_data, lines[j], LINE_COL, TOTAL_ON)
            curr_riders.append(riders)
        ridership_time.append(curr_riders)
        
        
    # Step Three: Communicate! 
    # Plot the average number of riders getting on each line
    print("Average ridership per line:")
    for i in range(len(lines)):
        print("\t", lines[i], ": ", round(ridership[i]), " avg riders.",
              sep = "")
    plot_ridership(ridership, lines)
    plt.show()
    
    # Step Three: Communicate
    # Plot each line's ridership over the day as a line chart
    plot_time_ridership(ridership_time, lines)
    
main()  
