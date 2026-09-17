from game import Game
from ai import get_best_move


def test_game_detects_winner():
    game = Game()
    game.board = ["X", "X", "X", " ", " ", " ", " ", " ", " "]
    assert game.check_winner() == "X"


def test_game_tracks_draw():
    game = Game()
    game.board = ["X", "O", "X", "X", "O", "O", "O", "X", "X"]
    assert game.is_draw() is True


def test_ai_prefers_winning_move():
    board = ["O", "O", " ", "X", "X", " ", " ", " ", " "]
    assert get_best_move(board) == 2
