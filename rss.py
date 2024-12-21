import requests
from bs4 import BeautifulSoup
from feedgen.feed import FeedGenerator

# URL of the website to scrape
url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Create an RSS feed
fg = FeedGenerator()
fg.title('Custom RSS Feed')
fg.link(href=url, rel='alternate')
fg.description('An RSS feed created from a webpage')

# Extract relevant content
for item in soup.select('.article-class'):  # Replace with actual selector
    entry = fg.add_entry()
    entry.title(item.select_one('.title-class').text)  # Replace with actual selector
    entry.link(href=item.select_one('a')['href'])
    entry.description(item.select_one('.description-class').text)

# Write RSS feed to file
fg.rss_file('feed.xml')
