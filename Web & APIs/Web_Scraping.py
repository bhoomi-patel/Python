#  Web Scraping = Extracting data from websites automatically
#  BeautifulSoup = Python library for parsing HTML/XML
#  Parse HTML - turn messy HTML into clean, usable data 
import requests
from bs4 import BeautifulSoup 

# Get webpage content
url = "https://quotes.toscrape.com/"
res = requests.get(url)
soup = BeautifulSoup(res.content,'html.parser')

# Find elements
title = soup.find('title').text
quotes  = soup.find_all('div',class_='quote')

print(f"Page title: {title}")
print(f"Found {len(quotes)} quotes ")

# Extract quote data 
for q in quotes[:3]: # first 3 quotes
    text=q.find('span',class_='text').text
    author=q.find('small',class_='author').text
    tags = [tag.text for tag in q.find_all("a",class_='tag')]

    print(f"\n {text}")
    print(f"\n {author} ")
    print(f" Tags: {', '.join(tags)}")


html_content = """
<html>
  <body>
    <span class="author-name"><a href="https://example.com">Alice</a></span>
  </body>
</html>
"""

# BeautifulSoup css selectors
soup = BeautifulSoup(html_content, 'html.parser')

# by tag
title = soup.select('h1') # all h1 tags
header = soup.select_one('header') # first header tag
title = soup.select('div p') # all p tags inside div

quote = soup.select('.quote') # class="quote"
text = soup.select('.quote.text') #class="text" inside class="quote"

# By ID
header = soup.select('#header')      # id="header"

# By attribute
link = soup.select('a[href]') # all links with href attribute
external_link = soup.select('a[href^="http"]') # links starting with http

# Combining selectors
author_link = soup.select('span.author-name a') # specific structure

print(f"H1 tag: {title}")
print(f"link: {link}")
print(f"Author link: {author_link}")
print(f"External link: {external_link}")
print(f"Header: {header}")
print(f"Quote text: {text}")
print(f"Div p tags: {quote}")

