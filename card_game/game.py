from cards import Card
import random

# class game
class Game:
	def __init__(self):
		# Grid Size
		self.size = 4
		# Card Options
		self.card_options = ['Add', 'Boo', 'Cat', 'Dev',
							'Egg', 'Far', 'Gum', 'Hut']
		# Column for top row
		self.columns = ['A', 'B', 'C', 'D']
		self.cards = []
		# location
		self.locations = []
		for column in self.columns:					# ['A', 'B', 'C', 'D']
			for num in range(1, self.size + 1):		# [1, 2, 3, 4]  +1 because Python Range stops before last number
				self.locations.append(f'{column}{num}')

# Methods
	def set_cards(self):
    # We are going to place exactly two copies of each word from self.card_options
    # onto distinct grid locations (like 'A1', 'B3', etc.).
    
    # 'used_locations' remembers every location we've already assigned a card to,
    # so that we never put two cards in the same cell.
		used_locations = []

    # Loop over each word we want to include in the deck.
		for word in self.card_options:

        # Each word needs two cards (a matching pair).
			for i in range(2):
			# Build the set of still-available locations by subtracting
            # the locations already used from the full set of locations.

            # Example:
            #   self.locations = {'A1', 'A2', ..., 'D4'}
            #   used_locations = ['A2', 'B3']
            #   available_locations = {'A1','A3',...,'D4'} minus {'A2','B3'}

				available_locations = set(self.locations) - set(used_locations)

            # random.choice needs a sequence (like a list), not a set, so we convert.
            # Then we pick one random free spot from the available ones.				

				random_location = random.choice(list(available_locations))

            # Mark that spot as taken so it can't be used again for any later card.

				used_locations.append(random_location)

            # Create the actual Card object that "glues" the word to the location.
            # After this line, 'card.card == word' and 'card.location == random_location'.
							
				card = Card(word, random_location)

            # Keep track of this card in the game's master list of cards.

				self.cards.append(card)	

				print(f"[id={id(card)}] Created card: word='{card.card}', "
					f"location='{card.location}', matched={card.matched}")

	
	def create_row(self, num):
	# We’re going to fill this list with 4 cells (for columns A, B, C, D). At the end, 
	# this list gets returned so the grid printer can join it up with bars.		

		row = []

	# We’re going across the row left to right: A, B, C, D. For each column 
	# we’ll look to see if there’s a card at that location.		

		for column in self.columns:

	# Now, for this specific column, we scan through all cards in the game. 
	# Each card has a .location like 'B2'.
				
			for card in self.cards:

	# If we’re building row 2, and we’re on column 'B', then f'{column}{num}' = "B2". 
	# So if card.location matches "B2", we found the occupant for this cell.

				if card.location == f'{column}{num}':

	# If the card has been “flipped and matched,” then it gets revealed.
	# str(card) calls your __str__, which just prints the word ("Egg", "Cat", etc.).
	# If it’s still hidden, append three spaces so the grid looks blank.

					if card.matched:
						row.append(str(card))
					else:
						row.append('   ')
					break
		return row

	# create grid 
	def create_grid(self):		
		header = ' |  ' + 	'  |  '.join(self.columns) + '  |'
		print(header)

		for row in range(1, self.size + 1):
			print_row = f'{row}| '
			get_row = self.create_row(row)
			print_row += ' | '.join(get_row) + ' |'
			print(print_row)

	# check for matches
	def check_match(self, loc1, loc2):
		cards = []
		for card in self.cards:
			if card.location == loc1 or card.location == loc2:
				cards.append(card)
		if cards[0] == cards[1]:
			cards[0].matched = True
			cards[1].matched = True
			return True
		else:
			for card in cards:
				print(f'{card.location}: {card}')
			return False

	def check_win(self):
		for card in self.cards:
			if card.matched == False:
				return False
		return True

	def check_location(self, time):
		while True:
			guess = input(f"What's the location of your {time} card ")
			if guess.upper() in self.locations:
				return guess.upper()
			else:
				print('Not a valid location')
	
	def start_game(self):
		game_running = True
		print("Memory Game")
		self.set_cards()
		while game_running:
			self.create_grid()
			guess1 = self.check_location('First')
			guess2 = self.check_location('Second')
			if self.check_match(guess1, guess2):
				if self.check_win():
					print('You Win!')
					self.create_grid()
					game_running = False
			else:
				input("Those cards were not a match. Press enter to continue.")
	print("Game Over!")
	
# dunder main
if __name__ == '__main__':
	my_game = Game()
	# my_game.set_cards()
	my_game.start_game()

	# my_game.create_grid()A1
	# my_game.cards[0].matched = True
	# my_game.cards[1].matched = True
	# my_game.cards[2].matched = True
	# my_game.cards[3].matched = True
	# print(my_game.create_row(1))
	# print(my_game.create_row(2))
	# print(my_game.create_row(3))
	# print(my_game.create_row(4))
	
	# create game nstance
	# call start game method