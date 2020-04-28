#!/usr/bin/env python
"""ババ抜きプレイヤーCPUクラス."""
from python_trump import old_maid_player


class OldMaidPlayerCpu(old_maid_player.OldMaidPlayer):
    """ババ抜きプレイヤーCPUクラス."""

    def __init__(self, player_name='p'):
        """コンストラクタ."""
        super(OldMaidPlayerCpu, self).__init__(player_name)

    def event_turn_start(self, trump_list):
        """手番開始."""
        pass

    def event_turn_select(self, trump_list):
        """手番カード選択."""
        return None
