#!/usr/bin/env python
"""整数乱数生成インターフェース."""
from abc import ABCMeta, abstractmethod


class RandomInt(metaclass=ABCMeta):
    """整数乱数生成インターフェースクラス."""

    @abstractmethod
    def get_range(self, min, max):
        """指定範囲で乱数を取得する."""
        return None
