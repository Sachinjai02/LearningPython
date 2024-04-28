import bs4
import requests

result = requests.get("https://en.wikipedia.org/wiki/Grace_Hopper")
soup = bs4.BeautifulSoup(result.text, "lxml")
print(soup.select('.mw-headline')[0].text)

