import bs4
import requests

number_pages = 50
base_url = 'https://books.toscrape.com/catalogue/page-{}.html'

for n in range(1, number_pages+1):
    result = requests.get(base_url.format(n))
    soup = bs4.BeautifulSoup(result.text, 'lxml')
    print(f'printing results from {n} page')
    products = soup.select('.product_pod')
    for prod in products:
        twoStarBook = prod.select(".star-rating.Two")
        if twoStarBook:
            title = prod.select('h3 a')[0]['title']
            print(f"Title of two star book is: {title}")