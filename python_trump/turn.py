#!/usr/bin/env python
"""ターンクラス"""


class Turn:

    def __init__(self, first_turn=0, max_player=4):
        """コンストラクタ"""
        self.turn = first_turn
        self.max_player = max_player

    def change(self):
        """順繰りにターン切り替え"""
        self.turn += 1
        if self.turn >= self.max_player:
            self.turn = 0

    def reverse(self):
        """逆順にターン切り替え"""
        self.turn -= 1
        if self.turn < 0:
            self.turn = self.max_player - 1

    def get(self):
        """ターンを取得する"""
        return self.turn
