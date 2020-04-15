#!/usr/bin/env python
"""トランプテストクラス"""
# import pytest
from python_trump import trump


def test_suit():
    assert trump.Trump(trump.Trump.SPADE, 1).get_suit_short_string() == "S"
