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
