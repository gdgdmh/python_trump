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
    player = old_maid_player.OldMaidPlayer()
    player.add_hand(trump.Trump(trump.Trump.HEART, 2))
    assert player.get_hand_size() == 1
    t = player.play_hand(0)
    assert player.get_hand_size() == 0
    assert t.get_suit() == trump.Trump.HEART
    assert t.get_number() == 2


def test_play_hand_002():
    """手札からカードを出す(2枚)"""
    player = old_maid_player.OldMaidPlayer()
    player.add_hand(trump.Trump(trump.Trump.DIAMOND, 2))
    player.add_hand(trump.Trump(trump.Trump.SPADE, 6))
    assert player.get_hand_size() == 2
    t = player.play_hand(0)
    assert player.get_hand_size() == 1
    assert t.get_suit() == trump.Trump.DIAMOND
    assert t.get_number() == 2


def test_play_trump_001():
    """手札からトランプを出す(1枚)"""
    player = old_maid_player.OldMaidPlayer()
    player.add_hand(trump.Trump(trump.Trump.CLUB, 13))
    t = player.play_trump(trump.Trump(trump.Trump.CLUB, 13))
    assert t.get_suit() == trump.Trump.CLUB
    assert t.get_number() == 13
    assert player.get_hand_size() == 0


def test_play_trump_002():
    """手札からトランプを出す(3枚)"""
    player = old_maid_player.OldMaidPlayer()
    player.add_hand(trump.Trump(trump.Trump.SPADE, 2))
    player.add_hand(trump.Trump(trump.Trump.DIAMOND, 2))
    t = player.play_trump(trump.Trump(trump.Trump.SPADE, 2))
    assert t.get_suit() == trump.Trump.SPADE
    assert t.get_number() == 2
    assert player.get_hand_size() == 1


def test_play_trump_003():
    """手札からトランプを出す"""
    player = old_maid_player.OldMaidPlayer()
    player.add_hand(trump.Trump(trump.Trump.HEART, 11))
    player.add_hand(trump.Trump(trump.Trump.DIAMOND, 4))
    player.add_hand(trump.Trump(trump.Trump.JOKER, 1))
    t = player.play_trump(trump.Trump(trump.Trump.JOKER, 1))
    assert t.get_suit() == trump.Trump.JOKER
    assert t.get_number() == 1
    t = player.play_trump(trump.Trump(trump.Trump.HEART, 11))
    assert t.get_suit() == trump.Trump.HEART
    assert t.get_number() == 11
    t = player.play_trump(trump.Trump(trump.Trump.DIAMOND, 4))
    assert t.get_suit() == trump.Trump.DIAMOND
    assert t.get_number() == 4
    assert player.get_hand_size() == 0


def test_play_pair_001():
    """ペアカードを出す(1組)"""
    player = old_maid_player.OldMaidPlayer()
    player.add_hand(trump.Trump(trump.Trump.HEART, 2))
    player.add_hand(trump.Trump(trump.Trump.CLUB, 2))
    pair_list = player.play_pair()
    pair1 = pair_list[0].get()
    # 順不同でS2かH2が設定されている([0]と[1]のスートが一致してないこと)
    assert pair1[0].get_suit() == trump.Trump.HEART or trump.Trump.CLUB
    assert pair1[0].get_number() == 2
    assert pair1[1].get_suit() == trump.Trump.HEART or trump.Trump.CLUB
    assert pair1[1].get_number() == 2
    assert pair1[0].get_suit() != pair1[1].get_suit()
    assert player.get_hand_size() == 0


def test_play_pair_002():
    """ペアカードを出す(ペアなし)"""
    player = old_maid_player.OldMaidPlayer()
    player.add_hand(trump.Trump(trump.Trump.SPADE, 1))
    player.add_hand(trump.Trump(trump.Trump.HEART, 2))
    pair_list = player.play_pair()
    # None or []
    assert not pair_list
    assert player.get_hand_size() == 2


def test_play_pair_003():
    """ペアカードを出す(2ペア同じ数字)"""
    player = old_maid_player.OldMaidPlayer()
    player.add_hand(trump.Trump(trump.Trump.DIAMOND, 13))
    player.add_hand(trump.Trump(trump.Trump.HEART, 13))
    player.add_hand(trump.Trump(trump.Trump.SPADE, 13))
    player.add_hand(trump.Trump(trump.Trump.CLUB, 13))
    pair_list = player.play_pair()
    pair1 = pair_list[0].get()
    assert pair1[0].get_suit() == trump.Trump.DIAMOND or trump.Trump.HEART
    assert pair1[0].get_number() == 13
    assert pair1[1].get_suit() == trump.Trump.DIAMOND or trump.Trump.HEART
    assert pair1[1].get_number() == 13
    assert pair1[0].get_suit() != pair1[1].get_suit()
    pair2 = pair_list[1].get()
    assert pair2[0].get_suit() == trump.Trump.SPADE or trump.Trump.CLUB
    assert pair2[0].get_number() == 13
    assert pair2[1].get_suit() == trump.Trump.SPADE or trump.Trump.CLUB
    assert pair2[1].get_number() == 13
    assert pair2[0].get_suit() != pair1[1].get_suit()
    assert player.get_hand_size() == 0


def test_play_pair_004():
    """ペアカードを出す(JOKER入りでペアにならない)"""
    player = old_maid_player.OldMaidPlayer()
    player.add_hand(trump.Trump(trump.Trump.JOKER, 1))
    player.add_hand(trump.Trump(trump.Trump.DIAMOND, 2))
    player.add_hand(trump.Trump(trump.Trump.HEART, 3))
    player.add_hand(trump.Trump(trump.Trump.SPADE, 4))
    player.add_hand(trump.Trump(trump.Trump.CLUB, 1))
    pair_list = player.play_pair()
    # None or []
    assert not pair_list
    assert player.get_hand_size() == 5


def test_play_pair_005():
    """ペアカードを出す(奇数手札)"""
    player = old_maid_player.OldMaidPlayer()
    player.add_hand(trump.Trump(trump.Trump.DIAMOND, 2))
    player.add_hand(trump.Trump(trump.Trump.HEART, 3))
    player.add_hand(trump.Trump(trump.Trump.SPADE, 2))
    pair_list = player.play_pair()
    pair1 = pair_list[0].get()
    assert pair1[0].get_suit() == trump.Trump.DIAMOND or trump.Trump.SPADE
    assert pair1[0].get_number() == 2
    assert pair1[1].get_suit() == trump.Trump.DIAMOND or trump.Trump.SPADE
    assert pair1[1].get_number() == 2
    assert pair1[0].get_suit() != pair1[1].get_suit()
    assert player.get_hand_size() == 1


def test_play_pair_006():
    """ペアカードを出す(2ペアで違う数字)"""
    player = old_maid_player.OldMaidPlayer()
    player.add_hand(trump.Trump(trump.Trump.DIAMOND, 5))
    player.add_hand(trump.Trump(trump.Trump.HEART, 10))
    player.add_hand(trump.Trump(trump.Trump.SPADE, 10))
    player.add_hand(trump.Trump(trump.Trump.CLUB, 5))
    pair_list = player.play_pair()
    pair1 = pair_list[0].get()
    assert pair1[0].get_suit() == trump.Trump.DIAMOND or trump.Trump.CLUB
    assert pair1[0].get_number() == 5
    assert pair1[1].get_suit() == trump.Trump.DIAMOND or trump.Trump.CLUB
    assert pair1[1].get_number() == 5
    assert pair1[0].get_suit() != pair1[1].get_suit()
    pair2 = pair_list[1].get()
    assert pair2[0].get_suit() == trump.Trump.HEART or trump.Trump.SPADE
    assert pair2[0].get_number() == 10
    assert pair2[1].get_suit() == trump.Trump.HEART or trump.Trump.SPADE
    assert pair2[1].get_number() == 10
    assert pair2[0].get_suit() != pair1[1].get_suit()
    assert player.get_hand_size() == 0


def test_play_pair_007():
    """ペアカードを出す(全部のトランプ)"""
    player = old_maid_player.OldMaidPlayer()
    for n in range(13):
        player.add_hand(trump.Trump(trump.Trump.SPADE, n + 1))
        player.add_hand(trump.Trump(trump.Trump.HEART, n + 1))
        player.add_hand(trump.Trump(trump.Trump.DIAMOND, n + 1))
        player.add_hand(trump.Trump(trump.Trump.CLUB, n + 1))
    pair_list = player.play_pair()
    # 全てチェックするのはナンセンスなのでペアの数だけチェック
    assert len(pair_list) == (52 / 2)
    assert player.get_hand_size() == 0


def test_get_pair_001():
    """ペアの取得"""
    player = old_maid_player.OldMaidPlayer()
    player.add_hand(trump.Trump(trump.Trump.SPADE, 2))
    player.add_hand(trump.Trump(trump.Trump.HEART, 2))
    pair_list = player.get_pair()
    pair1 = pair_list[0].get()
    # 順不同でS2かH2が設定されている([0]と[1]のスートが一致してないこと)
    assert pair1[0].get_suit() == trump.Trump.SPADE or trump.Trump.HEART
    assert pair1[0].get_number() == 2
    assert pair1[1].get_suit() == trump.Trump.SPADE or trump.Trump.HEART
    assert pair1[1].get_number() == 2
    assert pair1[0].get_suit() != pair1[1].get_suit()


def test_get_pair_002():
    """ペアの取得(ペアなし)"""
    player = old_maid_player.OldMaidPlayer()
    player.add_hand(trump.Trump(trump.Trump.SPADE, 1))
    player.add_hand(trump.Trump(trump.Trump.HEART, 2))
    pair_list = player.get_pair()
    # None or []
    assert not pair_list


def test_get_pair_003():
    """ペアの取得(2ペアで同じ数字)"""
    player = old_maid_player.OldMaidPlayer()
    player.add_hand(trump.Trump(trump.Trump.DIAMOND, 13))
    player.add_hand(trump.Trump(trump.Trump.HEART, 13))
    player.add_hand(trump.Trump(trump.Trump.SPADE, 13))
    player.add_hand(trump.Trump(trump.Trump.CLUB, 13))
    pair_list = player.get_pair()
    pair1 = pair_list[0].get()
    assert pair1[0].get_suit() == trump.Trump.DIAMOND or trump.Trump.HEART
    assert pair1[0].get_number() == 13
    assert pair1[1].get_suit() == trump.Trump.DIAMOND or trump.Trump.HEART
    assert pair1[1].get_number() == 13
    assert pair1[0].get_suit() != pair1[1].get_suit()
    pair2 = pair_list[1].get()
    assert pair2[0].get_suit() == trump.Trump.SPADE or trump.Trump.CLUB
    assert pair2[0].get_number() == 13
    assert pair2[1].get_suit() == trump.Trump.SPADE or trump.Trump.CLUB
    assert pair2[1].get_number() == 13
    assert pair2[0].get_suit() != pair1[1].get_suit()


def test_get_pair_004():
    """ペアの取得(JOKER入りでペアにならない)"""
    player = old_maid_player.OldMaidPlayer()
    player.add_hand(trump.Trump(trump.Trump.JOKER, 1))
    player.add_hand(trump.Trump(trump.Trump.DIAMOND, 2))
    player.add_hand(trump.Trump(trump.Trump.HEART, 3))
    player.add_hand(trump.Trump(trump.Trump.SPADE, 4))
    player.add_hand(trump.Trump(trump.Trump.CLUB, 1))
    pair_list = player.get_pair()
    # None or []
    assert not pair_list


def test_get_pair_005():
    """ペアの取得(奇数手札)"""
    player = old_maid_player.OldMaidPlayer()
    player.add_hand(trump.Trump(trump.Trump.DIAMOND, 2))
    player.add_hand(trump.Trump(trump.Trump.HEART, 3))
    player.add_hand(trump.Trump(trump.Trump.SPADE, 2))
    pair_list = player.get_pair()
    pair1 = pair_list[0].get()
    assert pair1[0].get_suit() == trump.Trump.DIAMOND or trump.Trump.SPADE
    assert pair1[0].get_number() == 2
    assert pair1[1].get_suit() == trump.Trump.DIAMOND or trump.Trump.SPADE
    assert pair1[1].get_number() == 2
    assert pair1[0].get_suit() != pair1[1].get_suit()


def test_get_pair_006():
    """ペアの取得(2ペアで違う数字)"""
    player = old_maid_player.OldMaidPlayer()
    player.add_hand(trump.Trump(trump.Trump.DIAMOND, 5))
    player.add_hand(trump.Trump(trump.Trump.HEART, 10))
    player.add_hand(trump.Trump(trump.Trump.SPADE, 10))
    player.add_hand(trump.Trump(trump.Trump.CLUB, 5))
    pair_list = player.get_pair()
    pair1 = pair_list[0].get()
    assert pair1[0].get_suit() == trump.Trump.DIAMOND or trump.Trump.CLUB
    assert pair1[0].get_number() == 5
    assert pair1[1].get_suit() == trump.Trump.DIAMOND or trump.Trump.CLUB
    assert pair1[1].get_number() == 5
    assert pair1[0].get_suit() != pair1[1].get_suit()
    pair2 = pair_list[1].get()
    assert pair2[0].get_suit() == trump.Trump.HEART or trump.Trump.SPADE
    assert pair2[0].get_number() == 10
    assert pair2[1].get_suit() == trump.Trump.HEART or trump.Trump.SPADE
    assert pair2[1].get_number() == 10
    assert pair2[0].get_suit() != pair1[1].get_suit()


def test_get_pair_007():
    """ペアの取得(全部のトランプ)"""
    player = old_maid_player.OldMaidPlayer()
    for n in range(13):
        player.add_hand(trump.Trump(trump.Trump.SPADE, n + 1))
        player.add_hand(trump.Trump(trump.Trump.HEART, n + 1))
        player.add_hand(trump.Trump(trump.Trump.DIAMOND, n + 1))
        player.add_hand(trump.Trump(trump.Trump.CLUB, n + 1))
    pair_list = player.get_pair()
    # 全てチェックするのはナンセンスなのでペアの数だけチェック
    assert len(pair_list) == (52 / 2)


def test_get_hand_size_001():
    """手札の枚数を取得チェック"""
    player = old_maid_player.OldMaidPlayer()
    assert player.get_hand_size() == 0
    player.add_hand(trump.Trump(trump.Trump.JOKER, 2))
    assert player.get_hand_size() == 1
    player.add_hand(trump.Trump(trump.Trump.DIAMOND, 1))
    assert player.get_hand_size() == 2


def test_get_hand_size_002():
    """手札の枚数を取得チェック"""
    player = old_maid_player.OldMaidPlayer()
    assert player.get_hand_size() == 0
    player.add_hand(trump.Trump(trump.Trump.SPADE, 2))
    assert player.get_hand_size() == 1
    player.add_hand(trump.Trump(trump.Trump.SPADE, 1))
    assert player.get_hand_size() == 2
    player.add_hand(trump.Trump(trump.Trump.SPADE, 3))
    assert player.get_hand_size() == 3
