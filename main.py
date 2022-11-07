from bs4 import BeautifulSoup
import requests

url = 'https://coinmarketcap.com/'
result = requests.get(url).text
doc = BeautifulSoup(result, 'html.parser')

# Tree Structure
tbody = doc.tbody
trs = tbody.contents

# Tree Siblings traversing on same level
# print(list(trs[0].next_siblings))

# Tree Parents and Descendants
# print(list(trs[0].descendants))
# print(list(trs[0].contents))
# print(list(trs[0].))

# Getting Crypto Prices
prices = {}

# This script finds the price of the first 10 cryptocurrencies on coinmarketcap.com.
for tr in trs[:10]:
    name, price = tr.contents[2:4]
    fixed_name = name.p.string
    fixed_price = price.a.string

# This line of code prints name with corresponding price.
    prices[fixed_name] = fixed_price

print(prices)


