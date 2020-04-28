#!/usr/bin/env python
"""ターンクラス."""


class Turn:
    """ターンクラス."""

    def __init__(self, first_turn=0, max_player=4):
        """コンストラクタ."""
        self._turn = first_turn
        self._max_player = max_player

    def change(self):
        """順繰りにターン切り替え."""
        self._turn += 1
        if self._turn >= self._max_player:
            self._turn = 0

    def reverse(self):
        """逆順にターン切り替え."""
        self._turn -= 1
        if self._turn < 0:
            self._turn = self._max_player - 1

    def set(self, set_turn):
        """ターンを強制的に設定する."""
        self._turn = set_turn

    def get(self):
        """ターンを取得する."""
        return self._turn
