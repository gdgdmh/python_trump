#!/usr/bin/env python
"""結果クラス"""


class Result:

    def __init__(self):
        """コンストラクタ"""
        self.ended = False
        self.win_player = 0

    def set_ended(self, is_ended):
        """終局したか設定"""
        self.ended = is_ended

    def is_ended(self):
        """終局したか"""
        return self.ended

    def set_win_player(self, win_player_number):
        """勝ちプレイヤーの設定"""
        self.win_player = win_player_number

    def get_win_player(self):
        """勝ちプレイヤーの取得"""
        return self.win_player
