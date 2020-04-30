#!/usr/bin/env python
"""トランプ手札クラス."""
import random
from python_trump import trump


class TrumpHand:
    """トランプ手札クラス."""

    def __init__(self):
        """コンストラクタ."""
        self._hand = []

    def add(self, card):
        """トランプを手札に加える."""
        if str(type(card)) != trump.Trump.TYPE_STRING:
            raise ValueError("card not trump!")
        self._hand.append(card)

    def remove(self, index):
        """手札からトランプを除く(index指定)."""
        card = self._hand[index]
        self._hand.remove(card)
        return card

    def remove_trump(self, card):
        """手札からトランプを除く."""
        self._hand.remove(card)
        return card

    def clear(self):
        """手札を全て削除."""
        self._hand.clear()
        pass

    def sort(self):
        """手札をソートする."""
        self._hand.sort(key=trump.Trump.get_sort_number)

    def shuffle(self):
        """手札をシャッフルする."""
        self._shuffle(self._hand)

    def index(self, index):
        """手札からカードを取得する."""
        return self._hand[index]

    def size(self):
        """手札の枚数を取得する."""
        return len(self._hand)

    def is_empty(self):
        """手札が空か."""
        return len(self._hand) == 0

    def copy_list(self):
        """リストのコピー."""
        return self._hand.copy()

    def print(self):
        """手札の表示."""
        index = 0
        for card in self._hand:
            print("[" + str(index) + "]", end="")
            card.print_string()
            index += 1

    def _shuffle(self, trumps):
        """手札をシャッフルする."""
        size = len(trumps)
        for i in range(size, 0, -1):
            i1 = i - 1
            i2 = random.randint(0, i - 1)
            trumps[i1], trumps[i2] = trumps[i2], trumps[i1]
