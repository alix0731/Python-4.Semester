class Deck:

	def __init__(self, cards):
		self.__cards = cards 

	def __repr__(self):
		return self.__dict__

	def __getitem__(self, key):
		return self.__cards[key]
	def __len__(self):
		return len(self.__cards)

	def __setitem__(self, key, value):
		self.__cards[key] = value

	def printAll(self):
		for a in self.__cards:
			print(a)

	def __add__(self, add):
		self.__cards.append(add)
	
	def __remove__(self, delete):
		self.__cards.remove(delete)





		
	

