#!/usr/bin/env python
"""トランプペアクラス."""
from python_trump import trump


class TrumpPair:
    """トランプペアクラス."""

    def __init__(self, trump1, trump2):
        """コンストラクタ."""
        if str(type(trump1)) != trump.Trump.TYPE_STRING:
            raise ValueError("trump1 not trump!")
        if str(type(trump2)) != trump.Trump.TYPE_STRING:
            raise ValueError("trump2 not trump!")
        self._pair1 = trump1
        self._pair2 = trump2

    def get(self):
        """トランプのペアを取得."""
        return (self._pair1, self._pair2)
