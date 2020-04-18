#!/usr/bin/env python
"""手札テストクラス"""
from python_trump import trump_hand
from python_trump import trump


def test_add_001():
    """トランプを手札に追加チェック"""
    hand = trump_hand.TrumpHand()
    hand.add(trump.Trump(trump.Trump.JOKER, 1))
    assert hand.size() == 1
    t = hand.index(0)
    assert t.get_suit() == trump.Trump.JOKER
    assert t.get_number() == 1


def test_add_002():
    """トランプを手札に追加チェック(2枚)"""
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


def test_remove_001():
    """手札からトランプを削除チェック(1枚)"""
    hand = trump_hand.TrumpHand()
    hand.add(trump.Trump(trump.Trump.CLUB, 13))
    hand.remove(0)
    assert hand.size() == 0


def test_remove_002():
    """手札からトランプを削除チェック(2枚)"""
    hand = trump_hand.TrumpHand()
    hand.add(trump.Trump(trump.Trump.SPADE, 5))
    hand.add(trump.Trump(trump.Trump.JOKER, 1))
    hand.remove(0)
    assert hand.size() == 1
    hand.remove(0)
    assert hand.size() == 0


def test_sort_001():
    """dummy"""
    pass


def test_index_001():
    """手札からカードの情報を取得する"""
    hand = trump_hand.TrumpHand()
    hand.add(trump.Trump(trump.Trump.JOKER, 2))
    t = hand.index(0)
    assert t.get_suit() == trump.Trump.JOKER
    assert t.get_number() == 2


def test_index_002():
    """手札からカードの情報を取得する(2枚)"""
    hand = trump_hand.TrumpHand()
    hand.add(trump.Trump(trump.Trump.CLUB, 11))
    hand.add(trump.Trump(trump.Trump.SPADE, 3))
    t = hand.index(0)
    assert t.get_suit() == trump.Trump.CLUB
    assert t.get_number() == 11
    t2 = hand.index(1)
    assert t2.get_suit() == trump.Trump.SPADE
    assert t2.get_number() == 3


def test_size_001():
    """手札の枚数を取得する"""
    hand = trump_hand.TrumpHand()
    hand.add(trump.Trump(trump.Trump.HEART, 6))
    assert hand.size() == 1


def test_size_002():
    """手札の枚数を取得する"""
    hand = trump_hand.TrumpHand()
    hand.add(trump.Trump(trump.Trump.DIAMOND, 13))
    hand.add(trump.Trump(trump.Trump.HEART, 6))
    assert hand.size() == 2


def test_is_empty_001():
    """手札が空かチェック"""
    hand = trump_hand.TrumpHand()
    assert hand.is_empty()


def test_is_empty_002():
    """手札が空かチェック(追加して削除)"""
    hand = trump_hand.TrumpHand()
    hand.add(trump.Trump(trump.Trump.HEART, 2))
    hand.remove(0)
    assert hand.is_empty()
