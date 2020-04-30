#!/usr/bin/env python
"""エントリーポイント."""
from python_trump import old_maid_game


def main():
    """エントリーポイント."""
    print('main')
    og = old_maid_game.OldMaidGame()
    while og.get_scene() is not old_maid_game.OldMaidGame.SCENE_END:
        og.task()
    print("old_maid_game end")


if __name__ == '__main__':
    main()
