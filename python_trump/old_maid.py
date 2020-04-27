#!/usr/bin/env python
"""ババ抜きクラス"""
from python_trump import old_maid_player
from python_trump import trump_deck
from python_trump import turn
from python_trump import result


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
            raise ValueError("set player_count >= 2 and player_count <= 26")
        self.players = []
        for _ in range(player_count):
            self.players.append(old_maid_player.OldMaidPlayer())
        self.player_count = player_count
        # ターン
        self.game_turn = turn.Turn(0, player_count)
        # 結果
        self.game_result = result.Result()

    def initialize_game(self):
        """ゲームの初期化"""
        self.deck.set_one_joker_deck()
        self.trash_list.clear()
        for p in self.players:
            p.initialize_game()
        self.game_turn.set(0)
        self.game_result.set_ended(False)
        self.game_result.set_win_player(0)

    def task(self):
        """ゲーム処理"""
        pass
