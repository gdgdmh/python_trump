#!/usr/bin/env python
"""ババ抜きプレイヤークラス"""
from python_trump import trump_hand
from python_trump import trump_pair
from python_trump import trump


class OldMaidPlayer:

    def __init__(self):
        """コンストラクタ"""
        self.name = "p"
        self.hand = trump_hand.TrumpHand()

    def add_hand(self, card):
        """カードを手札に加える"""
        self.hand.add(card)

    def play_hand(self, index):
        """カードを手札から出す(index指定)"""
        return self.hand.remove(index)

    def play_trump(self, card):
        """カードを手札からだす(カード指定)"""
        return self.hand.remove_trump(card)

    def get_pair(self):
        """ペアのカードを取得する"""
        if self.hand.size() <= 1:
            return None
        trump_list = self.hand.copy_list()
        pair_list = []
        while True:
            pair = self._get_pair_hand(trump_list)
            if not pair:
                # None or []
                break
            else:
                p = trump_pair.TrumpPair(pair[0], pair[1])
                pair_list.append(p)
                trump_list.remove(pair[0])
                trump_list.remove(pair[1])
        return pair_list

    def get_hand_size(self):
        """手札の枚数を取得する"""
        return self.hand.size()

    def _get_pair_hand(self, trump_list):
        """手札からペアとなるものを返す"""
        size = len(trump_list)
        for i in range(size):
            for j in range(size):
                ic = trump_list[i]
                jc = trump_list[j]
                if ic is jc:
                    continue
                if ic.get_number() == jc.get_number() and \
                        not ic.is_joker() and not jc.is_joker():
                    # 2枚ともジョーカーでないならnumber一致でペア
                    return (ic, jc)
        return None
