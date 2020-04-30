#!/usr/bin/env python
"""ババ抜きテストクラス."""
from python_trump import old_maid
from python_trump import scene


def test_initialize_game_001():
    """ゲームの初期化."""
    om = old_maid.OldMaid(4)
    om.initialize_game()
    assert om.get_scene() == scene.Scene.INITIALIZE


def test_task_001():
    """ゲームのタスク(カード配布)."""
    om = old_maid.OldMaid(4)
    om.initialize_game()
    om.task()
    assert om.get_scene() == scene.Scene.DEAL


def test_task_002():
    """ゲームのタスク(初期化)."""
    pass


def test_get_scene_001():
    """シーン取得."""
    om = old_maid.OldMaid(4)
    om.initialize_game()
    assert om.get_scene() == scene.Scene.INITIALIZE


def test_get_players_001():
    """プレイヤーの取得."""
    om = old_maid.OldMaid(4)
    om.initialize_game()
    ps = om.get_players()
    assert len(ps) == 4
