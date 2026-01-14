from google_play_scraper import reviews
import csv
result, continuation_token = reviews(
    'com.ubercab',
    lang='en',
    country='us', 
    count=15_000_000 
)


with open("Reviews.csv",'w',newline='', encoding='utf-8') as f:
   
    writer = csv.writer(f)
    for i in result:
        writer.writerow([i['content'],i['score']])

print("Written.")