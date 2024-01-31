'''

DS2000 Spring 2022
Benjamin Teixeira
    
Filename: catdog.py
    
Description: prompting pet information and converting metric data to US system
    
'''
'''
# test case 1:
    20 kg = 44.0 lbs
    50.8 cm = 20 inch
    20 cel = 68 f
    
# test case 2
    9.0909 kg = 20 lb
    9.0909 kg = 20 lbs
    20 cm = 7.874 inch
    0 cel = 32 f
    
'''

def main():
    
# user inputs pet's name
    name = str(input("What's your pet's name?:"))

# user inputs pet's data
    weight = float(input("What's their weight? [kg]:"))
    length = float(input("What's their length? [cm]:")) 
    temp = float(input("What's their temperature? [cel]:"))

# convert data from metric
    weight_lbs = round(weight * 2.2, 2)
    length_inch = round(length / 2.54, 2)
    temp_f = round(temp * 9/5 + 32, 2)

# round conversions to 2 decimal places
    print("Here is", name,"'s data converted from metric:")
    print("Dog's weight [lbs]:", weight_lbs)
    print("Dog's length [inch]:", length_inch)
    print("Dog's temp [f]:", temp_f)
    
main()
