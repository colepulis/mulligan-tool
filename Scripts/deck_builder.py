import random



class Deck:
    #inputs to describe the deck in question
    def __init__(self):
        self.nr_lands = 24
        self.nr_good_lands = 17
        self.nr_cards = 60
        self.gd_lands_in_hand = 0
        self.lands_in_hand = 0 
        self.cards_in_hand = 0 
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
        #print (self.nr_cards)
        return card_type
        
    # Draw an opening hand of 7 cards and then make basic mulligan decisions based on num of lands in hand	
    def draw_opening_hand(self):
        n_mulls = 0
        #loop draw_card() until mulligan parameters are met. (>=2 lands <=4 lands == keep).
        # A mulligan is done by shuffling your hand of 7 back into your library and then drawing a new hand of 7. For each mulligan(n), the player must put n cards from their hand onto the bottom of their library. 
        while self.cards_in_hand <= 7: 
            if self.cards_in_hand == 7:
                if 2 <= self.lands_in_hand < 5:
                    #print("Keep", self.lands_in_hand, self.cards_in_hand, n_mulls)
                    if self.lands_in_hand >= (self.cards_in_hand -1):
                        self.lands_in_hand = (self.cards_in_hand -1)
                    return [self.lands_in_hand, self.gd_lands_in_hand, (self.cards_in_hand - n_mulls), self.nr_cards]
                else: 
                    n_mulls += 1
                    self.nr_cards = self.cards_in_hand + self.nr_cards
                    self.cards_in_hand = 0
                    self.lands_in_hand = 0
                    self.gd_lands_in_hand = 0
                    #print ("Mulligan")
            card_type = self.draw_card()
            if card_type < 3:
                self.lands_in_hand += 1
                self.cards_in_hand += 1
                if card_type == 1:
                    self.gd_lands_in_hand += 1
            elif card_type == 3:
                self.cards_in_hand += 1

class Play:	
    def __init__(self, turns_allowed, gd_lands_needed):
        self.turns_allowed = turns_allowed
        self.gd_lands_needed = gd_lands_needed

    def play_turns_allowed(self):
        n_turns = 1
        starting_deck = Deck()
        temp_list = starting_deck.draw_opening_hand()
        self.lands_in_hand, self.gd_lands_in_hand, self.cards_in_hand, nr_cards = [temp_list[i] for i in range(len(temp_list))]
        if self.turns_allowed == 1:
            if self.gd_lands_in_hand >= self.gd_lands_needed: return True
            else: return False
        else:
            while n_turns <= self.turns_allowed and self.gd_lands_in_hand <= self.gd_lands_needed:
                n_turns += 1
                card_type = starting_deck.draw_card()
                if card_type < 3:
                    self.lands_in_hand += 1
                    self.cards_in_hand += 1
                    if card_type == 1:
                        self.gd_lands_in_hand += 1
                else:
                    self.cards_in_hand += 1
            if self.lands_in_hand <= self.turns_allowed: return True
            else:
                #print ("Total lands: ", self.lands_in_hand,"\nGood lands: ", self.gd_lands_in_hand,"\nCards drawn: ", self.cards_in_hand,"\nCards left in deck: ", nr_cards)
                return False
            
    def repeat_fn(self, n, fn):    
        n_runs = 0
        n_successes = 0
        for _ in range(n):
            simulation = fn()
            n_runs += 1
            if simulation: n_successes += 1
        return n_successes/n_runs

#card parameters        
test = Play(5,3)
print (test.repeat_fn(100000,test.play_turns_allowed))
