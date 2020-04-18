#!/usr/bin/env python
"""エントリーポイント"""
from python_trump import trump
from python_trump import trump_deck


def main():
    print('main')
    # test code
    # list = range(1, 15)
    # for num in list:
    #     print(str(num))
    # type test
    card = trump.Trump(trump.Trump.JOKER, 1)
    print(type(card))
    deck = trump_deck.TrumpDeck()
    deck.print()
    # list_test = []
    # list_test.pop()

    deck = trump_deck.TrumpDeck()
    deck.set_no_joker_deck()
    deck.print()
    deck.shuffle()
    deck.shuffle()
    deck.shuffle()
    deck.print()

    print('main end')


if __name__ == '__main__':
    main()
