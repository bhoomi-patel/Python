import requests
from bs4 import BeautifulSoup

def scrape_news_headlines(url):
    """Scrape news headlines from a website."""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise error for bad responses

        soup = BeautifulSoup(response.content, 'html.parser')
        headlines_selectors = ['h1', 'h2', 'h3', '.headline', '.title', '.story-title', '[data-testid="headline"]']
        headlines = []

        for selector in headlines_selectors:
            elements = soup.select(selector)
            for element in elements[:10]:
                text = element.get_text(strip=True)
                if text and len(text) > 10:
                    headlines.append(text)

        return list(set(headlines))  # remove duplicates

    except Exception as e:
        print(f" Error scraping {url}: {e}")
        return []

# Example usage
news_headlines = scrape_news_headlines("https://www.bbc.com/news")
print("\n Sample Headlines:")
for h in news_headlines[:10]:
    print("-", h)

# multiple sources 
urls = [
    "https://www.bbc.com/news",
    "https://www.reuters.com/",
    "https://www.ndtv.com/latest",
    "https://www.theguardian.com/international"
]

for site in urls:
    print(f"\n Headlines from {site}")
    headlines = scrape_news_headlines(site)
    for h in headlines[:5]:
        print(" -", h)