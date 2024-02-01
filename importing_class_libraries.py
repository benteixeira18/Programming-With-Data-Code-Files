'''

DS2000 Spring 2022 Homework 7
Benjamin Teixeira 4/8/22
    
Filename: importing_class_libraries.py
    
Description: importing and implementing race from Ant class in ant.py
    
'''
# importing Ant class and libraries here
from ant import Ant
import matplotlib.pyplot as plt
import random as rnd
import time

def plot():
    """name: plot
        input: matplotlib labels and dimensions
        result: initial and continuous snapshots of race"""
    
    # creating graph
    plt.figure(figsize = (5,5), dpi = 500)
    plt.grid()
    plt.xlim(0,150)
    plt.ylim(0,150)
         
    # labeling race track and starting line
    plt.xticks([0,30,60,90,120,150],
                ["Start", "20%", "40%", "60%", "80%", "Finish"])
    plt.yticks([0,30,60,90,120,150], 
                    ["→","→","→","→","→","→"])
         
    plt.title("DS2000 Ant Race")
    plt.xlabel("Race Track")
    plt.ylabel("Starting Line")

def main():
    
    # creating eight Ant objects to race against each other
    bill = Ant("Bill", y = rnd.randint(5,15))
    larry = Ant("Larry", y = rnd.randint(25,35), color = "Orange")
    paul = Ant("Paul", y = rnd.randint(45,55), color = "Red")
    kevin = Ant("Kevin", y = rnd.randint(65,75), color = "Grey")
    rajon = Ant("Rajon", y = rnd.randint(85,95), color = "Turquoise")
    isaiah = Ant("Isaiah", y = rnd.randint(105,115), color = "Blue")
    jaylen = Ant("Jaylen", y = rnd.randint(125,135), color = "Pink")
    jayson = Ant("Jayson", y = rnd.randint(145,149), color = "Black")
    
    # plotting race track, drawing and showing ants at starting line
    plot()
    
    ant_lst = [bill, larry, paul, kevin, rajon, isaiah, jaylen, jayson]
    for ants in ant_lst:
        ants.draw() 
        
    plt.show()
    
    # announcing the start of the race
    print("Starting race in 3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("False start! Go!")
    
    # replotting race track for continuous snapshots, establishing edge
    width = 150
    while ants.x < width:
        plot()
        
        # starting the race by moving the ants with delays for snapshots
        for ants in ant_lst:
            ants.move(rnd.randint(1,10), width = width)
            ants.draw() 
            time.sleep(.0001)
        
        plt.show()
        
        # establishing finish line, ending the race
        for ants in ant_lst:
            if ants.x >= width:
                break
            
    # announcing conclusion and winner of the race
    print(ants.at_edge(width = width)) 
    print(ants)
    
main()
