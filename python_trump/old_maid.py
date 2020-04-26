#!/usr/bin/env python
"""ババ抜きクラス"""
from python_trump import old_maid_player
from python_trump import trump_deck


class OldMaid:

    MIN_PLAYER = 2
    MAX_PLAYER = 26

    def __init__(self, player_count=4):
        """コンストラクタ"""
        # トランプデッキ
        self.deck = trump_deck.TrumpDeck()
        # 捨て札(トランプペアリスト)
        self.trash_list = []
        # プレイヤー
        if player_count < self.MIN_PLAYER or player_count > self.MAX_PLAYER:
            raise ValueError("card not trump!")

        self.players = []
        for _ in range(player_count):
            self.players.append(old_maid_player.OldMaidPlayer())
        self.player_count = player_count
        # ターン
        # 結果
