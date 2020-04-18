#!/usr/bin/env python
"""トランプデッキテストクラス"""
from python_trump import trump_deck
from python_trump import trump


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


def test_put_top_001():
    """トランプをデッキをトップに置いているかチェック"""
    deck = trump_deck.TrumpDeck()
    deck.put_top(trump.Trump(trump.Trump.JOKER, 1))
    card = deck.index(0)
    assert str(type(card)) == trump.Trump.TYPE_STRING
    assert card.get_number() == 1
    assert card.get_suit() == trump.Trump.JOKER
    assert card.is_joker()


def test_put_top_002():
    """トランプをデッキをトップに置いているかチェック(2枚)"""
    deck = trump_deck.TrumpDeck()
    deck.put_top(trump.Trump(trump.Trump.JOKER, 1))
    deck.put_top(trump.Trump(trump.Trump.CLUB, 10))
    card_joker = deck.index(0)
    assert str(type(card_joker)) == trump.Trump.TYPE_STRING
    assert card_joker.get_number() == 1
    assert card_joker.get_suit() == trump.Trump.JOKER
    assert card_joker.is_joker()
    card_club = deck.index(1)
    assert str(type(card_club)) == trump.Trump.TYPE_STRING
    assert card_club.get_number() == 10
    assert card_club.get_suit() == trump.Trump.CLUB
    assert card_club.is_club()


def test_put_top_003():
    """トランプをデッキをトップに置いているかチェック(3枚)"""
    deck = trump_deck.TrumpDeck()
    deck.put_top(trump.Trump(trump.Trump.SPADE, 13))
    deck.put_top(trump.Trump(trump.Trump.DIAMOND, 5))
    deck.put_top(trump.Trump(trump.Trump.HEART, 8))
    card_spade = deck.index(0)
    assert str(type(card_spade)) == trump.Trump.TYPE_STRING
    assert card_spade.get_number() == 13
    assert card_spade.get_suit() == trump.Trump.SPADE
    assert card_spade.is_spade()
    card_diamond = deck.index(1)
    assert str(type(card_diamond)) == trump.Trump.TYPE_STRING
    assert card_diamond.get_number() == 5
    assert card_diamond.get_suit() == trump.Trump.DIAMOND
    assert card_diamond.is_diamond()
    card_heart = deck.index(2)
    assert str(type(card_heart)) == trump.Trump.TYPE_STRING
    assert card_heart.get_number() == 8
    assert card_heart.get_suit() == trump.Trump.HEART
    assert card_heart.is_heart()


def test_draw_001():
    """デッキから引くチェック"""
    deck = trump_deck.TrumpDeck()
    deck.put_top(trump.Trump(trump.Trump.HEART, 11))
    card = deck.draw()
    assert str(type(card)) == trump.Trump.TYPE_STRING
    assert card.get_number() == 11
    assert card.get_suit() == trump.Trump.HEART
    assert card.is_heart()


def test_draw_002():
    """デッキから引くチェック(2枚)"""
    deck = trump_deck.TrumpDeck()
    deck.put_top(trump.Trump(trump.Trump.HEART, 9))
    deck.put_top(trump.Trump(trump.Trump.JOKER, 2))
    card_joker = deck.draw()
    assert str(type(card_joker)) == trump.Trump.TYPE_STRING
    assert card_joker.get_number() == 2
    assert card_joker.get_suit() == trump.Trump.JOKER
    assert card_joker.is_joker()
    card_heart = deck.draw()
    assert str(type(card_heart)) == trump.Trump.TYPE_STRING
    assert card_heart.get_number() == 9
    assert card_heart.get_suit() == trump.Trump.HEART
    assert card_heart.is_heart()


def test_index_001():
    """デッキの参照をチェック"""
    deck = trump_deck.TrumpDeck()
    deck.put_top(trump.Trump(trump.Trump.DIAMOND, 3))
    card = deck.index(0)
    assert str(type(card)) == trump.Trump.TYPE_STRING
    assert card.get_number() == 3
    assert card.get_suit() == trump.Trump.DIAMOND
    assert card.is_diamond()


def test_size_001():
    """デッキのサイズをチェック(1枚)"""
    deck = trump_deck.TrumpDeck()
    deck.put_top(trump.Trump(trump.Trump.SPADE, 6))
    assert deck.size() == 1


def test_size_002():
    """デッキのサイズをチェック(0枚)"""
    deck = trump_deck.TrumpDeck()
    assert deck.size() == 0


def test_size_003():
    """デッキのサイズをチェック(2枚)"""
    deck = trump_deck.TrumpDeck()
    deck.set_no_joker_deck()
    assert deck.size() == 52


def test_shuffle_001():
    """デッキのシャッフルをチェック"""
    deck = trump_deck.TrumpDeck()
    deck.set_one_joker_deck()
    deck_default = trump_deck.TrumpDeck()
    deck_default.set_one_joker_deck()
    deck.shuffle()
    size = deck.size()
    same_count = 0
    for i in range(size):
        if deck.index(i) == deck_default.index(i):
            same_count += 1
    # 乱数の程度によるが少なくとも一致が半分以下ならOK
    assert same_count <= (size / 2)
