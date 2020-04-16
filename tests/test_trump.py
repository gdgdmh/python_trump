#!/usr/bin/env python
"""トランプテストクラス"""
# import pytest
from python_trump import trump


def test_get_suit_joker():
    assert trump.Trump(trump.Trump.JOKER, 1).get_suit() == trump.Trump.JOKER


def test_get_suit_spade():
    assert trump.Trump(trump.Trump.SPADE, 1).get_suit() == trump.Trump.SPADE


def test_get_suit_heart():
    assert trump.Trump(trump.Trump.HEART, 1).get_suit() == trump.Trump.HEART


def test_get_suit_diamond():
    result = trump.Trump(trump.Trump.DIAMOND, 1).get_suit()
    assert result == trump.Trump.DIAMOND


def test_get_suit_club():
    assert trump.Trump(trump.Trump.CLUB, 1).get_suit() == trump.Trump.CLUB


def test_get_number_joker():
    assert trump.Trump(trump.Trump.JOKER, 1).get_number() == 1


def test_get_number_spade():
    assert trump.Trump(trump.Trump.SPADE, 1).get_number() == 1


def test_get_number_heart():
    assert trump.Trump(trump.Trump.HEART, 13).get_number() == 13


def test_get_number_diamond():
    assert trump.Trump(trump.Trump.DIAMOND, 5).get_number() == 5


def test_get_number_club():
    assert trump.Trump(trump.Trump.CLUB, 12).get_number() == 12


def test_get_suit_string_joker():
    assert trump.Trump(trump.Trump.JOKER, 1).get_suit_string() == "JOKER"


def test_get_suit_string_spade():
    assert trump.Trump(trump.Trump.SPADE, 2).get_suit_string() == "SPADE"


def test_get_suit_string_heart():
    assert trump.Trump(trump.Trump.HEART, 3).get_suit_string() == "HEART"


def test_get_suit_string_diamond():
    assert trump.Trump(trump.Trump.DIAMOND, 4).get_suit_string() == "DIAMOND"


def test_get_suit_string_club():
    assert trump.Trump(trump.Trump.HEART, 5).get_suit_string() == "HEART"


def test_get_suit_short_string_joker():
    assert trump.Trump(trump.Trump.JOKER, 2).get_suit_short_string() == "J"


def test_get_suit_short_string_spade():
    assert trump.Trump(trump.Trump.SPADE, 13).get_suit_short_string() == "S"


def test_get_suit_short_string_heart():
    assert trump.Trump(trump.Trump.HEART, 1).get_suit_short_string() == "H"


def test_get_suit_short_string_diamond():
    assert trump.Trump(trump.Trump.DIAMOND, 1).get_suit_short_string() == "D"


def test_get_suit_short_string_club():
    assert trump.Trump(trump.Trump.CLUB, 1).get_suit_short_string() == "C"
