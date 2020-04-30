#!/usr/bin/env python
"""整数乱数生成テストクラス."""
from python_trump import system_random_int


def test_get_range_001():
    """指定範囲の乱数を取得する(何度か実行して指定範囲チェック)."""
    s = system_random_int.SystemRandomInt()
    for _ in range(10):
        r = s.get_range(1, 2)
        assert r == 1 or r == 2


def test_get_range_002():
    """指定範囲の乱数を取得(3桁、何度か実行して指定範囲チェック)."""
    s = system_random_int.SystemRandomInt()
    for _ in range(10):
        r = s.get_range(1, 100)
        assert r >= 1 and r <= 100


def test_get_range_003():
    """指定範囲の乱数を取得(負の値、何度か実行して指定範囲チェック)."""
    s = system_random_int.SystemRandomInt()
    for _ in range(10):
        r = s.get_range(-20, -10)
        assert r >= -20 and r <= -10


def test_get_range_004():
    """指定範囲の乱数を取得(同一数値、何度か実行して指定範囲チェック)."""
    s = system_random_int.SystemRandomInt()
    for _ in range(10):
        r = s.get_range(1, 1)
        assert r == 1
