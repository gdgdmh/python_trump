#!/usr/bin/env python
"""ババ抜きプレイヤーテストクラス"""
from python_trump import old_maid_player
from python_trump import trump


def test_add_hand_001():
    """手札にカードを追加チェック"""
    player = old_maid_player.OldMaidPlayer()
    assert player.get_hand_size() == 0
    player.add_hand(trump.Trump(trump.Trump.SPADE, 2))
    assert player.get_hand_size() == 1


def test_add_hand_002():
    """手札にカードを追加チェック"""
    player = old_maid_player.OldMaidPlayer()
    assert player.get_hand_size() == 0
    player.add_hand(trump.Trump(trump.Trump.HEART, 12))
    assert player.get_hand_size() == 1
    player.add_hand(trump.Trump(trump.Trump.JOKER, 2))
    assert player.get_hand_size() == 2
    player.add_hand(trump.Trump(trump.Trump.CLUB, 6))
    assert player.get_hand_size() == 3


def test_play_hand_001():
    """手札からカードを出す"""
    pass


def test_get_pair_001():
    """dummy"""
    pass


def test_get_hand_size_001():
    """手札の枚数を取得チェック"""
    player = old_maid_player.OldMaidPlayer()
    assert player.get_hand_size() == 0
    player.add_hand(trump.Trump(trump.Trump.JOKER, 2))
    assert player.get_hand_size() == 1
    player.add_hand(trump.Trump(trump.Trump.DIAMOND, 1))
    assert player.get_hand_size() == 2
