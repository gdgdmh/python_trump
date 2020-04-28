#!/usr/bin/env python
"""トランプテストクラス."""
from python_trump import trump


def test___eq__001():
    """等価演算子==."""
    card1 = trump.Trump(trump.Trump.JOKER, 1)
    card2 = trump.Trump(trump.Trump.JOKER, 1)
    assert card1 == card2


def test___eq__002():
    """等価演算子==(SPADE)."""
    card1 = trump.Trump(trump.Trump.SPADE, 4)
    card2 = trump.Trump(trump.Trump.SPADE, 4)
    assert card1 == card2


def test___eq__003():
    """等価演算子==(HEART)."""
    card1 = trump.Trump(trump.Trump.HEART, 7)
    card2 = trump.Trump(trump.Trump.HEART, 7)
    assert card1 == card2


def test___eq__004():
    """等価演算子==(DIAMOND)."""
    card1 = trump.Trump(trump.Trump.DIAMOND, 12)
    card2 = trump.Trump(trump.Trump.DIAMOND, 12)
    assert card1 == card2


def test___eq__005():
    """等価演算子==のチェック."""
    card1 = trump.Trump(trump.Trump.CLUB, 10)
    card2 = trump.Trump(trump.Trump.CLUB, 10)
    assert card1 == card2


def test___ne__001():
    """等価演算子!(number違い)."""
    card1 = trump.Trump(trump.Trump.JOKER, 1)
    card2 = trump.Trump(trump.Trump.JOKER, 2)
    assert card1 != card2


def test___ne__002():
    """等価演算子!=(スート違い)."""
    card1 = trump.Trump(trump.Trump.DIAMOND, 1)
    card2 = trump.Trump(trump.Trump.CLUB, 1)
    assert card1 != card2


def test_print_string_001():
    """トランプを文字列で表示する(エラーが起きなければ成功とする)."""
    trump.Trump(trump.Trump.DIAMOND, 1).print_string()


def test_get_suit_001():
    """スート取得(JOKER)."""
    assert trump.Trump(trump.Trump.JOKER, 1).get_suit() == trump.Trump.JOKER


def test_get_suit_002():
    """スート取得(SPADE)."""
    assert trump.Trump(trump.Trump.SPADE, 1).get_suit() == trump.Trump.SPADE


def test_get_suit_003():
    """スート取得(HEART)."""
    assert trump.Trump(trump.Trump.HEART, 1).get_suit() == trump.Trump.HEART


def test_get_suit_004():
    """スート取得(DIAMOND)."""
    result = trump.Trump(trump.Trump.DIAMOND, 1).get_suit()
    assert result == trump.Trump.DIAMOND


def test_get_suit_005():
    """スート取得(CLUB)."""
    assert trump.Trump(trump.Trump.CLUB, 1).get_suit() == trump.Trump.CLUB


def test_get_number_001():
    """トランプ番号取得(JOKER)."""
    assert trump.Trump(trump.Trump.JOKER, 1).get_number() == 1


def test_get_number_002():
    """トランプ番号取得(SPADE)."""
    assert trump.Trump(trump.Trump.SPADE, 1).get_number() == 1


def test_get_number_003():
    """トランプ番号取得(HEART)."""
    assert trump.Trump(trump.Trump.HEART, 13).get_number() == 13


def test_get_number_004():
    """トランプ番号取得(DIAMOND)."""
    assert trump.Trump(trump.Trump.DIAMOND, 5).get_number() == 5


def test_get_number_005():
    """トランプ番号取得(CLUB)."""
    assert trump.Trump(trump.Trump.CLUB, 12).get_number() == 12


def test_is_joker_001():
    """ジョーカーか."""
    assert trump.Trump(trump.Trump.JOKER, 1).is_joker()


def test_is_joker_002():
    """ジョーカーか(2枚目)."""
    assert trump.Trump(trump.Trump.JOKER, 2).is_joker()


def test_is_joker_003():
    """ジョーカーか(ジョーカーではない)."""
    assert trump.Trump(trump.Trump.SPADE, 1).is_joker() is not True


def test_is_spade_001():
    """スペードか."""
    assert trump.Trump(trump.Trump.SPADE, 5).is_spade()


def test_is_spade_002():
    """スペードか(スペードではない)."""
    assert trump.Trump(trump.Trump.HEART, 5).is_spade() is not True


def test_is_heart_001():
    """ハートか."""
    assert trump.Trump(trump.Trump.HEART, 8).is_heart()


def test_is_heart_002():
    """ハートか(ハートではない)."""
    assert trump.Trump(trump.Trump.DIAMOND, 8).is_heart() is not True


def test_is_diamond_001():
    """ダイヤモンドか."""
    assert trump.Trump(trump.Trump.DIAMOND, 10).is_diamond()


def test_is_diamond_002():
    """ダイヤモンドか(ダイヤモンドではない)."""
    assert trump.Trump(trump.Trump.CLUB, 10).is_diamond() is not True


def test_is_club_001():
    """クラブか."""
    assert trump.Trump(trump.Trump.CLUB, 12).is_club()


def test_is_club_002():
    """クラブか(クラブではない)."""
    assert trump.Trump(trump.Trump.SPADE, 12).is_club() is not True


def test_get_suit_string_001():
    """トランプの番号(ジョーカーが取得できるかチェック."""
    assert trump.Trump(trump.Trump.JOKER, 1).get_suit_string() == "JOKER"


def test_get_suit_string_002():
    """トランプの番号(スペード)."""
    assert trump.Trump(trump.Trump.SPADE, 2).get_suit_string() == "SPADE"


def test_get_suit_string_003():
    """トランプの番号(ハート)."""
    assert trump.Trump(trump.Trump.HEART, 3).get_suit_string() == "HEART"


def test_get_suit_string_004():
    """トランプの番号(ハート)."""
    assert trump.Trump(trump.Trump.HEART, 12).get_suit_string() == "HEART"


def test_get_suit_string_005():
    """トランプの番号(ダイヤモンド)."""
    assert trump.Trump(trump.Trump.DIAMOND, 4).get_suit_string() == "DIAMOND"


def test_get_suit_string_006():
    """トランプの番号(クラブ)."""
    assert trump.Trump(trump.Trump.CLUB, 5).get_suit_string() == "CLUB"


def test_get_suit_short_string_001():
    """スート省略文字列取得(ジョーカー)."""
    assert trump.Trump(trump.Trump.JOKER, 2).get_suit_short_string() == "J"


def test_get_suit_short_string_002():
    """スート省略文字列取得(スペード)."""
    assert trump.Trump(trump.Trump.SPADE, 13).get_suit_short_string() == "S"


def test_get_suit_short_string_003():
    """スート省略文字列取得(ハート)."""
    assert trump.Trump(trump.Trump.HEART, 4).get_suit_short_string() == "H"


def test_get_suit_short_string_004():
    """スート省略文字列取得(ダイヤモンド)."""
    assert trump.Trump(trump.Trump.DIAMOND, 11).get_suit_short_string() == "D"


def test_get_suit_short_string_005():
    """スート省略文字列取得(クラブ)."""
    assert trump.Trump(trump.Trump.CLUB, 10).get_suit_short_string() == "C"


def test_define_type_string_001():
    """クラスタイプ文字列取得."""
    card = trump.Trump(trump.Trump.JOKER, 1)
    assert trump.Trump.TYPE_STRING == str(type(card))


def test_get_sort_number_001():
    """ソート用番号を取得(ジョーカー)."""
    card = trump.Trump(trump.Trump.JOKER, 1)
    sort_number = card.get_sort_number()
    assert sort_number == (trump.Trump.SUIT_SORT[trump.Trump.JOKER] + 1)


def test_get_sort_number_002():
    """ソート用番号を取得(スペード)."""
    card = trump.Trump(trump.Trump.SPADE, 5)
    sort_number = card.get_sort_number()
    assert sort_number == (trump.Trump.SUIT_SORT[trump.Trump.SPADE] + 5)


def test_get_sort_number_003():
    """ソート用番号を取得(ハート)."""
    card = trump.Trump(trump.Trump.HEART, 10)
    sort_number = card.get_sort_number()
    assert sort_number == (trump.Trump.SUIT_SORT[trump.Trump.HEART] + 10)


def test_get_sort_number_004():
    """ソート用番号を取得(ダイヤモンド)."""
    card = trump.Trump(trump.Trump.DIAMOND, 13)
    sort_number = card.get_sort_number()
    assert sort_number == (trump.Trump.SUIT_SORT[trump.Trump.DIAMOND] + 13)


def test_get_sort_number_005():
    """ソート用番号を取得(クラブ)."""
    card = trump.Trump(trump.Trump.CLUB, 1)
    sort_number = card.get_sort_number()
    assert sort_number == (trump.Trump.SUIT_SORT[trump.Trump.CLUB] + 1)
