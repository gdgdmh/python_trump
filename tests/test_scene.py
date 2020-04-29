#!/usr/bin/env python
"""シーンテストクラス."""
from python_trump import scene


def test_initialize_game_001():
    """ゲーム初期化."""
    s = scene.Scene()
    s.initialize_game()
    assert s.get() == scene.Scene.INITIALIZE


def test_set_001():
    """シーン設定."""
    s = scene.Scene()
    s.set(scene.Scene.INITIALIZE)
    assert s.get() == scene.Scene.INITIALIZE


def test_set_002():
    """シーン設定."""
    s = scene.Scene()
    s.set(scene.Scene.DEAL)
    assert s.get() == scene.Scene.DEAL


def test_set_003():
    """シーン設定."""
    s = scene.Scene()
    s.set(scene.Scene.START_SELECT_CARD)
    assert s.get() == scene.Scene.START_SELECT_CARD


def test_set_004():
    """シーン設定."""
    s = scene.Scene()
    s.set(scene.Scene.SELECT_CARD)
    assert s.get() == scene.Scene.SELECT_CARD


def test_set_005():
    """シーン設定."""
    s = scene.Scene()
    s.set(scene.Scene.PLAY_CARD)
    assert s.get() == scene.Scene.PLAY_CARD


def test_set_006():
    """シーン設定."""
    s = scene.Scene()
    s.set(scene.Scene.CHANGE_TURN)
    assert s.get() == scene.Scene.CHANGE_TURN


def test_set_007():
    """シーン設定."""
    s = scene.Scene()
    s.set(scene.Scene.END)
    assert s.get() == scene.Scene.END


def test_set_008():
    """シーン設定."""
    s = scene.Scene()
    try:
        s.set(999)
    except ValueError:
        pass
    else:
        assert False


def test_get_001():
    """シーン取得."""
    s = scene.Scene()
    assert s.get() == scene.Scene.INITIALIZE
