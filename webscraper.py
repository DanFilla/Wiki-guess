from bs4 import BeautifulSoup
import requests

def get_next_paragraph(count):
	#toclevel-1 tocsection-'count'
	next_paragraph_title = toctitle.find('li', class_='toclevel-1 tocsection-' + str(count)).text[2:]




points = 1
while 1:
	# Filter through wiki pages until we find an artical with a contents page.
	try:
		req = requests.get("https://en.wikipedia.org/wiki/Special:Random").text
		soup = BeautifulSoup(req, 'lxml')
		toctitle = soup.find('div', class_='toctitle')
	except AttributeError:
		continue

	# Display the first paragraph to the user with all of the answers 
	# replaced by '-'
	answer = soup.find('h1').text
	answer_list = answer.lower().split()
	print(answer)
	first_paragraph = soup.find('div', id='mw-content-text').p.text

	# Make sure that the first_paragraph is not empty.
	if first_paragraph.strip() and len(answer_list) <= 3:

		for word in answer_list:
			first_paragraph = first_paragraph.lower().replace(word, '-'.center(len(word), '-'))

		print(first_paragraph)

		# Loop for each wiki page the user can guess on.
		while 1:
			user_input = input('What is your guess?...').lower()
			if user_input == 'next':
				points += 1
				print('The correct answer is ' + answer)
				print('You have ' + str(points) + ' points.')
				continue
			elif user_input == answer.lower():
				points -= 10
				print('You got it correct!')
				print('Your score is ' + str(points))
				break
			elif user_input in answer_list:
				print("Alright close enough, I'll give it to you...")
				print('The actuall answer is ' + answer)
				print('Your score is ' + str(points))
				break
			else:
				continue
	else:
		continue




























