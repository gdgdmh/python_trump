#!/usr/bin/env python
"""結果 テストクラス"""
from python_trump import result


def test_set_ended_001():
    """終局設定(True)"""
    r = result.Result()
    assert not r.is_ended()
    r.set_ended(True)
    assert r.is_ended()


def test_set_ended_002():
    """終局設定(False)"""
    r = result.Result()
    assert not r.is_ended()
    r.set_ended(False)
    assert not r.is_ended()


def test_is_ended_001():
    """終局しているか(True)"""
    r = result.Result()
    r.set_ended(True)
    assert r.is_ended()


def test_is_ended_002():
    """終局しているか(False)"""
    r = result.Result()
    r.set_ended(False)
    assert not r.is_ended()


def test_set_win_player_001():
    """勝利プレイヤーの設定"""
    r = result.Result()
    r.set_win_player(0)
    assert r.get_win_player() == 0


def test_set_win_player_002():
    """勝利プレイヤーの設定"""
    r = result.Result()
    r.set_win_player(9)
    assert r.get_win_player() == 9


def test_get_win_player_001():
    """勝利プレイヤーの取得"""
    r = result.Result()
    r.set_win_player(10)
    assert r.get_win_player() == 10


def test_get_win_player_002():
    """勝利プレイヤーの設定"""
    r = result.Result()
    r.set_win_player(999)
    assert r.get_win_player() == 999
