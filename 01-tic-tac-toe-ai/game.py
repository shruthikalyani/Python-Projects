class Game:
    WINNING_LINES = (
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    )

    def __init__(self):
        self.reset()

    def reset(self):
        self.board = [" "] * 9
        self.winner = None
        self.draw = False
        self.game_over = False

    def available_moves(self):
        return [index for index, cell in enumerate(self.board) if cell == " "]

    def make_move(self, index, symbol):
        if self.game_over or not 0 <= index < 9:
            return False
        if self.board[index] != " ":
            return False

        self.board[index] = symbol
        self.winner = self.check_winner()

        if self.winner is not None:
            self.game_over = True
            return True

        if self.is_draw():
            self.draw = True
            self.game_over = True
            return True

        return True

    def check_winner(self, board=None):
        if board is None:
            board = self.board

        for a, b, c in self.WINNING_LINES:
            if board[a] != " " and board[a] == board[b] == board[c]:
                return board[a]
        return None

    def is_draw(self):
        return self.check_winner() is None and all(cell != " " for cell in self.board)
