'''

DS2000 Spring 2022
Benjamin Teixeira
    
Filename: practice_week6.py
    
Description: revising practicum

Revisting 401k basics:
    
    Emily annual salary = $10,000
    Emily contribtuion = 5% ($500)
    Emily paycheck = $9,500
    Company contribution = 10% ($1,000)
    401k after 1 year = $1,500 ($500 + $1,000)

Helpful techniques: 
    
    def function_name(parameters) <- defines a function
    parameters <- variables that are inputs to the function
    return <- returns the output to the function caller
    function_name(parameter_values) <- call a function
    output = function_name(parameter_values) <- call function, store
                                                output in "output"
    split = turns data line into a list
    for loop to change data into floats 
'''
# import main libraries
import matplotlib.pyplot as plt

# write read_data function
def read_data(filename):
    """name: read_data
        input: filename (list)
        return: data (float)"""
    # read in file
    with open (filename, "r") as infile:
        data = infile.readline().split(",")
        for i in range(len(data)):
            data[i] = float(data[i])        
    return data

# write employee_contribution function
def employee_contribution(salary):
    """name: employee_contribution
        input: salary (float)
        return: employee_contribution_amount (float)"""
    return salary * 0.05

# write company_contrubtion function
def company_contribution(salary, company_contribution_percent):
    """name: company contribution
        input: salary, company percent (float)
        return: company_contribution_amount (float)"""
    return salary * company_contribution_percent

# write plot_balance function
def plot_balance(data):
    """name: plot_balance
        input: data (list)
        return: balance (float)"""
    # label values    
    salary = data[0]  
    employee = data[1]
    company = data[2]
    years = int(data[3] )
    # label annual contribution and set initial balance
    annual_contribution = salary * (employee + company)
    balance = 0
    # calculate balance over 30 years
    for i in range(years):
        balance = balance * 1.02 + annual_contribution
        # visualize the data, set x value to track years
        plt.bar(i+1, balance, color="green")
    # detail the bar graph    
    plt.title("Retirement Balance after 30 Years")
    plt.xlabel("Years")
    plt.ylabel("Balance")
    plt.savefig("week6.png")
    
    return round(balance,2)

# write withdrawl function using last_year_balance
def withdrawl(data):
    """name: withdrawl
        input: data (list)
        return: months, remainder (list)"""
    monthly_withdrawl = int(data[4])
    last_year_balance = plot_balance(data)
    months = last_year_balance // monthly_withdrawl
    remainder = last_year_balance % monthly_withdrawl
    
    return round(months), round(remainder,2)
    
# In main function, call the 401k functions

def main():

    # call function 1, storing output in data
    data = read_data("pension2.txt")
    print("401k Data:", data)
    
    # call function 2
    print("Employee Contribution: $", employee_contribution(data[0]))
    
    # call function 3
    print("Company Contribution: $", company_contribution(data[0], data[2]))
    
    # call function 4
    print("Balance after 30 Years: $", plot_balance(data))
    
    # call function 5
    print("Months to Withdraw & Remainder:", withdrawl(data))
    
main()

