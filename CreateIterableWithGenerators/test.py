from collections import namedtuple


Card = namedtuple("Card", ["rank", "suit"])

class CardDeck:
    SUITS = ('Spades', 'Hearts', 'Diamonds', 'Clubs')
    RANKS = tuple(range(2, 11)) + tuple('JQKA')
        
    def __iter__(self):
        return CardDeck.card_gen()
    
    @staticmethod
    def card_gen():
        for suit in CardDeck.SUITS:
            for rank in CardDeck.RANKS:
                card = Card(rank, suit)
                yield card
        
carditerable = CardDeck()
for i in carditerable:
    print(i)
