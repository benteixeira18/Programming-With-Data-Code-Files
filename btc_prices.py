'''

DS2001 Weekly Exercise
Benjamin Teixeira
    
Filename: btc_prices.py
    
Description: analyzing Jan 2021 BTC prices
    
'''
"""
    Helpful techniques:

    while ...:  <- execute as long as the condition is true, to repeat a few lines of codes
    if not ...: <- execute when the condition is false 
    break <- exit the loop

    random.randint(a,b+1)/randrange(a,b) <- return a random integer N such that a <= N <= b. 
    random.seed(a_number) <- if you specify a seed value before you draw the 
                             random number, it will always return the same random number
                             
    max()/min()/sum()/len()  <- return the maximum/minimum/sum/length of a list
    lst[]  <- slicing/index of a list
"""

# import libraries
import matplotlib.pyplot as plt
import random as rnd

def main():
    
    # Add up 1 to 50, report sum
    x = 0
    y = 1
    while y <= 50:
        x += y
        y += 1
        if x == 1275:
            break
    print("Sum of adding 1 to 50:", x)
    
    # Set initial BTC values
    prices_lst = []
    total_price = 0
    days = 0
    
    # Read in Bitcoin prices
    with open ("jan_2021_btc.txt", "r") as infile: 
        while True:
            Jan_Day = infile.readline()
            BTC_Price = infile.readline()
            if Jan_Day == "" and BTC_Price == "":
                break
            
            # Convert day to int, price to float
            Jan_Day = int(Jan_Day)
            BTC_Price = round(float(BTC_Price),2)
            
            # Append list to include prices
            prices_lst.append(BTC_Price)
            
            # Apply initial values
            total_price += BTC_Price
            days += 1
            
            # Report low BTC price points
            if BTC_Price < 32000:
                print("Jan", Jan_Day)
            
    # Generate the graph and plot the data points
    plt.figure(figsize = (6,5), dpi = 300)
    plt.plot(range(1,32), prices_lst,"o-", color = "gold")
    plt.grid()
    plt.xlabel("Day")
    plt.ylabel("Price")
    plt.title("January 2021 BTC Prices")
    plt.savefig("btc.png")
    
    # Report highest and lowest prices
    highest_price = max(prices_lst)
    lowest_price = min(prices_lst)
    print("Highest price: $",highest_price)
    print("Lowest price: $", lowest_price)
            
    # Calculate average price
    avg_price = round(sum(prices_lst) / len(prices_lst),2)
    print("Average price: $", avg_price)
    
    # Create a list of 10 random prices (Bonus, not covered in class)
    random_prices = [34564, 29987, 34768, 33789, 32567, 35421, 39678, 42387, 
                     28550, 41392]
    random_BTC_price = rnd.randint(0, len(random_prices))
    random_BTC = random_prices[random_BTC_price]
    print(random_BTC)
    
main()
