#!/usr/bin/env python
"""ババ抜きゲームクラス."""
from python_trump import old_maid
from python_trump import scene


class OldMaidGame:
    """ババ抜きゲームクラス."""

    SCENE_INIT = 0
    SCENE_START_PLAY = 1
    SCENE_SELECT = 2
    SCENE_PLAY = 3
    SCENE_END = 4

    def __init__(self):
        """コンストラクタ."""
        self._om = old_maid.OldMaid(2)
        self._scene = self.SCENE_INIT

    def task(self):
        """メイン処理."""
        if self._scene == self.SCENE_INIT:
            self._task_init()
        elif self._scene == self.SCENE_START_PLAY:
            self._task_start_play()
        elif self._scene == self.SCENE_SELECT:
            self._task_select()
        elif self._scene == self.SCENE_PLAY:
            self._task_play()
        elif self._scene == self.SCENE_END:
            self._task_end()

    def get_scene(self):
        """シーンの取得."""
        return self._scene

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
            self._scene = self.SCENE_START_PLAY

    def _task_start_play(self):
        """手番開始."""
        if self._om.get_scene() == scene.Scene.START_SELECT_CARD:
            print("START_SELECT_CARD")
            self._om.task()
            self._scene = self.SCENE_SELECT
        else:
            assert(0)

    def _task_select(self):
        """手札選択."""
        if self._om.get_scene() == scene.Scene.SELECT_CARD:
            self._om.task()
        if self._om.get_scene() == scene.Scene.PLAY_CARD:
            self._om.task()
            self._scene = scene.Scene.PLAY_CARD
        if self._om.get_scene() == scene.Scene.END:
            self._scene = self.SCENE_END

    def _task_play(self):
        """手札捨て."""
        if self._om.get_scene() == scene.Scene.PLAY_CARD:
            pass

    def _task_end(self):
        """ゲーム終了."""
        pass
