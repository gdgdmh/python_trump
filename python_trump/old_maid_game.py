#!/usr/bin/env python
"""ババ抜きゲームクラス."""
from python_trump import old_maid
from python_trump import scene


class OldMaidGame:
    """ババ抜きゲームクラス."""

    SCENE_INIT = 0
    SCENE_START_SELECT = 1
    SCENE_SELECT = 2
    SCENE_PLAY = 3
    SCENE_CHANGE_TURN = 4
    SCENE_END = 5

    PLAYER_COUNT = 4

    def __init__(self):
        """コンストラクタ."""
        self._om = old_maid.OldMaid(self.PLAYER_COUNT)
        self._scene = self.SCENE_INIT

    def task(self):
        """メイン処理."""
        if self._scene == self.SCENE_INIT:
            self._task_init()
        elif self._scene == self.SCENE_START_SELECT:
            self._task_start_play()
        elif self._scene == self.SCENE_SELECT:
            self._task_select()
        elif self._scene == self.SCENE_PLAY:
            self._task_play()
        elif self._scene == self.SCENE_CHANGE_TURN:
            self._task_change_turn()
        elif self._scene == self.SCENE_END:
            self._task_end()

    def get_scene(self):
        """シーンの取得."""
        return self._scene

    def get_players(self):
        """プレイヤーの手札の取得."""
        return self._om.get_players()

    def _task_init(self):
        """初期化."""
        if self._om.get_scene() == scene.Scene.INITIALIZE:
            print("INITIALIZE")
            self._om.task()
        if self._om.get_scene() == scene.Scene.DEAL:
            print("DEAL")
            self._om.task()
        if self._om.get_scene() == scene.Scene.DEAL_PLAY:
            print("DEAL_PLAY")
            self._om.task()
            if self._om.get_scene() == scene.Scene.END:
                print("-> END")
                self._scene = self.SCENE_END
        if self._om.get_scene() == scene.Scene.START_SELECT_CARD:
            print("START_SELECT_CARD ->")
            self._scene = self.SCENE_START_SELECT

    def _task_start_play(self):
        """手番開始."""
        if self._om.get_scene() == scene.Scene.START_SELECT_CARD:
            print("START_SELECT_CARD")
            self._print_players()
            self._om.task()
            self._scene = self.SCENE_SELECT
        else:
            assert(0)

    def _task_select(self):
        """手札選択."""
        if self._om.get_scene() == scene.Scene.SELECT_CARD:
            print("SELECT_CARD")
            self._om.task()
        if self._om.get_scene() == scene.Scene.PLAY_CARD:
            print("-> PLAY_CARD")
            self._scene = self.SCENE_PLAY
        if self._om.get_scene() == scene.Scene.END:
            print("-> END")
            self._print_players()
            self._scene = self.SCENE_END

    def _task_play(self):
        """手札捨て."""
        print("PLAY_CARD")
        if self._om.get_scene() == scene.Scene.PLAY_CARD:
            self._om.task()
        if self._om.get_scene() == scene.Scene.END:
            self._print_players()
            self._scene = self.SCENE_END
        if self._om.get_scene() == scene.Scene.CHANGE_TURN:
            self._scene = self.SCENE_CHANGE_TURN

    def _task_change_turn(self):
        """ターン切り替え."""
        print("CHANGE_TURN")
        if self._om.get_scene() == scene.Scene.CHANGE_TURN:
            self._om.task()
        if self._om.get_scene() == scene.Scene.START_SELECT_CARD:
            self._scene = self.SCENE_START_SELECT

    def _task_end(self):
        """ゲーム終了."""
        print("END")

    def _print_players(self):
        """プレイヤーの表示."""
        ps = self._om.get_players()
        for n in range(self.PLAYER_COUNT):
            print("---player" + str(n) + "---")
            ps[n].print_hand()
