from bs4 import BeautifulSoup
import requests

def display_points(points, tokens):
	'''display the points and tokens to the user'''
	if tokens == 1:
		print('You have ' + str(points) + ' points and ' 
			+ str(tokens) + ' token.')
	else:
		print('You have ' + str(points) + ' points and ' 
			+ str(tokens) + ' tokens.')


points = 30
tokens = 0
while 1:
	if not exit or points <= 0:
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

	
	answer = soup.find('h1').text
	answer_list = answer.lower().split()

	# Make sure that the first_paragraph is long enough 
	# and the answer is not too long.
	if len(first_paragraph.split()) > 30 and len(answer_list) <= 3:

		for word in answer_list:
			# Display the first paragraph to the user with all of the answers 
			# replaced by '-'
			first_paragraph = first_paragraph.lower().replace(word, 
													'-'.center(len(word), '-'))

		print(first_paragraph)

		# Loop for each wiki page the user can guess on.
		while points > 0:
			user_input = input('What is your guess?...').lower()
			# Go to the next challange and deduct points for failing to 
			# answer properly.
			if user_input == 'next':
				points -= 5
				print('The correct answer is ' + answer)
				display_points(points, tokens)
				break
			# If the user is givin a paragraph that is not fair they can skip it 
			# without penalty
			elif user_input == 'n':
				print('Fine... ya big baby.')
				print('The answer was ' + '\'' +  answer + '\'' 
					+ ' by the way... its not that hard.')
				display_points(points, tokens)
				break
			# If the user uses a search engine then they must manually deduct 
			# points from their score.
			elif user_input.isdigit():
				points -= int(user_input)
				print(str(user_input) + ' have been added to your score.')
				display_points(points, tokens)
			# 'q' will quit the program and break all loops
			elif user_input == 'q':
				exit = False
				display_points(points, tokens)
				break
			# If there is a question with a middle initial or something small, 
			# it would be too easy to guess. 
			# This will prohibit that from happening.
			# answers must be greater then 2 characters in length.
			elif len(user_input) <= 2:
				print('you have to guess a longer word...')
				continue
			# If the user guess's the question and gets every charecter 
			# correct then they get 10 points back and they get a token.
			elif user_input == answer.lower():
				points += 10
				tokens += 1
				print('You got it correct!')
				display_points(points, tokens)
				break
			# If the user can guess just one word in the answer then they will 
			# be given a point and a token
			elif user_input in answer_list:
				points -= 1
				tokens += 1
				print("Alright close enough, I'll give it to you...")
				print('The actual answer is ' + answer)
				display_points(points, tokens)
				break
			# If the user guesses the answer wrong then 
			# they get deducted 2 points.
			else:
				points -= 2
				print('Wrong!!')
				display_points(points, tokens)
				continue
	else:
		print('Searching...')
		continue


