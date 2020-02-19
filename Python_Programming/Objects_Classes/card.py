# SUITs
# Spades   -->  3
# Hearts   -->  2
# Diamonds -->  1
# Clubs    -->  0

# RANKS
# Jack   -->  11
# Queen  -->  12
# King   -->  13


class Card:
    # attributes of the class
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["narf", "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.ranks[self.rank] + " of " + self.suits[self.suit]

    def cmp(self, other):
        # Checks the suits
        if self.suit > other.suit:
            return 1
        if self.suit < other.suit:
            return -1
        # Suits are the same... check ranks
        if self.rank > other.rank:
            return 1
        if self.rank < other.rank:
            return -1
        # Ranks are the same... it’s a tie
        return 0

    def __eq__(self, other):
        return self.cmp(other) == 0

    def __le__(self, other):
        return self.cmp(other) <= 0

    def __ge__(self, other):
        return self.cmp(other) >= 0

    def __gt__(self, other):
        return self.cmp(other) > 0

    def __lt__(self, other):
        return self.cmp(other) < 0

    def __ne__(self, other):
        return self.cmp(other) != 0


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

    def deal(self, hands, num_cards=999):
        num_hands = len(hands)
        for i in range(num_cards):
            if self.is_empty():
                break
            card = self.pop()           # take the top card
            hand = hands[i % num_hands] # whose turn is next
            hand.add(card)              # add the card to the hand


class Hand(Deck):
    def __init__(self, name=""):
        self.cards = []
        self.name = name

    def add(self, card):
        self.cards.append(card)

    def __str__(self):
        s = "Hand " + self.name
        if self.is_empty():
            s += " is empty\n"
        else:
            s += " contains\n"
        return s + Deck.__str__(self)


class OldMaidHands(Hand):
    def remove_matches(self):
        count = 0
        original_cards = self.cards[:] # copy of the list of cards
        for card in original_cards:
            match = Card(3 - card.suit, card.rank)
            if match in self.cards:
                self.cards.remove(card)
                self.cards.remove(match)
                print("Hand {0}: {1} match {2}".format(self.name, card, match))
                count += 1
        return count


'''
three_of_clubs = Card(0, 3)
card1 = Card(1, 11)
card2 = Card(1, 3)
card3 = Card(1, 11)
print(card1)
print(card2)
print(card1 < card2)
print(card1 == card3)
'''
red_deck = Deck()
red_deck.shuffle()
hand = Hand("Gonzalo")
red_deck.deal([hand], 5)
print(hand)
blue_deck = Deck()

print(red_deck)
