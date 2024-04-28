import requests
import bs4

result = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
soup = bs4.BeautifulSoup(result.text,"lxml")
# print(soup)

images = soup.select('a>img')
for image in images:
    print(image)

image = soup.select('.mw-file-element')[1]


image_link = requests.get('https:' + image['src'])
print(image_link.content) # binary contents

f = open('my_computer.jpg', 'wb')
f.write(image_link.content)
f.close()

