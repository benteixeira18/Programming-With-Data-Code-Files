'''

DS2000 Spring 2022
Benjamin Teixeira
    
Filename: slugging.py
    
Description: calculating hits Devers needs to meet batting average prediction 
    
'''
'''
Test case 1
    .400 batting average
    Devers needs 236 hits to meet expected batting average
    
Test case 2
    .350 batting average
    Devers needs 207 hits to meet expected batting average
    
'''

def main():
    # user inputs 2022 batting average
    BA_2022 = float(input("Devers' predicted batting average [decimal, 3]:"))
    
    # report 2021 performance
    print("2021 stats:")
    at_bats = 591
    hits = int(89 + 37 + 1 + 38)
    total_bases = int(89 + (37*2) + (1*3) + (38*4))
    BA_2021 = round(hits / at_bats, 3)
    SLG_2021 = round(total_bases / at_bats, 3)
    
    # calculate hits needed to meet expected 2022 batting average
    hits_2022 = int(at_bats * BA_2022)
    
    # round performance to 3 decimal points
    print("At bats:", at_bats)
    print("Hits:", hits)
    print ("Total bases:", total_bases)
    print("Batting Average [BA]:", BA_2021)
    print("Slugging Percentage [SLG]:", SLG_2021)
    
    # report hits needed to meet expected 2022 batting average
    print("2022 hit goal:")
    print("Devers needs", hits_2022, "hits in 2022 for a", BA_2022, "average")
    
main()
