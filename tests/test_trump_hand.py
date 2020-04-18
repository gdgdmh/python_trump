#!/usr/bin/env python
"""手札テストクラス"""
from python_trump import trump_hand
from python_trump import trump


def test_add_001():
    """トランプを手札に追加"""
    hand = trump_hand.TrumpHand()
    hand.add(trump.Trump(trump.Trump.JOKER, 1))
    assert hand.size() == 1
    t = hand.index(0)
    assert t.get_suit() == trump.Trump.JOKER
    assert t.get_number() == 1


def test_add_002():
    """トランプを手札に追加(2枚)"""
    hand = trump_hand.TrumpHand()
    hand.add(trump.Trump(trump.Trump.CLUB, 13))
    hand.add(trump.Trump(trump.Trump.DIAMOND, 5))
    assert hand.size() == 2
    t = hand.index(0)
    assert t.get_suit() == trump.Trump.CLUB
    assert t.get_number() == 13
    t2 = hand.index(1)
    assert t2.get_suit() == trump.Trump.DIAMOND
    assert t2.get_number() == 5
