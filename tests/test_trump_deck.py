#!/usr/bin/env python
"""トランプデッキテストクラス"""

from python_trump import trump_deck


def test_set_full_deck_001():
    """54枚のカードが設定されているかチェック"""
    deck = trump_deck.TrumpDeck()
    deck.set_full_deck()
    assert deck.size() == 54


def test_set_full_deck_002():
    """54枚のカードの中身をチェック"""
    deck = trump_deck.TrumpDeck()
    deck.set_full_deck()
    size = deck.size()
    joker_count = 0
    spade_count = 0
    heart_count = 0
    diamond_count = 0
    club_count = 0
    for i in range(size):
        card = deck.index(i)
        if card.is_joker():
            joker_count += 1
        elif card.is_spade():
            spade_count += 1
        elif card.is_heart():
            heart_count += 1
        elif card.is_diamond():
            diamond_count += 1
        elif card.is_club():
            club_count += 1
    assert joker_count == 2
    assert spade_count == 13
    assert heart_count == 13
    assert diamond_count == 13
    assert club_count == 13
