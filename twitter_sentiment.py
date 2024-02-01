'''

DS2001 Spring 2022 Weekly Exercise
Benjamin Teixeira
    
Filename: twitter_sentiment.py
    
Description: sentiment analysis of twitter users

next(reader) skips header
    
'''

# import libraries here
import csv

# write functions here
def read_data(filename):
    """name: read_data
        input: twitter.csv
        result: list of tweets,
        header separated"""
    
    # reading in data, appending to list
    twitter_data = []

    with open (filename, encoding="utf8") as file:
        data = csv.reader(file, delimiter = ",")
        for row in data:
            twitter_data.append(row)
    
        # separating header
        header = twitter_data[0]
        full_data = twitter_data[1:]
    
    return header, full_data
        
def read_txt(filename):
    """name: read_txt
        input: filename (string)
        result: words (a list of strings)"""
    
    words = []
    
    # reading in, cleaning positive/negative words
    with open(filename, "r") as file:
        while True:
            line = file.readline()
            if not line:
                break
            words.append(line.strip())
            
    return words

def calc_sentiment_score(header, data, positive_words, negative_words):
    """name: calc_sentiment_score
        input: header, data, positive and negative words
        result: sentiment score of each tweet between -1 and 1"""
        
    # getting text section from index
    text_index = header.index("text")
    header.append("sentiment_score")
    
    # separating text row, converting to lowercase, splitting into list
    for row in data:
        tweet = row[text_index].lower().split()
        
        # list comprehension to clean data, remove @
        tweet = [word for word in tweet if word[0] != "@"]
        
        # calculating sentiment score
        score = 0
        for word in tweet:
            if word in negative_words:
                score -= 1
            elif word in positive_words:
                score += 1
                
        row.append(score/len(tweet))
        
    return header, data

def calc_avg_score(date, header, data):
    """name: calc_avg_score
        input: date (string), header (list), data (list of lists)
        result: average sentiment score across twitter.csv tweets"""
        
    # finding sentiment_score and created_at columns
    score_index = header.index("sentiment_score")
    date_index = header.index("created_at")
    
    scores = []
    
    # if statement finding date/score in index 
    for row in data:
        if date in row[date_index]:
            scores.append(row[score_index])
    
    # calculate, returning average
    avg = sum(scores)/len(scores)
    
    return avg

def main():
    
    # call read_data function
    header, data = read_data("twitter.csv")
    
    # call read_txt function
    # changed .txt name, using practicum file names in different files for hw
    positive = read_txt("positive.txt")
    negative = read_txt("negative.txt")
    
    # call calc_sentiment_score function
    header, data = calc_sentiment_score(header, data, positive, negative)
    
    # call calc_avg_score function
    average_score = calc_avg_score("2/29/20", header, data)
    print("Average twitter.csv Sentiment Score:", round(average_score, 7))

main()
