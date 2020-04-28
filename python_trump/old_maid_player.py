#!/usr/bin/env python
"""ババ抜きプレイヤークラス."""
from python_trump import trump_hand
from python_trump import trump_pair


class OldMaidPlayer:
    """ババ抜きプレイヤークラス."""

    def __init__(self, player_name='p'):
        """コンストラクタ."""
        self._name = player_name
        self._hand = trump_hand.TrumpHand()

    def get_name(self):
        """名前の取得."""
        return self._name

    def initialize_game(self):
        """ゲーム開始のための初期化."""
        self._hand.clear()

    def event_turn_start(self, trump_list):
        """手番開始."""
        pass

    def event_turn_select(self, trump_list):
        """手番カード選択."""
        return None

    def add_hand(self, card):
        """カードを手札に加える."""
        self._hand.add(card)

    def play_hand(self, index):
        """カードを手札から出す(index指定)."""
        return self._hand.remove(index)

    def play_trump(self, trump):
        """カードを手札からだす(カード指定)."""
        return self._hand.remove_trump(trump)

    def play_pair(self):
        """ペアカードを出す."""
        # ペアカードを手札から出す
        pair_list = self.get_pair()
        for p in pair_list:
            self.play_trump(p.get()[0])
            self.play_trump(p.get()[1])
        return pair_list

    def get_pair(self):
        """ペアのカードを取得する."""
        if self._hand.size() <= 1:
            return None
        trump_list = self._hand.copy_list()
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
        """手札の枚数を取得する."""
        return self._hand.size()

    def get_hand(self):
        """手札を取得する."""
        return self._hand.copy_list()

    def _get_pair_hand(self, trump_list):
        """手札からペアとなるものを返す."""
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
