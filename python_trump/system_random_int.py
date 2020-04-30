#!/usr/bin/env python
"""整数乱数生成(システム使用)."""
import random
from python_trump import random_int


class SystemRandomInt(random_int.RandomInt):
    """整数乱数生成(システム使用)."""

    def get_range(self, min, max):
        """指定範囲で乱数を取得する."""
        return random.randint(min, max)
