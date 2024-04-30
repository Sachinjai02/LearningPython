import bs4
import requests


def getAuthors(url):
    authors = set()
    try:
        result = requests.get(url)
    except:
        print('Error connecting to the url')

    else:
        if result.status_code != 404:
            soup = bs4.BeautifulSoup(result.text, 'lxml')
            quotes = soup.select('.quote')
            for quote in quotes:
                page_authors = quote.select('.author')[0].text
                authors.add(page_authors)
    print(f'Authors for page {url} are: {authors}')
    return authors


result = requests.get('http://quotes.toscrape.com')
soup = bs4.BeautifulSoup(result.text,'lxml')
print(soup)
#Get the name of authors on home page
authors = set()
quote_list = []
quotes = soup.select('.quote')
for quote in quotes:
    authors.add(quote.select('.author')[0].text)
    quote_list.append(quote.select('.text')[0].text)

print(authors)
print(quote_list)
tags = list(map(lambda tag: tag.select('a')[0].text, soup.select('.tag-item')))
print(f'top ten tags: {tags}')

base_url = 'https://quotes.toscrape.com/page/{}/'
page_num = 1
all_authors = set()
while True:
    authors = getAuthors(base_url.format(page_num))
    if len(authors) == 0:
        break
    all_authors = all_authors.union(authors)
    page_num += 1

print(all_authors)





