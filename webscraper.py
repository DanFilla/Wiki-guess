from bs4 import BeautifulSoup
import requests





url = "https://en.wikipedia.org/wiki/Special:Random"
url2 = "https://en.wikipedia.org/wiki/John_F._Cassidy"
url3 = "https://en.wikipedia.org/wiki/George_Hotz"

# print(soup.prettify())


while 1:
	try:
		req = requests.get("https://en.wikipedia.org/wiki/Special:Random").text
		soup = BeautifulSoup(req, 'lxml')
		toctitle = soup.find('div', class_='toctitle')

	except AttributeError:
		continue

	title = soup.find('h1').text
	first_paragraph = soup.find('div', id='mw-content-text').p.text


	print(title)

	for word in title.lower().split():
		first_paragraph = first_paragraph.lower().replace(word, '-'.center(len(word), '-'))



	print(first_paragraph)





