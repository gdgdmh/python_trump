#!/usr/bin/env python
"""トランプデッキテストクラス"""

from python_trump import trump_deck


def test_set_full_deck_001():
    """54枚のカードが設定されているかチェック"""
    deck = trump_deck.TrumpDeck()
    deck.set_full_deck()
    assert deck.size() == 54
