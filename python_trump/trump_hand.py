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
        """手札からトランプを除く(index指定)"""
        card = self.hand[index]
        self.hand.remove(card)
        return card

    def remove_trump(self, card):
        """手札からトランプを除く"""
        self.hand.remove(card)
        return card

    def clear(self):
        """手札を全て削除"""
        self.hand.clear()
        pass

    def sort(self):
        """手札をソートする"""
        self.hand.sort(key=trump.Trump.get_sort_number)

    def index(self, index):
        """手札からカードを取得する"""
        return self.hand[index]

    def size(self):
        """手札の枚数を取得する"""
        return len(self.hand)

    def is_empty(self):
        """手札が空か"""
        return len(self.hand) == 0

    def copy_list(self):
        """リストのコピー"""
        return self.hand.copy()

    def print(self):
        """手札の表示"""
        index = 0
        for card in self.hand:
            print("[" + str(index) + "]", end="")
            card.print_string()
            index += 1
