'''

DS2000 Spring 2022
Benjamin Teixeira
    
Filename: plot_bones.py
    
Description: comparing the number of bones days
vs. no bones days per week

Creating scatter plot
    
'''
'''
Test Case 1

    Week 1: 3 Bones Days, 2 No Bones Days
    Week 2: 4 Bones Days, 1 No Bones Days
    
Test Case 2
    Week 3: 2 Bones Days, 3 No Bones Days
    Week 4: 0 Bones Days, 5 No Bones Days
'''   
# import matplotlib and assign it as plt
import matplotlib.pyplot as plt

def main():
    
    # read bones days data from file
    filename = "november_bones.txt"
    with open (filename, "r") as infile:
        
        # read bones data from week 1
        infile.readline()
        bonesday1 = int(infile.readline())
        x_pos = 1

        # read bones data from week 2
        infile.readline()
        bonesday2 = int(infile.readline())
        x_pos2 = 2
        
        # read bones data from week 3
        infile.readline()
        bonesday3 = int(infile.readline())
        x_pos3 = 3
       
        # read bones data from week 4
        infile.readline()
        bonesday4 = int(infile.readline())
        x_pos4 = 4
       
        
    # read no bones days data from file
    filename2 = "november_nobones.txt"
    with open (filename2, "r") as infile:
        
        # read no bones data from week 1
        infile.readline()
        bonesday5 = int(infile.readline())
        x_pos5 = 1
        
        # read no bones data from week 2
        infile.readline()
        bonesday6 = int(infile.readline())
        x_pos6 = 2
        
        # read no bones data from week 3
        infile.readline()
        bonesday7 = int(infile.readline())
        x_pos7 = 3
        
        # read no bones data from week 4
        infile.readline()
        bonesday8 = int(infile.readline())
        x_pos8 = 4
        
    # Create the graph
    
    plt.figure(figsize=(6,4), dpi = 200)
    
    # Plot the bones days data points
    plt.plot(x_pos, bonesday1, "o", color = "red", label = "Bones Days")
    plt.plot(x_pos2, bonesday2, "o", color = "red")
    plt.plot(x_pos3, bonesday3, "o", color = "red")
    plt.plot(x_pos4, bonesday4, "o", color = "red")
    
    # Plot the no bones days data points
    plt.plot(x_pos5, bonesday5, "s", color = "blue", label = "No Bones Days")
    plt.plot(x_pos6, bonesday6, "s", color = "blue")
    plt.plot(x_pos7, bonesday7, "s", color = "blue")
    plt.plot(x_pos8, bonesday8, "s", color = "blue")
    
    
    # Visualize the data
    plt.grid()
    plt.xlabel("November Week Number")
    plt.ylabel("Days per Week")
    plt.title("Bones vs. No Bones Days per Week")

    plt.legend()
    plt.xlim(0,5)
    plt.ylim(0,7)
    plt.savefig("plot_bones.png")

main()  
