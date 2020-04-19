#!/usr/bin/env python
"""エントリーポイント"""
from python_trump import trump
from python_trump import trump_deck
from python_trump import trump_hand


def main():
    print('main')
    # test code
    # list = range(1, 15)
    # for num in list:
    #     print(str(num))
    # type test
    card = trump.Trump(trump.Trump.JOKER, 1)
    print(type(card))
    print(card.get_sort_number())
    # deck test
    deck = trump_deck.TrumpDeck()
    deck.set_no_joker_deck()
    print('main end')
    # hand
    hand = trump_hand.TrumpHand()
    hand.add(trump.Trump(trump.Trump.JOKER, 1))
    hand.add(trump.Trump(trump.Trump.CLUB, 1))
    hand.add(trump.Trump(trump.Trump.SPADE, 1))
    hand.print()
    hand.sort()
    hand.print()


if __name__ == '__main__':
    main()
