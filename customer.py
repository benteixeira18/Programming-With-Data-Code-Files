'''

DS2001 Spring 2022 Weekly Exercise 12
Benjamin Teixeira
    
Filename: customer.py
    
Description: analyzing customer data with advertising info
    
'''

# define classes here
class Customer:
    
    def __init__(self, name, orders_total = 0, orders_quarter = 0,
                 recency = 100, frequency = 0, monvalue = 0):
        """Establishing constructor here"""
        
        self.name = name
        self.orders_total = orders_total
        self.orders_quarter = orders_quarter # ot/4?
        self.recency = recency
        self.frequency = frequency
        self.monvalue = monvalue
        
    def new_month(self):
        """name: new_month
            input: self, necessary variables
            result: incrementing the recency attribute by 1"""
        
        self.recency += 1
        
    def new_quarter(self):
        """name: new_quarter
            input: self, necessary variables
            result: setting frequency to equal orders_quarter,
                    resetting orders_quarter to 0"""
                    
        self.frequency = self.orders_quarter
        self.orders_quarter = 0
            
    def new_order(self, spend):
        """name: new_order
            input: self, spend, necessary variables
            result: determining new total spend, monvalue = avg spend, 
                    orders total and quarter + 1, resetting recency to 1"""
        
        new_total_spend = self.monvalue * self.orders_total + spend
        self.monvalue = new_total_spend / (self.orders_total + 1)
        
        self.orders_total += 1
        self.orders_quarter += 1
        
        self.recency = 1
            
def main():
    
    # calling objects, month 1 here
    Ben = Customer("Ben")
    Ben.new_order(32)
    
    # month 2
    Ben.new_month()
    Ben.new_order(56)
    
    # month 3
    Ben.new_month()
    Ben.new_order(45)
    Ben.new_order(28)
    
    # month 4
    Ben.new_month()
    Ben.new_quarter()
    
    # print attributes (name, orders, quarterly orders, RFM)
    print("Name: ", Ben.name)
    print("Total Orders: ", Ben.orders_total)
    print("Total Quarterly Orders: ", Ben.orders_quarter)
    print("RFM: ", Ben.recency, Ben.frequency, Ben.monvalue)
    
if __name__ == "__main__":
    main()