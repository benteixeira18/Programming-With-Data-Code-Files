'''

DS2000 Spring 2022
Benjamin Teixeira
    
Filename: prices.py
    
Description: Plotting Apple's opening and closing stock prices
    
'''

# import library

import matplotlib.pyplot as plt

def main():
    
    # read jan 2022 open file
    filename = "jan_2022_open.txt"
    with open (filename, "r") as infile:
        open_1 = int(infile.readline())
        open_1_stock = float(infile.readline())
        open_2 = int(infile.readline())
        open_2_stock = float(infile.readline())
    
    # read jan 2022 close file
    filename2 = "jan_2022_close.txt"
    with open (filename2, "r") as infile:
        close_1 = int(infile.readline())
        close_1_stock = float(infile.readline())
        close_2 = int(infile.readline())
        close_2_stock = float(infile.readline())
        
    # build closing graph
    plt.figure(figsize = (6,4), dpi = 500)
    
    # determine plot point color of jan 19 close 
    if close_2_stock <= close_1_stock:
        color2 = "red"
    else:
        color2 = "green"
    
    # plot the stock prices
    plt.plot(close_1,close_1_stock,"o",color = "blue",label = "1/18 close")
    plt.plot(close_2,close_2_stock,"o",color = color2, label = "1/19 close")
    plt.legend()
    
    plt.grid()
    plt.xticks([17,18,19,20])
    plt.ylim(155,175)
    plt.xlabel("January 2022 Date")
    plt.ylabel("Stock Price [$]")
    plt.title("Apple's Closing Prices")
    plt.savefig("close.png")
    
    # build graph for opening and closing prices
    
    plt.figure(figsize = (6,4), dpi = 500)
    
    plt.plot(close_1,close_1_stock,"o",color = "blue",label = "1/18 close")
    plt.plot(close_2,close_2_stock,"o",color = "red", label = "1/19 close")
    plt.plot(open_1,open_1_stock,"o",color = "green", label = "1/18 open")
    plt.plot(open_2,open_2_stock, "o",color = "black", label = "1/19 open")
    plt.legend()
    
    plt.grid()
    plt.xticks([17,18,19,20])
    plt.ylim(155,175)
    plt.xlabel("January 2022 Date")
    plt.ylabel("Stock Price [$]")
    plt.title("Apple's Opening vs. Closing Prices")
    plt.savefig("open.close.png")
    
main()