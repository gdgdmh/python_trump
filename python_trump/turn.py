#!/usr/bin/env python
"""ターンクラス."""


class Turn:
    """ターンクラス."""

    def __init__(self, first_turn=0, max_player=4):
        """コンストラクタ."""
        self._turn = first_turn
        self._max_player = max_player
        self._exclusions = []

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

    def exclusion(self, number):
        """指定番号をターンから除外する."""
        if number < 0 or number >= self._max_player:
            raise ValueError("range error")
        if self._exclusions.count(number) > 0:
            raise ValueError("dumplicate error")
        self._exclusions.append(number)
        self._exclusions.sort()

    def reset_exclusion(self):
        """除外リストをクリアする."""
        self._exclusions.clear()

    def get_exclusion_size(self):
        """除外リストのサイズを取得."""
        return len(self._exclusions)

    def _get_next_turn(self, turn_number):
        """次のターンの人の番号を取得する."""
        if len(self._exclusions) > self._max_player - 1:
            # 全てのプレイヤーが除外リストに登録済みならそのまま返す
            return turn_number
        t = turn_number
        while (True):
            t = t + 1
            if t >= self._max_player:
                t = 0
            if self._exclusions.count(t) == 0:
                break
        return t

    def _get_before_turn(self, turn_number):
        """前のターンの人の番号を取得する."""
        if len(self._exclusions) > self._max_player - 1:
            # 全てのプレイヤーが除外リストに登録済みならそのまま返す
            return turn_number
        t = turn_number
        while (True):
            t = t - 1
            if t < 0:
                t = self._max_player - 1
            if self._exclusions.count(t) == 0:
                break
        return t
