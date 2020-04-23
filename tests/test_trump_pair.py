#!/usr/bin/env python
"""トランプペアテストクラス"""
from python_trump import trump_pair
from python_trump import trump


def test_get_001():
    """トランプペアの取得"""
    trump1 = trump.Trump(trump.Trump.SPADE, 9)
    trump2 = trump.Trump(trump.Trump.DIAMOND, 10)
    pair = trump_pair.TrumpPair(trump1, trump2)
    trumps = pair.get()
    assert trumps[0].get_suit() == trump.Trump.SPADE
    assert trumps[0].get_number() == 9
    assert trumps[1].get_suit() == trump.Trump.DIAMOND
    assert trumps[1].get_number() == 10


def test_get_002():
    """トランプペアの取得(2)"""
    trump1 = trump.Trump(trump.Trump.CLUB, 8)
    trump2 = trump.Trump(trump.Trump.HEART, 11)
    pair = trump_pair.TrumpPair(trump1, trump2)
    trumps = pair.get()
    assert trumps[0].get_suit() == trump.Trump.CLUB
    assert trumps[0].get_number() == 8
    assert trumps[1].get_suit() == trump.Trump.HEART
    assert trumps[1].get_number() == 11


def test_get_003():
    """トランプペアの取得(3)"""
    trump1 = trump.Trump(trump.Trump.JOKER, 1)
    trump2 = trump.Trump(trump.Trump.SPADE, 13)
    pair = trump_pair.TrumpPair(trump1, trump2)
    trumps = pair.get()
    assert trumps[0].get_suit() == trump.Trump.JOKER
    assert trumps[0].get_number() == 1
    assert trumps[1].get_suit() == trump.Trump.SPADE
    assert trumps[1].get_number() == 13


def test_get_004():
    """トランプペアの取得(4)"""
    trump1 = trump.Trump(trump.Trump.DIAMOND, 3)
    trump2 = trump.Trump(trump.Trump.JOKER, 2)
    pair = trump_pair.TrumpPair(trump1, trump2)
    trumps = pair.get()
    assert trumps[0].get_suit() == trump.Trump.DIAMOND
    assert trumps[0].get_number() == 3
    assert trumps[1].get_suit() == trump.Trump.JOKER
    assert trumps[1].get_number() == 2
