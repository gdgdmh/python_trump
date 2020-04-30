#!/usr/bin/env python
"""ババ抜きクラス."""
from python_trump import old_maid_player_cpu
from python_trump import trump_deck
from python_trump import trump_deal
from python_trump import turn
from python_trump import scene
from python_trump import result


class OldMaid:
    """ババ抜きクラス."""

    MIN_PLAYER = 2
    MAX_PLAYER = 26

    def __init__(self, player_count=4):
        """コンストラクタ."""
        # トランプデッキ
        self._deck = trump_deck.TrumpDeck()
        # 捨て札(トランプペアリスト)
        self._trash_list = []
        # プレイヤー
        if player_count < self.MIN_PLAYER or player_count > self.MAX_PLAYER:
            raise ValueError("set player_count >= 2 and player_count <= 26")
        self._players = []
        for _ in range(player_count):
            self._players.append(old_maid_player_cpu.OldMaidPlayerCpu())
        self._player_count = player_count
        # ターン
        self._game_turn = turn.Turn(0, player_count)
        # シーン
        self._game_scene = scene.Scene()
        # 結果
        self._game_result = result.Result()

    def initialize_game(self):
        """ゲームの初期化."""
        self._deck.set_one_joker_deck()
        self._deck.shuffle()
        self._trash_list.clear()
        for p in self._players:
            p.initialize_game()
        self._game_turn.set(0)
        self._game_scene.initialize_game()
        self._game_result.set_ended(False)
        self._game_result.set_win_player(0)

    def task(self):
        """ゲーム処理."""
        s = self._game_scene.get()
        if s == scene.Scene.INITIALIZE:
            self._task_initialize()
        elif s == scene.Scene.DEAL:
            self._task_deal()
        elif s == scene.Scene.DEAL_PLAY:
            self._task_deal_play()
        elif s == scene.Scene.START_SELECT_CARD:
            self._task_start_select_card()
        elif s == scene.Scene.SELECT_CARD:
            self._task_select_card()
        elif s == scene.Scene.PLAY_CARD:
            self._task_play_card()
        elif s == scene.Scene.CHANGE_TURN:
            self._task_change_turn()
        elif s == scene.Scene.END:
            self._task_end()

    def get_scene(self):
        """現在のシーンを取得."""
        return self._game_scene.get()

    def get_players(self):
        """プレイヤーの取得."""
        return self._players

    def _task_initialize(self):
        """初期化シーン."""
        self.initialize_game()
        self._game_scene.set(scene.Scene.DEAL)

    def _task_deal(self):
        """カード配布シーン."""
        deal = trump_deal.TrumpDeal()
        deal.deal(self._deck, self._players)
        self._game_scene.set(scene.Scene.DEAL_PLAY)

    def _task_deal_play(self):
        """カード配布後カード捨てシーン."""
        n = 0
        for p in self._players:
            pl = p.play_pair()
            if not pl:
                pass
            else:
                self._trash_list.extend(pl)
            if self._is_player_done(n):
                # すぐに上がる可能性がある
                self._proc_player_done(n)
            n += 1

        if self._is_playing_enable():
            self._game_scene.set(scene.Scene.START_SELECT_CARD)
        else:
            self._game_scene.set(scene.Scene.END)

    def _task_start_select_card(self):
        """カード選択開始シーン."""
        t = self._game_turn.get()
        b = self._game_turn.get_before_turn()
        self._players[t].event_turn_start(self._players[b].get_hand())
        self._game_scene.set(scene.Scene.SELECT_CARD)

    def _task_select_card(self):
        """カード選択シーン."""
        t = self._game_turn.get()
        b = self._game_turn.get_before_turn()
        r = self._players[t].event_turn_select(self._players[b].get_hand())
        if r is None:
            return
        ptrump = self._players[b].play_hand(r)
        self._players[t].add_hand(ptrump)
        self._game_scene.set(scene.Scene.PLAY_CARD)

    def _task_play_card(self):
        """カード捨てシーン."""
        t = self._game_turn.get()
        b = self._game_turn.get_before_turn()
        pl = self._players[t].play_pair()
        if not pl:
            pass
        else:
            self._trash_list.extend(pl)

        if self._is_player_done(t):
            self._proc_player_done(t)
        if self._is_player_done(b):
            self._proc_player_done(b)

        if self._is_playing_enable():
            self._game_scene.set(scene.Scene.CHANGE_TURN)
        else:
            self._game_scene.set(scene.Scene.END)

    def _task_change_turn(self):
        """ターン切り替えシーン."""
        self._game_turn.change()
        self._game_scene.set(scene.Scene.START_SELECT_CARD)

    def _task_end(self):
        """終了シーン."""
        pass

    def _proc_player_done(self, number):
        """プレイヤーが上がったときの処理."""
        assert self._players[number].get_hand_size() == 0
        if self._game_turn.get_exclusion_size() == 0:
            # first player done
            self._game_result.set_win_player(number)
        self._game_turn.exclusion(number)
        if self._game_turn.get_exclusion_size() == (self._player_count - 1):
            # last player done
            self._game_result.set_ended(True)

    def _is_player_done(self, number):
        """プレイヤーが上がったか."""
        if self._players[number].get_hand_size() == 0:
            return True
        return False

    def _is_playing_enable(self):
        """ゲームが続行可能か(2人以上居れば続行可能)."""
        cnt = 0
        for n in range(self._player_count):
            if not self._is_player_done(n):
                cnt += 1
        if cnt >= self.MIN_PLAYER:
            return True
        return False
