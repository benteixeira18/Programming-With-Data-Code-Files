'''

DS2000 Spring 2022
Benjamin Teixeira
    
Filename: gadgets.py
     
Description: determining how a gadget seller selects his 
most optimal conusmer target market 
    
'''

def main():
    
    # prompt the customer to input their age and salary
    
    age = int(input("How old are you? [yrs]:"))
    salary = int(input("What is your annual salary? [$]:"))
    
    # fiter consumer selling chance based on inouts
    if age >= 70:
        print("Not a target customer")
    elif salary < 40000:
        print("Not a target customer")
    else:
        print("Bingo! Go to www.buygadget.com to learn more!")
        
    # filter on new age and salary limits
    
    age2 = int(input("Please repeat your age again [yrs]:"))
    salary2 = int(input("Please input your annual salary again [$]:"))
    
    if age2 >= 40 and salary2 >= 30000:
        print("Bingo! Go to www.buygadget.com to learn more!")
    elif age2 >= 40 and salary2 <= 30000:
        print("Not a target customer")
    elif age2 <= 40 and salary2 >= 20000:
        print("Bingo! Go to www.buygadget.com to learn more!")
    else:
        print("Not a target customer")
        
main()
