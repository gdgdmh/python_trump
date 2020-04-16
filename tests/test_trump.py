#!/usr/bin/env python
"""トランプテストクラス"""
from python_trump import trump


def test_get_suit_001():
    """get_suitでジョーカーが判定できるかチェック"""
    assert trump.Trump(trump.Trump.JOKER, 1).get_suit() == trump.Trump.JOKER


def test_get_suit_002():
    """get_suitでスペードが判定できるかチェック"""
    assert trump.Trump(trump.Trump.SPADE, 1).get_suit() == trump.Trump.SPADE


def test_get_suit_003():
    """get_suitでハートが判定できるかチェック"""
    assert trump.Trump(trump.Trump.HEART, 1).get_suit() == trump.Trump.HEART


def test_get_suit_004():
    """get_suitでダイヤモンドが判定できるかチェック"""
    result = trump.Trump(trump.Trump.DIAMOND, 1).get_suit()
    assert result == trump.Trump.DIAMOND


def test_get_suit_005():
    """get_suitでクラブが判定できるかチェック"""
    assert trump.Trump(trump.Trump.CLUB, 1).get_suit() == trump.Trump.CLUB


def test_get_number_001():
    """get_numberでジョーカーのnumberが取得できるかチェック"""
    assert trump.Trump(trump.Trump.JOKER, 1).get_number() == 1


def test_get_number_002():
    """get_numberでスペードのnumberが取得できるかチェック"""
    assert trump.Trump(trump.Trump.SPADE, 1).get_number() == 1


def test_get_number_003():
    """get_numberでハートのnumberが取得できるかチェック"""
    assert trump.Trump(trump.Trump.HEART, 13).get_number() == 13


def test_get_number_004():
    """get_numberでダイヤモンドのnumberが取得できるかチェック"""
    assert trump.Trump(trump.Trump.DIAMOND, 5).get_number() == 5


def test_get_number_005():
    """get_numberでクラブのnumberが取得できるかチェック"""
    assert trump.Trump(trump.Trump.CLUB, 12).get_number() == 12


def test_is_joker_001():
    """is_jokerで判定できるかチェック"""
    assert trump.Trump(trump.Trump.JOKER, 1).is_joker()


def test_is_joker_002():
    """is_jokerで2枚目のジョーカーを判定できるかチェック"""
    assert trump.Trump(trump.Trump.JOKER, 2).is_joker()


def test_is_joker_003():
    """is_jokerでジョーカーではないカードを判定できるかチェック"""
    assert trump.Trump(trump.Trump.SPADE, 1).is_joker() is not True


def test_is_spade_001():
    """is_spadeで判定できるかチェック"""
    assert trump.Trump(trump.Trump.SPADE, 5).is_spade()


def test_is_spade_002():
    """is_spadeでスペードではないカードを判定できるかチェック"""
    assert trump.Trump(trump.Trump.HEART, 5).is_spade() is not True


def test_is_heart_001():
    """is_heartで判定できるかチェック"""
    assert trump.Trump(trump.Trump.HEART, 8).is_heart()


def test_is_heart_002():
    """is_heartでハートではないカードを判定できるかチェック"""
    assert trump.Trump(trump.Trump.DIAMOND, 8).is_heart() is not True


def test_is_diamond_001():
    """is_diamondで判定できるかチェック"""
    assert trump.Trump(trump.Trump.DIAMOND, 10).is_diamond()


def test_is_diamond_002():
    """is_diamondでダイヤモンドではないカードを判定できるかチェック"""
    assert trump.Trump(trump.Trump.CLUB, 10).is_diamond() is not True


def test_is_club_001():
    """is_clubで判定できるかチェック"""
    assert trump.Trump(trump.Trump.CLUB, 12).is_club()


def test_is_club_002():
    """is_clubでクラブではないカードを判定できるかチェック"""
    assert trump.Trump(trump.Trump.SPADE, 12).is_club() is not True


def test_get_suit_string_001():
    """get_suit_stringでジョーカーが取得できるかチェック"""
    assert trump.Trump(trump.Trump.JOKER, 1).get_suit_string() == "JOKER"


def test_get_suit_string_002():
    """get_suit_stringでスペードが取得できるかチェック"""
    assert trump.Trump(trump.Trump.SPADE, 2).get_suit_string() == "SPADE"


def test_get_suit_string_003():
    """get_suit_stringでハートが取得できるかチェック"""
    assert trump.Trump(trump.Trump.HEART, 3).get_suit_string() == "HEART"


def test_get_suit_string_004():
    """get_suit_stringでハートが取得できるかチェック"""
    assert trump.Trump(trump.Trump.HEART, 12).get_suit_string() == "HEART"


def test_get_suit_string_005():
    """get_suit_stringでダイヤモンドが取得できるかチェック"""
    assert trump.Trump(trump.Trump.DIAMOND, 4).get_suit_string() == "DIAMOND"


def test_get_suit_string_006():
    """get_suit_stringでクラブが取得できるかチェック"""
    assert trump.Trump(trump.Trump.CLUB, 5).get_suit_string() == "CLUB"


def test_get_suit_short_string_001():
    """get_suit_short_stringでジョーカーが取得できるかチェック"""
    assert trump.Trump(trump.Trump.JOKER, 2).get_suit_short_string() == "J"


def test_get_suit_short_string_002():
    """get_suit_short_stringでスペードが取得できるかチェック"""
    assert trump.Trump(trump.Trump.SPADE, 13).get_suit_short_string() == "S"


def test_get_suit_short_string_003():
    """get_suit_short_stringでハートが取得できるかチェック"""
    assert trump.Trump(trump.Trump.HEART, 4).get_suit_short_string() == "H"


def test_get_suit_short_string_004():
    """get_suit_short_stringでダイヤモンドが取得できるかチェック"""
    assert trump.Trump(trump.Trump.DIAMOND, 11).get_suit_short_string() == "D"


def test_get_suit_short_string_005():
    """get_suit_short_stringでクラブが取得できるかチェック"""
    assert trump.Trump(trump.Trump.CLUB, 10).get_suit_short_string() == "C"
