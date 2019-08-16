import random



class Deck:
    #inputs to describe the deck in question
    def __init__(self, nr_lands, nr_good_lands, nr_cards):
        self.nr_lands = nr_lands
        self.nr_good_lands = nr_good_lands
        self.nr_cards = nr_cards
        
    # Draw a random card from the deck and then evaluate cards remaining in deck
    def draw_card(self):
        card = random.randint(1,self.nr_cards)
        if card > self.nr_lands:
            self.nr_cards -= 1
            card_type = 3
        elif card <= self.nr_good_lands:
            self.nr_cards -= 1
            self.nr_good_lands -=1
            card_type = 1
        else:
            self.nr_cards -= 1
            self.nr_lands -= 1
            card_type = 2
        print (self.nr_cards)
        return card_type

    # Draw an opening hand of 7 cards and then make basic mulligan decisions based on num of lands in hand	
    def draw_opening_hand(self):
        gd_lands_in_hand = 0
        lands_in_hand = 0
        cards_in_hand = 0
        n_mulls = 0
        #loop draw_card() until mulligan parameters are met. (>2 lands <6 lands == keep).
        # A mulligan is done by shuffling your hand of 7 back into your library and then drawing a new hand of 7. For each mulligan(n), the player must put n cards on the bottom of their library. 
        while cards_in_hand <= 7: 
            if cards_in_hand == 7:
                if 2 <= lands_in_hand < 5:
                    print("Keep", lands_in_hand, cards_in_hand, n_mulls)
                    return [lands_in_hand, gd_lands_in_hand, (cards_in_hand - n_mulls), self.nr_cards]
                else: 
                    n_mulls += 1
                    self.nr_cards = cards_in_hand + self.nr_cards
                    cards_in_hand = 0
                    lands_in_hand = 0
                    gd_lands_in_hand = 0
                    print ("Mulligan")
            card_type = self.draw_card()
            if card_type < 3:
                lands_in_hand += 1
                cards_in_hand += 1
                if card_type == 1:
                    gd_lands_in_hand += 1
            elif card_type == 3:
                cards_in_hand += 1

test_deck = Deck(24,14,60)
print (test_deck.draw_opening_hand())