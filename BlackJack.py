# Mini-project #6 - Blackjack

import simplegui
import random

# player = []
# dealer = []
# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")

in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 10, 'Q': 10, 'K': 10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print
            "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank),
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]],
                          CARD_SIZE)


# define hand class
class Hand:
    def __init__(self):
        self.hand = []  # create Hand object

    def __str__(self):
        j = ''
        for i in self.hand:  # return a string representation of a hand
            j += str(i) + ' '
        return 'Hand contains:' + j

    def add_card(self, card):
        self.hand.append(card)  # add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        value = 0
        for i in self.hand:  # compute the value of the hand, see Blackjack video
            j = str(i)
            k = VALUES[j[1]]
            value += k
        for i in self.hand:
            if (value + 10) <= 21:
                j = str(i)
                if j[1] == 'A':
                    value += 10
        return value

    def draw(self, canvas, pos):
        global constant
        for i in self.hand:  # draw a hand on the canvas, use the draw method for cards
            j = str(i)
            suit = j[0]
            rank = j[1]
            card = Card(suit, rank)
            card.draw(canvas, pos)
            pos[0] += 80


# define deck class

class Deck:
    def __init__(self):
        self.deck = []
        k = ''
        for i in SUITS:  # create a Deck object
            for j in RANKS:
                self.deck.append(Card(i, j))

    def shuffle(self):
        # add cards back to deck and shuffle
        random.shuffle(self.deck)  # use random.shuffle() to shuffle the deck

    def deal_card(self):
        #        print self.deck[len(self.deck) - 1]
        return self.deck.pop()  # deal a card object from the deck

    def __str__(self):
        j = ''
        for i in self.deck:
            j += str(i) + ' '
        return 'Deck contains:' + j  # return a string representing the deck


player = []
dealer = []
check = False


# define event handlers for buttons
def deal():
    global outcome, in_play, dealer, player, cards_deck, check, score
    # your code goes here
    check = True
    cards_deck = Deck()
    cards_deck.shuffle()
    dealer = Hand()
    player = Hand()
    for i in range(2):
        k = cards_deck.deal_card()
        dealer.add_card(k)
        j = cards_deck.deal_card()
        player.add_card(j)
    outcome = 'Hit or Stand?'
    if in_play:
        score -= 1
        outcome = 'Game forefeited'
    in_play = True


def hit():
    # replace with your code below
    global in_play, outcome, score
    if in_play:  # if the hand is in play, hit the player
        player.add_card(cards_deck.deal_card())
        i = player.get_value()  # if busted, assign a message to outcome, update in_play and score
        if i > 21:
            outcome = 'You are busted, dealer wins.'
            score -= 1
            in_play = False


def stand():
    global in_play, outcome, score
    if player != []:
        if player.get_value() > 21:  # replace with your code below
            outcome = 'You are busted'
    else:
        outcome = 'Deal cards.'
    if in_play:  # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
        while dealer.get_value() < 17:
            dealer.add_card(cards_deck.deal_card())
        if dealer.get_value() > 21:
            outcome = 'Dealer is busted, Player wins.'
            score += 1

        else:
            if player.get_value() <= dealer.get_value():
                outcome = 'Dealer Wins.'
                score -= 1
            else:
                outcome = 'Player Wins.'
                score += 1
        in_play = False

        # assign a message to outcome, update in_play and score


title = 'BLACKJACK'
outcome = 'Hit or Stand?'
dealer_title = 'Dealer Cards'
player_title = 'Player Cards'
score = 0


# draw handler
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    global player, dealer, score
    points = 'Score:' + str(score)
    if check:
        player.draw(canvas, [100, 350])
        dealer.draw(canvas, [100, 100])
    canvas.draw_text(title, [220, 40], 32, 'white', 'sans-serif')
    canvas.draw_text(outcome, [240, 300], 26, 'black', 'sans-serif')
    canvas.draw_text(dealer_title, [110, 90], 26, 'white', 'sans-serif')
    canvas.draw_text(player_title, [110, 330], 26, 'white', 'sans-serif')
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [136.5, 149], CARD_SIZE)
    canvas.draw_text(points, [450, 90], 26, 'black', 'sans-serif')


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

# create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit", hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# get things rolling
frame.start()
