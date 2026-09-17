import tkinter as tk

from ai import get_best_move
from game import Game


BACKGROUND = "#171717"
CARD = "#222222"
BUTTON = "#2d2d2d"
BUTTON_HOVER = "#3a3a3a"
TEXT = "#ffffff"
MUTED = "#a0a0a0"


class TicTacToeApp:
    def __init__(self, root):
        self.root = root
        self.game = Game()
        self.score = {"player": 0, "draw": 0, "ai": 0}
        self.player_turn = True

        self.root.title("Tic-Tac-Toe AI")
        self.root.geometry("500x650")
        self.root.resizable(False, False)
        self.root.configure(bg=BACKGROUND)

        self.title = tk.Label(
            self.root,
            text="TIC-TAC-TOE",
            font=("Arial", 28, "bold"),
            bg=BACKGROUND,
            fg=TEXT,
        )
        self.title.pack(pady=(35, 5))

        self.subtitle = tk.Label(
            self.root,
            text="You are X  •  AI is O",
            font=("Arial", 12),
            bg=BACKGROUND,
            fg=MUTED,
        )
        self.subtitle.pack(pady=(0, 20))

        self.score_frame = tk.Frame(self.root, bg=BACKGROUND)
        self.score_frame.pack(pady=5)

        self.player_score = tk.Label(
            self.score_frame,
            text="YOU\n0",
            font=("Arial", 15, "bold"),
            bg=CARD,
            fg=TEXT,
            width=8,
            height=3,
        )
        self.player_score.pack(side="left", padx=8)

        self.draw_score = tk.Label(
            self.score_frame,
            text="DRAW\n0",
            font=("Arial", 15, "bold"),
            bg=CARD,
            fg=TEXT,
            width=8,
            height=3,
        )
        self.draw_score.pack(side="left", padx=8)

        self.ai_score = tk.Label(
            self.score_frame,
            text="AI\n0",
            font=("Arial", 15, "bold"),
            bg=CARD,
            fg=TEXT,
            width=8,
            height=3,
        )
        self.ai_score.pack(side="left", padx=8)

        self.status = tk.Label(
            self.root,
            text="Your turn",
            font=("Arial", 14, "bold"),
            bg=BACKGROUND,
            fg=TEXT,
        )
        self.status.pack(pady=20)

        self.board_frame = tk.Frame(self.root, bg=BACKGROUND)
        self.board_frame.pack()

        self.buttons = []
        for row in range(3):
            for column in range(3):
                position = row * 3 + column
                button = tk.Button(
                    self.board_frame,
                    text="",
                    font=("Arial", 32, "bold"),
                    width=4,
                    height=2,
                    bg=BUTTON,
                    fg=TEXT,
                    activebackground=BUTTON_HOVER,
                    activeforeground=TEXT,
                    relief="flat",
                    bd=0,
                    highlightthickness=0,
                    command=lambda p=position: self.handle_player_move(p),
                )
                button.grid(row=row, column=column, padx=5, pady=5)
                self.buttons.append(button)

        self.new_game = tk.Button(
            self.root,
            text="NEW GAME",
            font=("Arial", 13, "bold"),
            bg=TEXT,
            fg=BACKGROUND,
            activebackground="#dddddd",
            activeforeground=BACKGROUND,
            relief="flat",
            bd=0,
            padx=25,
            pady=12,
            command=self.reset_board,
        )
        self.new_game.pack(pady=30)

        self.update_scores()
        self.reset_board()

    def update_scores(self):
        self.player_score.config(text=f"YOU\n{self.score['player']}")
        self.draw_score.config(text=f"DRAW\n{self.score['draw']}")
        self.ai_score.config(text=f"AI\n{self.score['ai']}")

    def update_board(self):
        for position, button in enumerate(self.buttons):
            value = self.game.board[position]
            button.config(text=value if value != " " else "")

            if self.game.game_over or value != " ":
                button.config(state="disabled")
            elif self.player_turn:
                button.config(state="normal")
            else:
                button.config(state="disabled")

    def handle_player_move(self, position):
        if not self.player_turn or self.game.game_over:
            return
        if not self.game.make_move(position, "X"):
            return

        self.update_board()
        if self.game.game_over:
            self.finish_round()
            return

        self.player_turn = False
        self.status.config(text="AI is thinking...")
        self.update_board()
        self.root.after(350, self.ai_turn)

    def ai_turn(self):
        if self.game.game_over:
            return

        move = get_best_move(self.game.board)
        if move is None:
            return

        self.game.make_move(move, "O")
        self.update_board()

        if self.game.game_over:
            self.finish_round()
            return

        self.player_turn = True
        self.status.config(text="Your turn")
        self.update_board()

    def finish_round(self):
        if self.game.winner == "X":
            self.score["player"] += 1
            self.status.config(text="You win!")
        elif self.game.winner == "O":
            self.score["ai"] += 1
            self.status.config(text="AI wins!")
        else:
            self.score["draw"] += 1
            self.status.config(text="It's a draw!")

        self.player_turn = False
        self.update_scores()
        self.update_board()

    def reset_board(self):
        self.game.reset()
        self.player_turn = True
        self.status.config(text="Your turn")
        self.update_scores()
        self.update_board()


def main():
    root = tk.Tk()
    TicTacToeApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
