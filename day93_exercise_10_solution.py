
import requests
query=input("what type of news are you interested in?")

url=f"https://newsapi.org/v2/everything?q={query}&from=2026-05-26&to=2026-05-26&sortBy=popularity&apiKey=7a7a600f8f4f42af995bcbd7d69c71ab"
r=requests.get(url)
print(r.text)

news=(r.text)
print(news,type(news))