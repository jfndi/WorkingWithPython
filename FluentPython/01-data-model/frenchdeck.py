#
# Simple example demonstrating the power of implementing just two special
# methods: __getitem__ and __len__.
#
import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        print("===> Calling __init__()")
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        print('===> Calling __len__()')
        return len(self._cards)

    def __getitem__(self, position):
        print('===> Calling __getitem__()')
        return self._cards[position]


if __name__ == '__main__':
    print('Creating a FrenchDeck instance')
    deck = FrenchDeck()
    print(f'Number of cards in a FrenchDeck: {len(deck)}')

    from random import choice
    card = choice(deck)
    print(f'Chosen card is: {card}')
    card = choice(deck)
    print(f'Another card is: {card}')

    print('Iterate the collection.')
    iteration = 1
    for card in deck:
        print(f'{iteration}: {card}')
        iteration = iteration + 1

    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

    def spades_high(card):
        rank_value = FrenchDeck.ranks.index(card.rank)
        return rank_value * len(suit_values) + suit_values[card.suit]

    print('Sorted collection')
    iteration = 1
    for card in sorted(deck, key=spades_high):
        print(f'{iteration}: {card}')
        iteration = iteration + 1
