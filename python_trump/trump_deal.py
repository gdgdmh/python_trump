#!/usr/bin/env python
"""トランプ配布クラス."""


class TrumpDeal:
    """トランプ配布クラス."""

    def __init__(self):
        """コンストラクタ."""
        pass

    def deal(self, deck, old_maid_players):
        """プレイヤーに対してトランプを配布する."""
        if deck.size() <= 0:
            return
        if len(old_maid_players) == 0:
            return

        player_index = 0
        player_max = len(old_maid_players)
        while deck.size() > 0:
            # deal
            t = deck.draw()
            old_maid_players[player_index].add_hand(t)
            # player_index update
            player_index += 1
            if player_index >= player_max:
                player_index = 0
