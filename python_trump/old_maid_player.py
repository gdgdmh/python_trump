#!/usr/bin/env python
"""ババ抜きプレイヤークラス"""
from python_trump import trump_hand


class OldMaidPlayer:

    def __init__(self):
        """コンストラクタ"""
        self.name = "p"
        self.hand = trump_hand.TrumpHand()

    def add_hand(self, card):
        """カードを手札に加える"""
        self.hand.add(card)

    def play_hand(self, index):
        """カードを手札から出す(index指定)"""
        return self.hand.remove(index)

    def play_trump(self, card):
        """カードを手札からだす(カード指定)"""
        return self.hand.remove_trump(card)

    def get_pair(self):
        """ペアのカードを取得する"""
        pass

    def get_hand_size(self):
        """手札の枚数を取得する"""
        return self.hand.size()
