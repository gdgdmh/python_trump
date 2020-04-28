#!/usr/bin/env python
"""トランプデッキクラス."""
import random
from python_trump import trump


class TrumpDeck:
    """トランプデッキクラス."""

    def __init__(self):
        """コンストラクタ."""
        self.deck = []
        pass

    def set_full_deck(self):
        """デッキに54枚(ジョーカー2枚)のカードを設定する."""
        self.deck.append(trump.Trump(trump.Trump.JOKER, 1))
        self.deck.append(trump.Trump(trump.Trump.JOKER, 2))
        self.set_no_joker_deck()

    def set_one_joker_deck(self):
        """デッキに53枚(ジョーカー1枚)のカードを設定する."""
        self.deck.append(trump.Trump(trump.Trump.JOKER, 1))
        self.set_no_joker_deck()

    def set_no_joker_deck(self):
        """デッキに52枚のカードを設定する."""
        for n in range(13):
            self.deck.append(trump.Trump(trump.Trump.SPADE, n + 1))
            self.deck.append(trump.Trump(trump.Trump.HEART, n + 1))
            self.deck.append(trump.Trump(trump.Trump.DIAMOND, n + 1))
            self.deck.append(trump.Trump(trump.Trump.CLUB, n + 1))

    def put_top(self, card):
        """カードをデッキの一番上に置く."""
        if str(type(card)) != trump.Trump.TYPE_STRING:
            raise ValueError("card not trump!")
        self.deck.append(card)

    def draw(self):
        """カードを引く."""
        return self.deck.pop()

    def index(self, index):
        """デッキの要素を返す."""
        return self.deck[index]

    def size(self):
        """デッキのサイズを返す."""
        return len(self.deck)

    def print(self):
        """デッキの中身を表示する."""
        index = 0
        for card in self.deck:
            print("[" + str(index) + "]", end="")
            card.print_string()
            index += 1

    def shuffle(self, num=3):
        """デッキをシャッフルする."""
        if num <= 0:
            raise ValueError("num > 0")
        for _ in range(num):
            self._shuffle()

    def _shuffle(self):
        """デッキをシャッフルする(Fisher-Yates shuffle)."""
        size = len(self.deck)
        for i in range(size, 0, -1):
            i1 = i - 1
            i2 = random.randint(0, i - 1)
            self.deck[i1], self.deck[i2] = self.deck[i2], self.deck[i1]
