#!/usr/bin/env python
"""トランプクラス"""


class Trump:
    """トランプデータクラス"""
    JOKER = 0x00
    SPADE = 0x02
    HEART = 0x04
    DIA = 0x08
    CLUB = 0x010
    MIN_NUMBER = 1
    MAX_NUMBER = 13
    MAX_JOKER = 2
    SPADE_STRING = "SPADE"
    HEART_STRING = "HEART"
    DIA_STRING = "DIAMOND"
    CLUB_STRING = "CLUB"
    SPADE_SHORT_STRING = "S"
    HEART_SHORT_STRING = "H"
    DIA_SHORT_STRING = "D"
    CLUB_SHORT_STRING = "C"

    def __init__(self, suit, number):
        self.suit = suit
        self.number = number
        if suit != Trump.JOKER:
            # 通常のスートは1から13
            assert number >= Trump.MIN_NUMBER and number <= Trump.MAX_NUMBER
        else:
            # ジョーカーは1か2
            assert number >= Trump.MIN_NUMBER and number <= Trump.MAX_JOKER

    def print_string(self):
        """トランプを文字列で表示する"""
        print(self.get_suit_short_string() + str(self.number))

    def get_suit(self):
        """トランプのスートを取得する"""
        return self.suit

    def get_number(self):
        """トランプの番号を取得する"""
        return self.number

    def get_suit_string(self):
        """スートの文字列を取得する"""
        if self.suit == Trump.SPADE:
            return Trump.SPADE_STRING
        elif self.suit == Trump.HEART:
            return Trump.HEART_STRING
        elif self.suit == Trump.DIA:
            return Trump.DIA_STRING
        elif self.suit == Trump.CLUB:
            return Trump.CLUB_STRING

    def get_suit_short_string(self):
        """スートの短縮文字列を取得する"""
        if self.suit == Trump.SPADE:
            return Trump.SPADE_SHORT_STRING
        elif self.suit == Trump.HEART:
            return Trump.HEART_SHORT_STRING
        elif self.suit == Trump.DIA:
            return Trump.DIA_SHORT_STRING
        elif self.suit == Trump.CLUB:
            return Trump.CLUB_SHORT_STRING
