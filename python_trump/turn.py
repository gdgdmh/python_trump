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
        self._turn = self._get_next_turn(self._turn)

    def reverse(self):
        """逆順にターン切り替え."""
        self._turn = self._get_before_turn(self._turn)

    def set(self, set_turn):
        """ターンを強制的に設定する."""
        self._turn = set_turn

    def get(self):
        """ターンを取得する."""
        return self._turn

    def get_before_turn(self):
        """前のターンの人を取得する."""
        return self._get_before_turn(self._turn)

    def _get_next_turn(self, turn_number):
        """次のターンの人の番号を取得する."""
        t = turn_number + 1
        if t >= self._max_player:
            t = 0
        return t

    def _get_before_turn(self, turn_number):
        """前のターンの人の番号を取得する."""
        t = turn_number - 1
        if t < 0:
            t = self._max_player - 1
        return t
