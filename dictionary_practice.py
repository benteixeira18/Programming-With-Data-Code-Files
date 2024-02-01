'''

DS2001 Weekly Exercise
Benjamin Teixeira
    
Filename: dictionary.py
    
Description: dictionaries
    
Helpful techniques:
  
Dictionary: {key:value} pairs  
        
An example: cvx_dict = {'company': 'CVX',
                        'name': 'Chevron Corporation',
                        'price': 110.24}
 
Add a key-value pair to cvx_dict
>>> cvx_dict['volume'] = 4869064
    
Access value: 
>>> print(cvx_dict['company'])
CVX
    
'''

# data for today: 
companies=['CVX','AXP','MRK','IBM','DIS']
name = ['Chevron Corporation', 'American Express', 'Merck & Co., Inc.',
        'International Business Machines Corporation', 'The Walt Disney Company']
price = [110.24,135.6,82.46,151.1,139.14]
volume = [4869064,1888892,8502056,3233147,7872913]

# Q1:    
def CreateDowJonesDict():
    """ name: CreateDowJonesDict
        input: none 
        output: djlist (a list of dicts)
    """
    djlist = []
    
    # Q1: iterate by position for each list, keys & values match
    for i in range(len(companies)):
        my_dict = {"company": companies[i], 
                   "name": name[i],
                   "price": price[i],
                   "volume": volume[i]}
    
        djlist.append(my_dict)
    
    return djlist

def main():
    # report company list
    company_list = CreateDowJonesDict()
    print(company_list)
    
    # Q2: list of company symbols & names using loop 
    for my_dict in company_list:
        print([my_dict["company"], my_dict["name"]])
        
    # Q3: Iterate over CVX dictionary to print key names in 3 ways
    cvx_dict = company_list[0]
    
    # by keys
    for onekey in cvx_dict.keys():
        print(onekey)
           
    for onekey in cvx_dict:
         print(onekey)
    
    # by items
    for onekey, onevalue in cvx_dict.items():
        print(onekey)
        
    # Q4: iterate over Chevron dictionary, print tuples in 2 ways
    cvx_dict_2 = company_list[0]
    
    # by items
    for onekey in cvx_dict_2.items():
        print(onekey)
        
    for onekey, onevalue in cvx_dict_2.items():
        print((onekey, onevalue))
        
    # Q5: iterate over Cheveron dict, print values in 4 ways
    for onekey, onevalue in cvx_dict.items():
        print(onevalue)
        
    for onevalue in cvx_dict.values():
        print(onevalue)
        
    for onekey in cvx_dict:
        print(cvx_dict[onekey])
        
    for onekey in cvx_dict:
        print(cvx_dict.get(onekey))
        
    # Q6: Sort company_list in alphabetical order on ticker
    def sort_ticker(my_dict):
        """name: sort_ticker
            input: company_list
            result: sorted in alphabetical order"""
        return my_dict["company"]
    company_list.sort(key=sort_ticker)
    print(company_list)
    
    # Q7 Sort company_list by volume in descending order
    def sort_volume(my_dict):
        """name: sort_volume
            input: company_list
            result: sorted in descending order"""
        return my_dict["volume"]
    company_list.sort(key=sort_volume, reverse = True)
    print(company_list)
         
main()
