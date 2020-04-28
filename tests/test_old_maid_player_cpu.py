#!/usr/bin/env python
"""ババ抜きプレイヤーテストクラス."""
from python_trump import old_maid_player_cpu
from python_trump import old_maid_player
from python_trump import trump


def test_event_turn_start_001():
    """手番開始."""
    m = old_maid_player_cpu.OldMaidPlayerCpu()
    c = old_maid_player.OldMaidPlayer()
    c.add_hand(trump.Trump(trump.Trump.SPADE, 1))
    c.add_hand(trump.Trump(trump.Trump.SPADE, 2))
    c.add_hand(trump.Trump(trump.Trump.SPADE, 3))
    c.add_hand(trump.Trump(trump.Trump.SPADE, 4))
    m.event_turn_start(c.get_hand())


def test_event_turn_select_001():
    """手番カード選択."""
    m = old_maid_player_cpu.OldMaidPlayerCpu()
    c = old_maid_player.OldMaidPlayer()
    c.add_hand(trump.Trump(trump.Trump.SPADE, 1))
    c.add_hand(trump.Trump(trump.Trump.SPADE, 2))
    c.add_hand(trump.Trump(trump.Trump.SPADE, 3))
    c.add_hand(trump.Trump(trump.Trump.SPADE, 4))
    m.event_turn_select(c.get_hand())
