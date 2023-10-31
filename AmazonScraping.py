import requests
from bs4 import BeautifulSoup
import pandas as pd

data = {'Title': [], 'Price': [], 'Stars': [], 'Reviews': []}

url = "https://www.amazon.in/s?k=iphone&crid=3E73E9TSI4LTL&sprefix=iphone%2Caps%2C188&ref=nb_sb_noss_1"

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.text, 'html.parser')

spans = soup.select("span.a-size-medium.a-color-base.a-text-normal")
prices = soup.select("span.a-price")
offers = soup.select('span.a-color-base.a-text-bold')
stars = soup.select('a.a-popover-trigger.a-declarative')
reviews = soup.select("span.a-size-base.s-underline-text")

print(len(offers))

for span in spans:
    print(span.string)
    data['Title'].append(span.string)

for price in prices:
    if (len(price.get("class")) == 1):
        print(price.find("span").get_text())
        data['Price'].append(price.find("span").get_text())

for offer in offers:
    if (offer.get("class") == ['a-color-base', 'a-text-bold']):
        print(offer.string)
        # data['Offer'].append(offer.string)

for star in stars:
    if (star.get("class") == ['a-popover-trigger', 'a-declarative']):
        print(star.find("span").get_text())
        data['Stars'].append(star.find("span").get_text())

for review in reviews:
    print(review.string)
    data['Reviews'].append(review.string)

df = pd.DataFrame.from_dict(data)
df.to_csv("data.csv", index=False)
df.head()
