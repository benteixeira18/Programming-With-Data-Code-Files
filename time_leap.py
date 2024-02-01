'''

DS2000 Spring 2022
Benjamin Teixeira
    
Filename: time_leap.py
    
Description: calculating time leap length
    
'''

'''
Test case 1
    Currently: Day 0 Hour 5
    Time leap: 20 hours
    It will be: Day 1 Hour 1
    
Test case 2

    Currently: Day 0 Hour 18
    Time leap: 18 hours
    It will be: Day 1 Hour 12
    
'''
def main():
    
    # report weekday number alignment
    print("Day 0 = Sunday, Day 1 = Monday... Day 6 = Saturday")
    
    # input weekday and hour of day
    current_day = (0)
    current_hour = (0)
    
    # report current weekday and hour of day
    print("It is currently Day", current_day, "Hour", current_hour)

    # user inputs length of time leap in hours
    leap = int(input("How long will the time leap be? [hrs]:"))

    # calculate hours left over
    hour = ((current_hour + leap) % 24)
    
    # calculate and report sum of days
    sum_days = (leap // 24)
    print("Sum of Days:", sum_days)

    # calculate weekday
    weekday = int(sum_days / 7)
    leap_day = (sum_days - (7*weekday))
    day = (leap_day + current_day)
   
    # report weekday, hour of day
    print("Time traveler will leap into") 
    print("Day:", day)
    print("Hour of Day:", hour)
    
main()
