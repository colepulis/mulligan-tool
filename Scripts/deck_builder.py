import random
from decorators import debug


class Deck:
    #inputs to describe the deck in question
    def __init__(self, lands, gd_lands, cards):
        self.lands_in_deck = lands
        self.gd_lands_in_deck = gd_lands
        self.cards_in_deck = cards
        self.gd_lands_in_hand = 0
        self.lands_in_hand = 0 
        self.cards_in_hand = 0
        self.store_nr_lands = lands
        self.store_nr_good_lands = gd_lands
        self.store_nr_cards = cards
    # Draw n cards from the deck and count cards remaining in deck
    def draw_card(self, n_cards):
        for _ in range(n_cards):
            card = random.randint(1,self.cards_in_deck)
            if card <= self.gd_lands_in_deck:
                self.gd_lands_in_hand += 1
                self.lands_in_hand += 1
                self.cards_in_hand += 1
                self.gd_lands_in_deck -= 1
                self.lands_in_deck -= 1
                self.cards_in_deck -= 1
            elif card <= self.lands_in_deck:
                self.lands_in_hand += 1
                self.cards_in_hand += 1
                self.lands_in_deck -= 1
                self.cards_in_deck -= 1
            else:
                self.cards_in_hand += 1
                self.cards_in_deck -= 1
            #print (card, self.cards_in_deck, self.cards_in_hand, self.gd_lands_in_deck, self.gd_lands_in_hand)
    def opening_hand(self, n_mulls=0):
        """ Draws an opening hand of 7 cards and then makes mulligan decsions based on the number of lands.
            If a mulligan is in order, the fn recurs until a suitable hand is found and then puts cards
            back in the deck = to the number of mulligans"""
        self.draw_card(7)
        
        if n_mulls == 2:
            self.cards_in_hand -= n_mulls
            self.cards_in_deck += n_mulls
            return 
        elif 2 <= self.lands_in_hand <= 5:
            if self.lands_in_hand > 3 and n_mulls:
                self.lands_in_hand -= 1
                n_mulls -= 1
            self.cards_in_hand -= n_mulls
            self.cards_in_deck += n_mulls
            
            return   
        else:
            n_mulls += 1
            self.reset_deck()
            self.reset_hand()
            return self.opening_hand(n_mulls)
   
    def play_turns_allowed(self, turns_allowed, gd_lands_needed):
        self.opening_hand()
        self.draw_card(turns_allowed - 1)
        if self.lands_in_hand < turns_allowed:
            return self.play_turns_allowed(turns_allowed, gd_lands_needed)
        elif turns_allowed <= 1:
            if self.gd_lands_in_hand >= gd_lands_needed: return True
            else: return False
        else:
            if self.gd_lands_in_hand >= gd_lands_needed and self.lands_in_hand >= turns_allowed:
                return True
            else: return False
            
    def repeat_fn(self, n, fn, *args):    
        n_successes = 0
        for _ in range(n):
            simulation = fn(*args)
            self.reset_deck()
            self.reset_hand()
            if simulation: n_successes += 1
        print (n, n_successes)
        return (n_successes/n)
    
    def reset_deck(self):
        self.lands_in_deck = self.store_nr_lands
        self.gd_lands_in_deck = self.store_nr_good_lands
        self.cards_in_deck = self.store_nr_cards
        
    def reset_hand(self):
        self.gd_lands_in_hand = 0
        self.lands_in_hand = 0 
        self.cards_in_hand = 0
        
#card parameters        
test = Deck(24,14,60)
#print(test.draw_card(60))
#print (test.play_turns_allowed(5,3))
print (test.repeat_fn(10000,test.play_turns_allowed,5,3))
