#!/usr/bin/env python
"""手札テストクラス."""
from python_trump import trump_hand
from python_trump import trump


def test_add_001():
    """トランプを手札に追加."""
    hand = trump_hand.TrumpHand()
    hand.add(trump.Trump(trump.Trump.JOKER, 1))
    assert hand.size() == 1
    t = hand.index(0)
    assert t.get_suit() == trump.Trump.JOKER
    assert t.get_number() == 1


def test_add_002():
    """トランプを手札に追加(2枚)."""
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
    """手札からトランプを削除(1枚)."""
    hand = trump_hand.TrumpHand()
    hand.add(trump.Trump(trump.Trump.CLUB, 13))
    t = hand.remove(0)
    assert t.get_suit() == trump.Trump.CLUB
    assert t.get_number() == 13
    assert hand.size() == 0


def test_remove_002():
    """手札からトランプを削除(2枚)."""
    hand = trump_hand.TrumpHand()
    hand.add(trump.Trump(trump.Trump.SPADE, 5))
    hand.add(trump.Trump(trump.Trump.JOKER, 1))
    t = hand.remove(0)
    assert t.get_suit() == trump.Trump.SPADE
    assert t.get_number() == 5
    assert hand.size() == 1
    t2 = hand.remove(0)
    assert t2.get_suit() == trump.Trump.JOKER
    assert t2.get_number() == 1
    assert hand.size() == 0


def test_remove_card_001():
    """指定したカードを削除(カードを生成)."""
    hand = trump_hand.TrumpHand()
    hand.add(trump.Trump(trump.Trump.JOKER, 1))
    t = hand.remove_trump(trump.Trump(trump.Trump.JOKER, 1))
    assert t.get_suit() == trump.Trump.JOKER
    assert t.get_number() == 1
    assert hand.size() == 0


def test_remove_card_002():
    """指定したカードを削除(index指定)."""
    hand = trump_hand.TrumpHand()
    hand.add(trump.Trump(trump.Trump.SPADE, 4))
    t = hand.remove_trump(hand.index(0))
    assert t.get_suit() == trump.Trump.SPADE
    assert t.get_number() == 4
    assert hand.size() == 0


def test_remove_card_003():
    """指定したカードを削除."""
    hand = trump_hand.TrumpHand()
    hand.add(trump.Trump(trump.Trump.SPADE, 4))
    hand.add(trump.Trump(trump.Trump.HEART, 4))
    hand.add(trump.Trump(trump.Trump.DIAMOND, 4))
    hand.add(trump.Trump(trump.Trump.CLUB, 4))
    rt = hand.remove_trump(trump.Trump(trump.Trump.HEART, 4))
    assert rt.get_suit() == trump.Trump.HEART
    assert rt.get_number() == 4
    assert hand.size() == 3
    t = hand.index(0)
    assert t.get_suit() == trump.Trump.SPADE
    assert t.get_number() == 4
    t2 = hand.index(1)
    assert t2.get_suit() == trump.Trump.DIAMOND
    assert t2.get_number() == 4
    t3 = hand.index(2)
    assert t3.get_suit() == trump.Trump.CLUB
    assert t3.get_number() == 4


def test_clear_001():
    """手札を全て削除(1枚)."""
    hand = trump_hand.TrumpHand()
    hand.add(trump.Trump(trump.Trump.HEART, 4))
    hand.clear()
    assert hand.size() == 0
    assert hand.is_empty()


def test_clear_002():
    """手札を全て削除(0枚)."""
    hand = trump_hand.TrumpHand()
    hand.clear()
    assert hand.size() == 0
    assert hand.is_empty()


def test_clear_003():
    """手札を全て削除(3枚)."""
    hand = trump_hand.TrumpHand()
    hand.add(trump.Trump(trump.Trump.HEART, 4))
    hand.add(trump.Trump(trump.Trump.SPADE, 10))
    hand.add(trump.Trump(trump.Trump.JOKER, 2))
    hand.clear()
    assert hand.size() == 0
    assert hand.is_empty()


def test_sort_001():
    """3枚のカードをソートする."""
    hand = trump_hand.TrumpHand()
    hand.add(trump.Trump(trump.Trump.CLUB, 5))
    hand.add(trump.Trump(trump.Trump.JOKER, 1))
    hand.add(trump.Trump(trump.Trump.DIAMOND, 4))
    hand.sort()
    t1 = hand.index(0)
    assert t1.get_suit() == trump.Trump.DIAMOND
    assert t1.get_number() == 4
    t2 = hand.index(1)
    assert t2.get_suit() == trump.Trump.CLUB
    assert t2.get_number() == 5
    t3 = hand.index(2)
    assert t3.get_suit() == trump.Trump.JOKER
    assert t3.get_number() == 1


def test_sort_002():
    """4枚のカードをソートする(同一スート)."""
    hand = trump_hand.TrumpHand()
    hand.add(trump.Trump(trump.Trump.HEART, 5))
    hand.add(trump.Trump(trump.Trump.HEART, 1))
    hand.add(trump.Trump(trump.Trump.HEART, 13))
    hand.add(trump.Trump(trump.Trump.HEART, 4))
    hand.sort()
    t1 = hand.index(0)
    assert t1.get_suit() == trump.Trump.HEART
    assert t1.get_number() == 1
    t2 = hand.index(1)
    assert t2.get_suit() == trump.Trump.HEART
    assert t2.get_number() == 4
    t3 = hand.index(2)
    assert t3.get_suit() == trump.Trump.HEART
    assert t3.get_number() == 5
    t4 = hand.index(3)
    assert t4.get_suit() == trump.Trump.HEART
    assert t4.get_number() == 13


def test_sort_003():
    """5枚のカードをソートする(各スート)."""
    hand = trump_hand.TrumpHand()
    hand.add(trump.Trump(trump.Trump.HEART, 1))
    hand.add(trump.Trump(trump.Trump.CLUB, 1))
    hand.add(trump.Trump(trump.Trump.SPADE, 1))
    hand.add(trump.Trump(trump.Trump.DIAMOND, 1))
    hand.add(trump.Trump(trump.Trump.JOKER, 1))
    hand.sort()
    t1 = hand.index(0)
    assert t1.get_suit() == trump.Trump.SPADE
    assert t1.get_number() == 1
    t2 = hand.index(1)
    assert t2.get_suit() == trump.Trump.HEART
    assert t2.get_number() == 1
    t3 = hand.index(2)
    assert t3.get_suit() == trump.Trump.DIAMOND
    assert t3.get_number() == 1
    t4 = hand.index(3)
    assert t4.get_suit() == trump.Trump.CLUB
    assert t4.get_number() == 1
    t5 = hand.index(4)
    assert t5.get_suit() == trump.Trump.JOKER
    assert t5.get_number() == 1


def test_sort_004():
    """3枚のカードをソートする(JOKER2枚)."""
    hand = trump_hand.TrumpHand()
    hand.add(trump.Trump(trump.Trump.JOKER, 2))
    hand.add(trump.Trump(trump.Trump.CLUB, 13))
    hand.add(trump.Trump(trump.Trump.JOKER, 1))
    hand.sort()
    t1 = hand.index(0)
    assert t1.get_suit() == trump.Trump.CLUB
    assert t1.get_number() == 13
    t2 = hand.index(1)
    assert t2.get_suit() == trump.Trump.JOKER
    assert t2.get_number() == 1
    t3 = hand.index(2)
    assert t3.get_suit() == trump.Trump.JOKER
    assert t3.get_number() == 2


def test_index_001():
    """手札からカードの情報を取得する."""
    hand = trump_hand.TrumpHand()
    hand.add(trump.Trump(trump.Trump.JOKER, 2))
    t = hand.index(0)
    assert t.get_suit() == trump.Trump.JOKER
    assert t.get_number() == 2


def test_index_002():
    """手札からカードの情報を取得する(2枚)."""
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
    """手札の枚数を取得する."""
    hand = trump_hand.TrumpHand()
    hand.add(trump.Trump(trump.Trump.HEART, 6))
    assert hand.size() == 1


def test_size_002():
    """手札の枚数を取得する."""
    hand = trump_hand.TrumpHand()
    hand.add(trump.Trump(trump.Trump.DIAMOND, 13))
    hand.add(trump.Trump(trump.Trump.HEART, 6))
    assert hand.size() == 2


def test_is_empty_001():
    """手札が空かチェック."""
    hand = trump_hand.TrumpHand()
    assert hand.is_empty()


def test_is_empty_002():
    """手札が空かチェック(追加して削除)."""
    hand = trump_hand.TrumpHand()
    hand.add(trump.Trump(trump.Trump.HEART, 2))
    hand.remove(0)
    assert hand.is_empty()


def test_copy_list_001():
    """手札のリストをコピーする."""
    hand = trump_hand.TrumpHand()
    hand.add(trump.Trump(trump.Trump.CLUB, 3))
    hand.add(trump.Trump(trump.Trump.SPADE, 10))
    cl = hand.copy_list()
    t1 = cl[0]
    assert t1.get_suit() == trump.Trump.CLUB
    assert t1.get_number() == 3
    t2 = cl[1]
    assert t2.get_suit() == trump.Trump.SPADE
    assert t2.get_number() == 10


def test_copy_list_002():
    """手札のリストをコピーする."""
    hand = trump_hand.TrumpHand()
    hand.add(trump.Trump(trump.Trump.DIAMOND, 1))
    hand.add(trump.Trump(trump.Trump.HEART, 12))
    hand.add(trump.Trump(trump.Trump.JOKER, 2))
    cards = hand.copy_list()
    t1 = cards[0]
    assert t1.get_suit() == trump.Trump.DIAMOND
    assert t1.get_number() == 1
    t2 = cards[1]
    assert t2.get_suit() == trump.Trump.HEART
    assert t2.get_number() == 12
    t3 = cards[2]
    assert t3.get_suit() == trump.Trump.JOKER
    assert t3.get_number() == 2


def test_print_001():
    """手札のリストをコピーする(エラーが起きなければ成功とする)."""
    hand = trump_hand.TrumpHand()
    hand.add(trump.Trump(trump.Trump.DIAMOND, 1))
    hand.print()
