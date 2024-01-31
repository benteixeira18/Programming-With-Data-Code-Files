'''

DS2000 Spring 2022
Benjamin Teixeira
    
Filename: sentiment_2.py
    
Description: gathering, analyzing & visualizing NEU COVID reddit sentiment
    
'''
# importing libraries 
import matplotlib.pyplot as plt

def class_words(filename):
    """name: class_words
        input: pos + neg text files
        return: positive and negative word list, stripped blank characters"""
    
    with open(filename, "r") as file:
        line = file.readlines()        
    
    return [row.strip() for row in line]

def read_reddit(filename):
    """name: read_reddit
        input: reddit.txt
        return: list lowercase, reversed, remove characters and whitespace"""
    
    comments = []
    punc = ".,9876543210()*&^%$#@!_+-=';:></?\""
    
    with open(filename, "r") as infile:
        while True:
            infile.readline()
            infile.readline()
            infile.readline()
            infile.readline()
            reddit = infile.readline()
            infile.readline()
            
            if not reddit:
                break
            
            # lowercase conversion, removing punctuation, numbers, white-space
            lowercase = reddit.lower()
            for cha in punc:
                low = lowercase.replace(cha, "")    
            l = low.replace("/n", "").replace("/t", "").replace("  ", "")
            
            # splitting list, appending reddit comments
            l_split = l.split()
            comments.append(l_split)
    
    return comments

def total_sentiment(list_of_lists, positive, negative):
    """name: total_attitude
        input: read_reddit comments & class_words +/- lists
        result: lists of lists, positive, neutral, negative COVID sentiment"""
    
    list_of_sentiment = []
    for words in list_of_lists:
        sentiment = []
        
        # filtering reddit words in comments based on sentiment
        for word in words: 
            if word in positive:
                sentiment.append(1)
            elif word in negative:
                sentiment.append(-1)
            else:
                sentiment.append(0)
        
        # list of lists to plot by comment
        list_of_sentiment.append(sentiment)
                     
    return list_of_sentiment

def plot_sentiment(sentiment):
    """name: plot_sentiment
        input: sentiment (list of lists)
        result: visualized neu reddit data labeled by 
        positive, negative and neutral covid sentiment"""

    # gathering sentiment count and scores per comment in NEU reddit
    score_lst = []
    for lst in sentiment:
        lst_score = 0
        
        # storing average in list to gather total sentiment scores
        lst_score += lst.count(1)
        lst_score -= lst.count(-1)
        avg = lst_score/len(lst)
        score_lst.append(avg)
        
    # calculating and analyzing overall reddit sentiment average
    average = sum(score_lst)/len(score_lst)
    print(round(average,4), "average NEU COVID Reddit sentiment score")
    
    if average > 0:
        print("Average NEU COVID Reddit sentiment has been positive")
    elif average == 0:
        print("Average NEU COVID Reddit sentiment has been neutral")
    else:
        print("Average NEU COVID Reddit sentiment has been negative")
         
    # setting counters for labeling
    plt.figure(figsize = (6,5), dpi = 250)
    score_lst.reverse()
    pos_label = 0
    neg_label = 0
    neu_label = 0
    
    # plotting and labeling data points based on sentiment score
    for i in range(len(score_lst)):
        if score_lst[i] > 0:
            if pos_label == 0:
                plt.scatter(i, score_lst[i], label = "pos", color = "green")
                pos_label += 1
            else:
                plt.scatter(i, score_lst[i], color = "green")
        elif score_lst[i] < 0:
            if neg_label == 0:
                plt.scatter(i, score_lst[i], label = "neg", color = "red")
                neg_label += 1
            else:
                plt.scatter(i, score_lst[i], color = "red")
        else:
            if neu_label == 0:
                plt.scatter(i, score_lst[i], label = "neu", color = "black")
                neu_label += 1
            else:
                plt.scatter(i, score_lst[i], color = "black")
            
    # labeling the visualization
    plt.legend()
    plt.title("NEU COVID-19 Reddit Word Count Sentiment")
    plt.xlabel("Recency of Post, Old to New")
    plt.ylabel("Average Sentiment Score per Post")
    plt.savefig("sentiment.png")
    
def main():
    
    # calling class_words function
    positive = class_words("positive-words.txt")
    negative = class_words("negative-words.txt")
    
    # calling read_reddit, total_sentiment, and plot_sentiment functions
    data = read_reddit("reddit.txt")
    reddit_sentiment = total_sentiment(data, positive, negative)
    plot_sentiment(reddit_sentiment)
    
main()


         
