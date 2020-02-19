from card import Card


class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))

    # Printing the deck
    def print_deck(self):
        for card in self.cards:
            print(card)

    def __str__(self):
        s = ""
        for i in range(len(self.cards)):
            s = s + " " * i + str(self.cards[i]) + "\n"
        return s

    # Shuffling the deck
    def shuffle(self):
        import random
        rng = random.Random()    # Random generator
        rng.shuffle(self.cards)
        # The method below works but the above one is better
        # num_cards = len(self.cards)
        # for i in range(num_cards):
        #    j = rng.randrange(i, num_cards)
        #    # Tuple assignment to swap the cards
        #    (self.cards[i], self.cards[j]) = (self.cards[j], self.cards[i])

    def remove(self, card):
        if card in self.cards:
            self.cards.remove(card)
            return True
        else:
            return False

    def pop(self):
        return self.cards.pop() # removes the last card in the list

    def is_empty(self):
        return self.cards == []


red_deck = Deck()
blue_deck = Deck()

print(red_deck)
