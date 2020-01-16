from bs4 import BeautifulSoup
import requests

def display_points(points, tokens):
	'''display the points and tokens to the user'''
	print('You have ' + str(points) + ' points and ' + str(tokens) + ' tokens.')


points = 30
tokens = 0
while points > 0:
	if not exit:
		break
	# Filter through wiki pages until we find an artical with a contents page.
	try:
		req = requests.get("https://en.wikipedia.org/wiki/Special:Random").text
		soup = BeautifulSoup(req, 'lxml')
		toctitle = soup.find('div', class_='toctitle').text
		first_paragraph = soup.find('div', id='mw-content-text').p.text
		print('Searching...')
	except AttributeError:
		print('Searching...')
		continue

	# Display the first paragraph to the user with all of the answers 
	# replaced by '-'
	answer = soup.find('h1').text
	answer_list = answer.lower().split()

	# Make sure that the first_paragraph is not empty.
	if len(first_paragraph.split()) > 30 and len(answer_list) <= 3:

		for word in answer_list:
			first_paragraph = first_paragraph.lower().replace(word, '-'.center(len(word), '-'))

		print(first_paragraph)

		# Loop for each wiki page the user can guess on.
		while points > 0:
			user_input = input('What is your guess?...').lower()

			if user_input == 'next':
				points -= 5
				print('The correct answer is ' + answer)
				display_points(points, tokens)
				break
			elif user_input == 'n':
				print('Fine... ya big baby.')
				print('The answer was ' + '\'' +  answer + '\'' + ' by the way... its not that hard.')
				display_points(points, tokens)
				break
			elif user_input.isdigit():
				points -= int(user_input)
				print(str(user_input) + ' have been added to your score.')
				display_points(points, tokens)
			elif user_input == 'q':
				exit = False
				display_points(points, tokens)
				break
			elif len(user_input) <= 2:
				print('you have to guess a longer word...')
				continue
			elif user_input == answer.lower():
				points += 10
				tokens += 1
				print('You got it correct!')
				display_points(points, tokens)
				break
			elif user_input in answer_list:
				points -= 1
				tokens += 1
				print("Alright close enough, I'll give it to you...")
				print('The actuall answer is ' + answer)
				display_points(points, tokens)
				break
			else:
				points -= 2
				print('Wrong!!')
				display_points(points, tokens)
				continue
	else:
		print('Searching...')
		continue













