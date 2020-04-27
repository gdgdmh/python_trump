#!/usr/bin/env python
"""ババ抜きテストクラス"""
from python_trump import old_maid
from python_trump import scene


def test_task_001():
    """ゲームのタスク"""
    om = old_maid.OldMaid(4)
    om.initialize_game()
    assert om.get_scene() == scene.Scene.INITIALIZE
    om.task()


def test_get_scene_001():
    """シーン取得"""
    om = old_maid.OldMaid(4)
    om.initialize_game()
    assert om.get_scene() == scene.Scene.INITIALIZE
