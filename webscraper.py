from bs4 import BeautifulSoup
import requests

points = 0
while exit:
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
				points += 5
				print('The correct answer is ' + answer)
				print('You have ' + str(points) + ' points.')
				break
			elif user_input.isdigit():
				points += int(user_input)
				print(str(user_input) + ' have been added to your score.')
				print('You now have a score of ' + str(points))
			elif user_input == 'q':
				exit = False
				print('You have a score of ' + str(points))
				break
			elif len(user_input) <= 2:
				print('you have to guess a longer word...')
				continue
			elif user_input == answer.lower():
				points -= 10
				print('You got it correct!')
				print('Your score is ' + str(points))
				break
			elif user_input in answer_list:
				points += 1
				print("Alright close enough, I'll give it to you...")
				print('The actuall answer is ' + answer)
				print('Your score is ' + str(points))
				break
			else:
				points += 2
				print('Wrong!!')
				continue
	else:
		continue




























