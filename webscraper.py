from bs4 import BeautifulSoup
import requests
import string



para = 1
while 1:
	# Filter through wiki pages until we find an artical with a contents page.
	try:
		req = requests.get("https://en.wikipedia.org/wiki/Special:Random").text
		soup = BeautifulSoup(req, 'lxml')
		toctitle = soup.find('div', class_='toctitle').text
	except AttributeError:
		continue

	# Display the first paragraph to the user with all of the answers 
	# replaced by '-'
	answer = soup.find('h1').text
	answer_list = answer.lower().split()
	first_paragraph = soup.find('div', id='mw-content-text').p.text

	# Make sure all letters in the title are in the english alphabet
	for letter in answer:
		if letter not in string.ascii_lowercase or letter not in string.punctuation:
			continue

	# Make sure that the first_paragraph is not empty.
	if first_paragraph.strip() and len(answer_list) <= 3:

		for word in answer_list:
			if len(word) == 1:
				continue
			first_paragraph = first_paragraph.lower().replace(word, '-'.center(len(word), '-'))

		print(first_paragraph)

		# Loop for each wiki page the user can guess on.
		while 1:
			user_input = input('What is your guess?...').lower()
			if user_input == 'next':
				print('The answer was ' + answer)
				continue
			elif user_input == answer.lower():
				print('You got it correct!')
				break
			elif user_input in answer_list:
				print("Alright close enough, I'll give it to you...")
				print('The actuall answer is ' + answer)
				break
			else:
				continue
	else:
		continue




























