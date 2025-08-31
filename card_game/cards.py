# card class
class Card:
	def __init__(self, word, location):
		self.card = word
		self.location = location
		# Track when a card has been matched
		self.matched = False
	
	def __eq__(self, other):
		return self.card == other.card
	
	def __str__(self):
		return self.card
	
	# New method: pretty-print all the details
	def info(self):
		return f"Card(word='{self.card}', location='{self.location}', matched={self.matched})"	
	
# Test Code to make sure it only uses "__main__"
# which will only run in this file
if __name__ == '__main__':
	card1 = Card('egg', 'A1')
	card2 = Card('egg', 'B1')
	card3 = Card('hut', 'D4')
	
	print(card1 == card2)
	print(card1 == card3)
	print(card1)
		
# hold a card
# matched or not?
# location of card on grid
# __eq__ are cards equal
# __str__ print out cards for user