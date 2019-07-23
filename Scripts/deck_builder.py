import random



class deck:
	def draw_card():
		# Manually set lands needed for cmc card
		nr_lands = 24
		nr_good_lands = 14
		nr_cards = 60
		# Code to draw a random card and then evaluate cards remaining in deck
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
		
	# function to draw an opening hand of 7 cards and then make basic mulligan decisions based on num of lands	
	def draw_opening_hand(draw):
		good_lands_in_hand = 0
		lands_in_hand = 0
		cards_in_hand = 0
		mulligan_counter = 0
		#no mulligan
		while cards_in_hand < 7 and mulligan_counter < 4: 
			card_type = draw()
			if card_type < 3:
				if card_type == 1:
					good_lands_in_hand += 1
				lands_in_hand += 1
				cards_in_hand += 1
			elif card_type == 3:
				cards_in_hand += 1
			if cards_in_hand == 7:
				if 2 < lands_in_hand < 6 or mulligan_counter == 3:
					print("Keep", lands_in_hand, cards_in_hand, mulligan_counter)
				else: 
					mulligan_counter += 1
					cards_in_hand = 0
					lands_in_hand = 0
					good_lands_in_hand = 0
				
				
	draw_opening_hand(draw_card)
	