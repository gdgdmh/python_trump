#!/usr/bin/env python
"""ターンテストクラス"""
from python_trump import turn


def test_change_001():
    """ターン切り替え(デフォルト)"""
    t = turn.Turn(0, 4)
    t.change()
    assert t.get() == 1


def test_change_002():
    """ターン切り替え(初期ターンずらし)"""
    t = turn.Turn(1, 4)
    t.change()
    assert t.get() == 2


def test_change_003():
    """ターン切り替え(境界付近)"""
    t = turn.Turn(2, 4)
    t.change()
    assert t.get() == 3


def test_change_004():
    """ターン切り替え(一周)"""
    t = turn.Turn(3, 4)
    t.change()
    assert t.get() == 0


def test_change_005():
    """ターン切り替え(プレイヤー数変更)"""
    t = turn.Turn(0, 10)
    t.change()
    assert t.get() == 1


def test_change_006():
    """ターン切り替え(プレイヤー数変更一周)"""
    t = turn.Turn(9, 10)
    t.change()
    assert t.get() == 0


def test_reverse_001():
    """ターン切り替え(逆順デフォルト)"""
    t = turn.Turn(0, 4)
    t.reverse()
    assert t.get() == 3


def test_reverse_002():
    """ターン切り替え(逆順)"""
    t = turn.Turn(1, 4)
    t.reverse()
    assert t.get() == 0


def test_reverse_003():
    """ターン切り替え(逆順)"""
    t = turn.Turn(2, 4)
    t.reverse()
    assert t.get() == 1


def test_reverse_004():
    """ターン切り替え(逆順MAX)"""
    t = turn.Turn(3, 4)
    t.reverse()
    assert t.get() == 2


def test_reverse_005():
    """ターン切り替え(逆順プレイヤー数変更)"""
    t = turn.Turn(3, 9)
    t.reverse()
    assert t.get() == 2


def test_reverse_006():
    """ターン切り替え(逆順プレイヤー数変更一周)"""
    t = turn.Turn(0, 9)
    t.reverse()
    assert t.get() == 8


def test_set_001():
    """ターン設定"""
    t = turn.Turn(0, 4)
    t.set(0)
    assert t.get() == 0


def test_set_002():
    """ターン設定"""
    t = turn.Turn(0, 4)
    t.set(1)
    assert t.get() == 1


def test_set_003():
    """ターン設定"""
    t = turn.Turn(0, 4)
    t.set(2)
    assert t.get() == 2


def test_set_004():
    """ターン設定"""
    t = turn.Turn(0, 4)
    t.set(3)
    assert t.get() == 3


def test_set_005():
    """ターン設定"""
    t = turn.Turn(0, 7)
    t.set(0)
    assert t.get() == 0


def test_set_006():
    """ターン設定"""
    t = turn.Turn(0, 7)
    t.set(6)
    assert t.get() == 6


def test_get_001():
    """ターン取得"""
    t = turn.Turn(0, 4)
    assert t.get() == 0


def test_get_002():
    """ターン取得"""
    t = turn.Turn(0, 4)
    t.change()
    assert t.get() == 1


def test_get_003():
    """ターン取得"""
    t = turn.Turn(0, 4)
    t.reverse()
    assert t.get() == 3
