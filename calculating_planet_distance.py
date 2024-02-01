'''

DS2000 Spring 2022
Benjamin Teixeira
    
Filename: calculating_planet_distance.py
    
Description: Calculating the distance between the sun and 
2 given planet using the Euclidean Distance method

Not to scale, creating scatterplot
    
'''
'''
Test Case 1
    Sun to Venus (Euclidean): 231.138
    Sun to Earth (Euclidean): 493.138
    Avg. Distance from Sun: 362.138
        
Test Case 2
    Sun to Pluto (Euclidean): 972.594
    Sun to Mercury (Euclidean): 113.111
    Avg. Distance from Sun: 542.853
'''
# import matplotlib as plt
import matplotlib.pyplot as plt

def main():
    # Label the sun's info as constants
    x_s = 100
    y_s = -100
    msize_s = 20
    color_s = "yellow"
    
    # Prompt the user to input planet 1 and read the file
    p1 = str(input("Enter venus, mercury, earth, or pluto:"))
    filename = p1 + ".txt"
    with open (filename, "r") as infile:
        x_p1 = int(infile.readline())
        y_p1 = int(infile.readline())
        msize_p1 = int(infile.readline())
        color_p1 = str(infile.readline()).strip()
        
    # Prompt the user to input planet 2 and read the file
    p2 = str(input("Enter again without a repeat planet:"))
    filename2 = p2 + ".txt"
    with open (filename2, "r") as infile:
        x_p2 = int(infile.readline())
        y_p2 = int(infile.readline())
        msize_p2 = int(infile.readline())
        color_p2 = str(infile.readline()).strip()
    
    # Calculate & report the distance from planet 1 & the sun
    x_distance1 = ((x_p1 - x_s) ** 2)
    y_distance1 = ((y_p1 - y_s) ** 2)
    squared_distance1 = x_distance1 + y_distance1
    distance1 = round(squared_distance1 ** .5, 3)
    print("Distance from the Sun to planet 1:", distance1)
    
    # Calculate & report the distance from planet 2 & the sun
    x_distance2 = ((x_p2 - x_s) ** 2)
    y_distance2 = ((y_p2 - y_s) ** 2)
    squared_distance2 = x_distance2 + y_distance2
    distance2 = round(squared_distance2 ** .5, 3)
    print("Distance from the Sun to planet 2:", distance2)
    
    # Calculate & report the average distance of the 2 planets
    avg_distance = round((distance1 + distance2) / 2, 3)
    print("Average distance from the sun:", avg_distance)
    
    # Build the graph
    plt.figure(figsize =(8,6), dpi = 250)
    
    # Plot the data points
    plt.plot(x_s, y_s, "o", color = color_s, markersize = msize_s, label="Sun")
    plt.plot(x_p1, y_p1, "o", color = color_p1, markersize = msize_p1, label=p1)
    plt.plot(x_p2, y_p2, "o", color = color_p2, markersize = msize_p2, label=p2)
    
    plt.grid()
    plt.xlabel("Planet location")
    plt.ylabel("Planet height")
    plt.title("The DS2000 Solar System")
    
    plt.xlim(-200, 300)
    plt.ylim(-200, 900)
    plt.legend()
    plt.savefig("planet.png")
    
main()
