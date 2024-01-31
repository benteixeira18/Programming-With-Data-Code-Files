'''

DS2000 Spring 2022 Homework 7
Benjamin Teixeira 4/8/22
    
Filename: ant.py
    
Description: defining ant class as baseline for ant racing
    
'''
# importing libraries
import matplotlib.pyplot as plt

class Ant:
    
    def __init__(self, name, x = 0, y = 0, color = "green"):
        """Establishing constructor for Ant class"""
        
        self.name = name
        self.x = x
        self.y = y
        self.color = color
    
    def draw(self):
        """name: draw
            input: Ant class
            result: visualized data points at current position"""
        
        plt.plot(self.x, self.y, marker = "4", 
                  markersize = 10, color = self.color)
        plt.text(self.x+.2, self.y+.8, self.name)
        
    def move(self, fwd, width):
        """name: move
            input: drawn objects, fwd, width
            result: moving the ant along x-axis towards the edge (width),
                    setting x >= width to avoid ants crossing over axis"""
        
        self.x += fwd
        self.width = width
        if self.x >= width:
            self.x = width
            
    def at_edge(self, width):
        """name: at_edge
            input: moved objects, self, width
            result: returning indication of an ant winning the race"""
        
        self.width = width
        if (self.x >= width) is True:
            return "The race is over!"
    
    def __str__(self):
        """name: __str__
            input: self
            result: the string used when calling print(__str__),
            in this case to announce the winner of the race"""
        
        return self.name + " won! Want to try again?"
        
        
        
        
        
    