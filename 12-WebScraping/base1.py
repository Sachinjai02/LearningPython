import requests
import bs4

example_url = "http://www.example.com"
results = requests.get(example_url)

print(type(results))
print(results.text)

soup = bs4.BeautifulSoup(results.text, "lxml")
print(soup)

print(soup.select('title')[0].getText())
print(soup.select('h1')[0])

site_paras_soup_obj = soup.select('p')
print(type(site_paras_soup_obj))
print(type(site_paras_soup_obj[0]))
site_paras_map = map(lambda obj: obj.getText(), site_paras_soup_obj)
print(list(site_paras_map))