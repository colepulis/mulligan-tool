import random



class Deck:
	#inputs to describe the deck in question
	def __init__(self, nr_lands, nr_good_lands, nr_cards):
		self.nr_lands = nr_lands
		self.nr_good_lands = nr_good_lands
		self.nr_cards = nr_cards
		
	# Draw a random card from the deck and then evaluate cards remaining in deck
	def draw_card(self):
		nr_cards = self.nr_cards
		nr_good_lands = self.nr_good_lands
		nr_lands = self.nr_lands
		card = random.randint(1,nr_cards)
		if card > nr_good_lands and nr_lands:
			nr_cards -= 1
			card_type = 3
		if card > nr_good_lands and card <= nr_lands:
			nr_cards -= 1
			nr_lands -= 1
			card_type = 2
		elif card <= nr_good_lands:
			nr_cards -= 1
			nr_lands -= 1			
			nr_good_lands -= 1
			card_type = 1
		return card_type
		#print(card, nr_good_lands, nr_lands, nr_cards)

	# Draw an opening hand of 7 cards and then make basic mulligan decisions based on num of lands in hand	
	def draw_opening_hand(self):
		draw_card = self.draw_card
		good_lands_in_hand = 0
		lands_in_hand = 0
		cards_in_hand = 0
		n_mulls = 0
		#loop draw_card() until mulligan parameters are met. (>2 lands <6 lands == keep).
		# A mulligan is done by shuffling your hand of 7 back into your library and then drawing a new hand of 7. For each mulligan(n), the player must put n cards on the bottom of their library. 
		while cards_in_hand < 7 and n_mulls < 4: 
			card_type = draw_card()
			if card_type < 3:
				if card_type == 1:
					good_lands_in_hand += 1
				lands_in_hand += 1
				cards_in_hand += 1
			elif card_type == 3:
				cards_in_hand += 1
			if cards_in_hand == 7:
				if 2 < lands_in_hand < 6 or n_mulls == 3:
					print("Keep", lands_in_hand, cards_in_hand, n_mulls)
				else: 
					n_mulls += 1
					cards_in_hand = 0
					lands_in_hand = 0
					good_lands_in_hand = 0
		
standard_test = Deck(24,14,60)
standard_test.draw_opening_hand()			
				