#!/usr/bin/env python
"""エントリーポイント."""
from python_trump import trump
from python_trump import trump_deck
from python_trump import trump_hand
from python_trump import old_maid_player
from python_trump import old_maid
from python_trump import old_maid_game


def main():
    """エントリーポイント."""
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
    # player
    player = old_maid_player.OldMaidPlayer()
    player.add_hand(trump.Trump(trump.Trump.SPADE, 1))
    player.add_hand(trump.Trump(trump.Trump.HEART, 2))
    player.print_hand()
    pair_list = player.get_pair()
    len(pair_list) == 2
    # old_maid
    om = old_maid.OldMaid(4)
    om.initialize_game()
    # old_maid_game
    og = old_maid_game.OldMaidGame()
    og.task()
    og.task()
    og.task()
    og.task()
    og.task()
    og.task()
    og.task()
    og.task()


if __name__ == '__main__':
    main()
