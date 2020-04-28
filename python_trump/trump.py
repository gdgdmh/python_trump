#!/usr/bin/env python
"""トランプクラス."""


class Trump:
    """トランプデータクラス."""

    JOKER = 0x00
    SPADE = 0x02
    HEART = 0x04
    DIAMOND = 0x08
    CLUB = 0x010
    MIN_NUMBER = 1
    MAX_NUMBER = 13
    MAX_JOKER = 2
    SUIT_SORT = {SPADE: 0, HEART: 20, DIAMOND: 40, CLUB: 60, JOKER: 80}
    SUIT_STRING = \
        {
            JOKER: "JOKER",
            SPADE: "SPADE",
            HEART: "HEART",
            DIAMOND: "DIAMOND",
            CLUB: "CLUB"
        }
    SUIT_SHORT_STRING = \
        {JOKER: "J", SPADE: "S", HEART: "H", DIAMOND: "D", CLUB: "C"}
    TYPE_STRING = '<class \'python_trump.trump.Trump\'>'

    def __init__(self, suit, number):
        """コンストラクタ."""
        self.suit = suit
        self.number = number
        if suit != Trump.JOKER:
            # 通常のスートは1から13
            assert number >= Trump.MIN_NUMBER and number <= Trump.MAX_NUMBER
        else:
            # ジョーカーは1か2
            assert number >= Trump.MIN_NUMBER and number <= Trump.MAX_JOKER

    def __eq__(self, other):
        """比較演算子==."""
        if not isinstance(other, Trump):
            return NotImplemented
        return (self.suit, self.number) == (other.suit, other.number)

    def __ne__(self, other):
        """比較演算子!=."""
        if not isinstance(other, Trump):
            return NotImplemented
        return (self.suit, self.number) != (other.suit, other.number)

    def print_string(self):
        """トランプを文字列で表示する."""
        print(self.get_suit_short_string() + str(self.number))

    def get_suit(self):
        """トランプのスートを取得する."""
        return self.suit

    def get_number(self):
        """トランプの番号を取得する."""
        return self.number

    def is_joker(self):
        """トランプがジョーカーか."""
        return self.suit == Trump.JOKER

    def is_spade(self):
        """トランプのスートがスペードか."""
        return self.suit == Trump.SPADE

    def is_heart(self):
        """トランプのスートがハートか."""
        return self.suit == Trump.HEART

    def is_diamond(self):
        """トランプのスートがダイアモンドか."""
        return self.suit == Trump.DIAMOND

    def is_club(self):
        """トランプのスートがクラブか."""
        return self.suit == Trump.CLUB

    def get_suit_string(self):
        """スートの文字列を取得する."""
        return Trump.SUIT_STRING[self.suit]

    def get_suit_short_string(self):
        """スートの短縮文字列を取得する."""
        return Trump.SUIT_SHORT_STRING[self.suit]

    def get_sort_number(self):
        """ソート用の番号を取得する."""
        return Trump.SUIT_SORT[self.suit] + self.number
