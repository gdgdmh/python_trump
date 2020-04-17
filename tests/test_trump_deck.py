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
            assert (card.get_number() >= 1 and card.get_number() <= 2)
        elif card.is_spade():
            spade_count += 1
            assert (card.get_number() >= 1 and card.get_number() <= 13)
        elif card.is_heart():
            heart_count += 1
            assert (card.get_number() >= 1 and card.get_number() <= 13)
        elif card.is_diamond():
            diamond_count += 1
            assert (card.get_number() >= 1 and card.get_number() <= 13)
        elif card.is_club():
            club_count += 1
            assert (card.get_number() >= 1 and card.get_number() <= 13)
    assert joker_count == 2
    assert spade_count == 13
    assert heart_count == 13
    assert diamond_count == 13
    assert club_count == 13


def test_set_full_deck_003():
    """54枚のカードを厳密にチェックする"""
    deck = trump_deck.TrumpDeck()
    deck.set_full_deck()
    size = deck.size()
    assert size == 54
    # 各数値が1つずつ存在する事を確認する
    joker_list = list(range(1, 3))
    spade_list = list(range(1, 14))
    heart_list = list(range(1, 14))
    diamond_list = list(range(1, 14))
    club_list = list(range(1, 14))
    for i in range(size):
        card = deck.index(i)
        if card.is_joker():
            assert (card.get_number() >= 1 and card.get_number() <= 2)
            joker_list.remove(card.get_number())
        elif card.is_spade():
            assert (card.get_number() >= 1 and card.get_number() <= 13)
            spade_list.remove(card.get_number())
        elif card.is_heart():
            assert (card.get_number() >= 1 and card.get_number() <= 13)
            heart_list.remove(card.get_number())
        elif card.is_diamond():
            assert (card.get_number() >= 1 and card.get_number() <= 13)
            diamond_list.remove(card.get_number())
        elif card.is_club():
            assert (card.get_number() >= 1 and card.get_number() <= 13)
            club_list.remove(card.get_number())
    # 全てのカードのnumberを重複なしで取り出せたなら各listが0になる
    assert len(joker_list) == 0
    assert len(spade_list) == 0
    assert len(heart_list) == 0
    assert len(diamond_list) == 0
    assert len(club_list) == 0


def set_one_joker_deck_001():
    """53枚のカードをチェックする"""
    deck = trump_deck.TrumpDeck()
    deck.set_one_joker_deck()
    size = deck.size()
    assert size == 53
    # 各数値が1つずつ存在する事を確認する
    joker_list = list(range(1, 2))
    spade_list = list(range(1, 14))
    heart_list = list(range(1, 14))
    diamond_list = list(range(1, 14))
    club_list = list(range(1, 14))
    for i in range(size):
        card = deck.index(i)
        if card.is_joker():
            assert (card.get_number() == 1)
            joker_list.remove(card.get_number())
        elif card.is_spade():
            assert (card.get_number() >= 1 and card.get_number() <= 13)
            spade_list.remove(card.get_number())
        elif card.is_heart():
            assert (card.get_number() >= 1 and card.get_number() <= 13)
            heart_list.remove(card.get_number())
        elif card.is_diamond():
            assert (card.get_number() >= 1 and card.get_number() <= 13)
            diamond_list.remove(card.get_number())
        elif card.is_club():
            assert (card.get_number() >= 1 and card.get_number() <= 13)
            club_list.remove(card.get_number())
    # 全てのカードのnumberを重複なしで取り出せたなら各listが0になる
    assert len(joker_list) == 0
    assert len(spade_list) == 0
    assert len(heart_list) == 0
    assert len(diamond_list) == 0
    assert len(club_list) == 0


def set_no_joker_deck_001():
    """52枚のカードをチェックする"""
    deck = trump_deck.TrumpDeck()
    deck.set_no_joker_deck()
    size = deck.size()
    assert size == 52
    # 各数値が1つずつ存在する事を確認する
    spade_list = list(range(1, 14))
    heart_list = list(range(1, 14))
    diamond_list = list(range(1, 14))
    club_list = list(range(1, 14))
    for i in range(size):
        card = deck.index(i)
        if card.is_spade():
            assert (card.get_number() >= 1 and card.get_number() <= 13)
            spade_list.remove(card.get_number())
        elif card.is_heart():
            assert (card.get_number() >= 1 and card.get_number() <= 13)
            heart_list.remove(card.get_number())
        elif card.is_diamond():
            assert (card.get_number() >= 1 and card.get_number() <= 13)
            diamond_list.remove(card.get_number())
        elif card.is_club():
            assert (card.get_number() >= 1 and card.get_number() <= 13)
            club_list.remove(card.get_number())
    # 全てのカードのnumberを重複なしで取り出せたなら各listが0になる
    assert len(spade_list) == 0
    assert len(heart_list) == 0
    assert len(diamond_list) == 0
    assert len(club_list) == 0
