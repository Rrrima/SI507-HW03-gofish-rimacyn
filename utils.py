import random

class Card(object):
	suit_names =  ["Diamonds","Clubs","Hearts","Spades"]
	rank_levels = [1,2,3,4,5,6,7,8,9,10,11,12,13]
	faces = {1:"Ace",11:"Jack",12:"Queen",13:"King"}

	def __init__(self, suit=0,rank=2):
		self.suit = self.suit_names[suit]
		if rank in self.faces: # self.rank handles printed representation
			self.rank = self.faces[rank]
		else:
			self.rank = rank
		self.rank_num = rank # To handle winning comparison

	def __str__(self):
		return "{} of {}".format(self.rank,self.suit)

class Hand(object):
	# create the Hand with an initial set of cards
	# param: a list of cards
	def __init__(self, init_cards):
		self.cards  = init_cards

	# add a card to the hand
	# silently fails if the card is already in the hand
	# param: the card to add
	# returns: nothing
	def add_card(self, card):
		if card not in self.cards:
			self.cards.append(card)
		else:
			return

	# remove a card from the hand
	# param: the card to remove
	# returns: the card, or None if the card was not in the Hand
	def remove_card(self, card):
		if card in self.cards:
			self.cards.remove(card)
			return card
		else:
			return None

	# draw a card from a deck and add it to the hand
	# side effect: the deck will be depleted by one card
	# param: the deck from which to draw
	# returns: nothing
	def draw(self, deck):
		dcard = deck.pop_card()
		self.cards.append(dcard)

	# looks for pairs of cards in a hand and removes them. 
	# Note that if there are three of a kind, only two should be removed 
	def remove_pairs(self):
		remained_list = []
		remained_str = []
		for each in self.cards:
			if str(each) in remained_str:
				card_index = remained_str.index(str(each))
				remained_str.remove(str(each))
				del remained_list[card_index]
			else:
				remained_list.append(each)
				remained_str.append(str(each))
		self.cards = remained_list

class Deck(object):
	def __init__(self): # Don't need any input to create a deck of cards
		# This working depends on Card class existing above
		self.cards = []
		for suit in range(4):
			for rank in range(1,14):
				card = Card(suit,rank)
				self.cards.append(card) # appends in a sorted order

	def __str__(self):
		total = []
		for card in self.cards:
			total.append(card.__str__())
		# shows up in whatever order the cards are in
		return "\n".join(total) # returns a multi-line string listing each card

	def pop_card(self, i=-1):
		# removes and returns a card from the Deck
		# default is the last card in the Deck
		return self.cards.pop(i) # this card is no longer in the deck -- taken off

	def shuffle(self):
		random.shuffle(self.cards)

	def replace_card(self, card):
		card_strs = [] # forming an empty list
		for c in self.cards: # each card in self.cards (the initial list)
			card_strs.append(c.__str__()) # appends the string that represents that card to the empty list
		if card.__str__() not in card_strs: # if the string representing this card is not in the list already
			self.cards.append(card) # append it to the list

	def sort_cards(self):
		# Basically, remake the deck in a sorted way
		# This is assuming you cannot have more than the normal 52 cars in a deck
		self.cards = []
		for suit in range(4):
			for rank in range(1,14):
				card = Card(suit,rank)
				self.cards.append(card)

	# parameters:(1)#hands (2)#cards per hand
	# return: a list of Hands. 
	def deal(self,hn,cn):
		if cn == -1:
			all_cards = len(self.cards)
			num = int(all_cards/hn)
			hand_list = []
			for i in range(hn-1):
				cur_hand = Hand(self.cards[num*i:num*i+num])
				hand_list.append(cur_hand)
			last_hand = Hand(self.cards[num*(hn-1):all_cards])
			hand_list.append(last_hand)
			return hand_list
		else:
			hand_list = []
			for i in range(hn):
				cur_hand = Hand(self.cards[cn*i:cn*i+cn])
				hand_list.append(cur_hand)
			return hand_list
