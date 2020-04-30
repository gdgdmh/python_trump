"""ババ抜きゲームテストクラス."""
from python_trump import old_maid_game


def test_task_001():
    """メイン処理."""
    og = old_maid_game.OldMaidGame()
    og.task()


def test_get_scene_001():
    """シーンの取得."""
    og = old_maid_game.OldMaidGame()
    assert og.get_scene() == old_maid_game.OldMaidGame.SCENE_INIT


def test_get_players_001():
    """プレイヤーの取得."""
    og = old_maid_game.OldMaidGame()
    ps = og.get_players()
    assert len(ps) == old_maid_game.OldMaidGame.PLAYER_COUNT
