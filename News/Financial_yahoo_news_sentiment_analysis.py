import feedparser

from transformers import pipeline


pipe = pipeline("text-classification", model="prosusAI/finbert")

ticker_symbol = 'GC=F'
keyword = 'gold'

rss_url = f'https://finance.yahoo.com/rss/2.0/headline?s={ticker_symbol}'
feed = feedparser.parse(rss_url)

total_score = 0
num_articles = 0

for i, entry in enumerate(feed.entries):
  if keyword.lower() not in entry.summary.lower():
    continue

  print(f"Title: {entry.title}")
  print(f"Link: {entry.link}")
  print(f"Published: {entry.published}")
  print(f"Summary: {entry.summary}")


  sentiment = pipe(entry.summary)[0]
  
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