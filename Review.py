import requests
from bs4 import BeautifulSoup
import os
import csv
import re

comments = []
os.system('cls')

def getLinks():
    response = requests.get("https://www.reddit.com/r/uber/.rss") 

    soup = BeautifulSoup(response.content, 'xml')
    
    links = [i.get_text() for i in soup.find_all('content')]

    x = 1
    total =  len(links)
    for i in links:
        match = re.search(r'https://www\.reddit\.com/r/uber/comments/[A-Za-z0-9_]+/[^"]*', i)
        if match:
            getcomments(f"{match.group(0)}/.rss")
            print(f"{x} of {total} : {match.group(0)}")
        x+=1

def getcomments(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'xml')
    comments_post = [i.get_text() for i in soup.find_all('content')][1:]
    for i in comments_post:
        comments.append(i.split("<p>")[1].split("</p>")[0])


getLinks()
with open("RedditReviews.csv",'w',newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for i in comments:
        writer.writerow([i])