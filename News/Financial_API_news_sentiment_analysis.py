import requests, os
from dotenv import load_dotenv

from transformers import pipeline
load_dotenv()
pipe = pipeline("text-classification", model="prosusAI/finbert")   #Model:- https://huggingface.co/ProsusAI/finbert

API_KEY = os.getenv('NEWS_API')

keyword = 'gold'
date = '2024-08-27'

url = (
    'https://newsapi.org/v2/everything?'
    f'q={keyword}&'
    f'from={date}&'
    'language=en&'
    'sortBy=popularity&'
    f'apiKey={API_KEY}'
)

response = requests.get(url)
articles = response.json()['articles']
articles = [article for article in articles if keyword.lower() in article['title'].lower() or keyword.lower() in article['description'].lower()]

total_score = 0
num_articles = 0

for i, article in enumerate(articles):
  print(f"Title: {article['title']}")
  print(f"Link: {article['url']}")
  print(f"Description: {article['description']}")


  sentiment = pipe(article['content'])[0]
  
  print(f"Sentiment: {sentiment['label']}")
  print(f"Score: {sentiment['score']}")
  print('-'*120)

  if sentiment['label']=='positive':
    total_score+=sentiment['score']
    num_articles+=1
  elif sentiment['label']=='negative':
    total_score-=sentiment['score']
    num_articles+=1

final_score = total_score/num_articles

print(f"Overal sentiment: {'positive' if final_score >= 0.15 else 'negative' if final_score <= -0.15 else 'neutral'} {final_score}")