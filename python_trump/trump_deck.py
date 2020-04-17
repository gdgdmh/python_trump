#!/usr/bin/env python
"""トランプデッキクラス"""
from python_trump import trump


class TrumpDeck:

    def __init__(self):
        """コンストラクタ"""
        self.deck = []
        pass

    def set_full_deck(self):
        """デッキに54枚(ジョーカー2枚)のカードを設定する"""
        self.deck.append(trump.Trump(trump.Trump.JOKER, 1))
        self.deck.append(trump.Trump(trump.Trump.JOKER, 2))
        for n in range(13):
            self.deck.append(trump.Trump(trump.Trump.SPADE, n + 1))
            self.deck.append(trump.Trump(trump.Trump.HEART, n + 1))
            self.deck.append(trump.Trump(trump.Trump.DIAMOND, n + 1))
            self.deck.append(trump.Trump(trump.Trump.CLUB, n + 1))

    def set_one_joker_deck(self):
        """デッキに53枚(ジョーカー1枚)のカードを設定する"""
        self.deck.append(trump.Trump(trump.Trump.JOKER, 1))
        for n in range(13):
            self.deck.append(trump.Trump(trump.Trump.SPADE, n + 1))
            self.deck.append(trump.Trump(trump.Trump.HEART, n + 1))
            self.deck.append(trump.Trump(trump.Trump.DIAMOND, n + 1))
            self.deck.append(trump.Trump(trump.Trump.CLUB, n + 1))

    def set_no_joker_deck(self):
        """デッキに52枚のカードを設定する"""
        for n in range(13):
            self.deck.append(trump.Trump(trump.Trump.SPADE, n + 1))
            self.deck.append(trump.Trump(trump.Trump.HEART, n + 1))
            self.deck.append(trump.Trump(trump.Trump.DIAMOND, n + 1))
            self.deck.append(trump.Trump(trump.Trump.CLUB, n + 1))

    def index(self, index):
        """デッキの要素を返す"""
        return self.deck[index]

    def size(self):
        """デッキのサイズを返す"""
        return len(self.deck)

    def print(self):
        """デッキの中身を表示する"""
        index = 0
        for card in self.deck:
            print("[" + str(index) + "]", end="")
            card.print_string()
            index += 1

    def shuffle(self):
        """デッキをシャッフルする"""
        pass

    def draw(self):
        """カードを引く"""
        pass
