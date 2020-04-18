#!/usr/bin/env python
"""トランプ手札クラス"""
from python_trump import trump


class TrumpHand:
    """手札クラス"""

    def __init__(self):
        """コンストラクタ"""
        self.hand = []

    def add(self, card):
        """トランプを手札に加える"""
        if str(type(card)) != trump.Trump.TYPE_STRING:
            raise ValueError("card not trump!")
        self.hand.append(card)

    def remove(self, index):
        """手札からトランプを除く"""
        self.hand.remove(self.hand[index])

    def sort(self):
        """手札をソートする"""
        pass

    def index(self, index):
        """手札からカードを取得する"""
        return self.hand[index]

    def size(self):
        """手札の枚数を取得する"""
        return len(self.hand)

    def is_empty(self):
        """手札が空か"""
        return len(self.hand) == 0
