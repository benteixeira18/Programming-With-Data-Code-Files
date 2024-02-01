'''

DS2001 Weekly Exercise 2
Benjamin Teixeira
    
Filename: pension_amount.py
    
Description: calculating pension amount
    
'''

def main():
    
    #Q1: user inputs their salary
    salaryQ1 = int(input("What is your annual salary? [$]:"))
    
    # calculate and display amount needed (5%) to contribute to pension
    pensionQ1 = (salaryQ1 * .05)
    print("You must contribute $",pensionQ1, "annually to your pension")
    
    #Q2: user inputs salary
    salaryQ2 = int(input("What is your annual salary? [$]:"))
    
    # calculate and display personal (5%) and company (10%) contribution
    pensionQ2 = (salaryQ2 * .05)
    companyQ2 = (pensionQ2 * 2)
    print("You must contribute $",pensionQ2, "annually to your pension")
    print("Your company will contribute $",companyQ2, "annually")
    
    #Q3: user inputs salary and company contribution percentage
    salaryQ3 = int(input("What is your annual salary? [$]:"))
    companyQ3 = float(input("What percent will your company add? [dec.]:"))
    
    # calculate and display users company contribution
    amountQ3 = (salaryQ3 * companyQ3)
    print("Your company will contribute $",amountQ3, "annually")
    
    #Q4: prompt pension.txt,
    pensiontxt = input("Input 'pension' to see pension.tx contribution info:")
    filename = (pensiontxt + ".txt")
    with open (filename, "r") as infile:
        personQ4 = infile.readline()
        salaryQ4 = int(infile.readline())
        pension = float(infile.readline())
        company = float(infile.readline())
    # calculate and display sum of employee and company pension contribution
    pensionQ4 = (pension * salaryQ4)
    companyQ4 = (company * salaryQ4)
    totalQ4 = (pensionQ4 + companyQ4)
    print("Name of person holding pension:",personQ4)
    print("Salary: $",salaryQ4)
    print("Personal contribution: $",pensionQ4)
    print("Company contribution: $",companyQ4)
    print("Total contribution: $",totalQ4)
    
    #Q5: using pension.txt, calculate 3-year account totals (Interest = 2%)
    year2 = ((totalQ4 * 1.02) + totalQ4)
    year3 = round(((year2 * 1.02) + totalQ4), 2)
    
    # display 3-year pension amount 
    print("In 3 years, Emily's pension account will have $",year3)
    
    #Q6: calculate months allowed to draw $200/month after Q5 (0 interest)
    months = (year3 // 200)
    balance = round((year3 - (months * 200)),1)
    
    # report how many months Emily can draw $200/month
    print("She can withdraw $200 from her pension for", months, "months")
    print("Her balance will be approximately $", balance)
       
main()


