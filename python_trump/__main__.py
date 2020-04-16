#!/usr/bin/env python
"""エントリーポイント"""
from python_trump import trump
from python_trump import trump_deck


def main():
    print('main')
    trump_test = trump.Trump(trump.Trump.SPADE, 1)
    trump_test.print_string()

    deck = trump_deck.TrumpDeck()
    deck.set_full_deck()
    # deck.print()


if __name__ == '__main__':
    main()
