#!/usr/bin/env python
"""シーンクラス."""


class Scene:
    """シーンクラス."""

    INITIALIZE = 0
    DEAL = 1
    SELECT_CARD = 2
    PLAY_CARD = 3
    CHANGE_TURN = 4
    END = 5

    def __init__(self):
        """コンストラクタ."""
        self._scene = Scene.INITIALIZE

    def initialize_game(self):
        """ゲームの初期化."""
        self._scene = Scene.INITIALIZE

    def set(self, set_scene):
        """シーンを設定する."""
        if not set_scene >= Scene.INITIALIZE or not set_scene <= Scene.END:
            raise ValueError("set scene error")
        self._scene = set_scene

    def get(self):
        """ターンを取得する."""
        return self._scene
