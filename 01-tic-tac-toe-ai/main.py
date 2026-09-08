import math
import tkinter as tk
from tkinter import messagebox


PLAYER = "X"
AI = "O"

board = [""] * 9
game_over = False
ai_job = None

player_score = 0
ai_score = 0
draw_score = 0

BG = "#0f1117"
CARD = "#171a23"
BUTTON = "#202530"
TEXT = "#f5f7fa"
SECONDARY = "#8b93a7"
ACCENT = "#7c5cff"

winning_combinations = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
]


def check_winner(current_board):
    for first, second, third in winning_combinations:
        if (
            current_board[first]
            and current_board[first] == current_board[second] == current_board[third]
        ):
            return current_board[first]

    if "" not in current_board:
        return "draw"

    return None


def minimax(current_board, maximizing):
    result = check_winner(current_board)

    if result == AI:
        return 1
    if result == PLAYER:
        return -1
    if result == "draw":
        return 0

    if maximizing:
        best_score = -math.inf
        for index in range(9):
            if current_board[index] == "":
                current_board[index] = AI
                score = minimax(current_board, False)
                current_board[index] = ""
                best_score = max(best_score, score)
        return best_score

    best_score = math.inf
    for index in range(9):
        if current_board[index] == "":
            current_board[index] = PLAYER
            score = minimax(current_board, True)
            current_board[index] = ""
            best_score = min(best_score, score)
    return best_score


def get_ai_move():
    best_score = -math.inf
    best_move = None

    for index in range(9):
        if board[index] == "":
            board[index] = AI
            score = minimax(board, False)
            board[index] = ""
            if score > best_score:
                best_score = score
                best_move = index

    return best_move


root = tk.Tk()
root.title("Tic-Tac-Toe AI")
root.geometry("500x650")
root.resizable(False, False)
root.configure(bg=BG)

title = tk.Label(root, text="TIC-TAC-TOE", font=("Arial", 28, "bold"), bg=BG, fg=TEXT)
title.pack(pady=(30, 2))

subtitle = tk.Label(
    root,
    text="Play against an unbeatable AI",
    font=("Arial", 11),
    bg=BG,
    fg=SECONDARY,
)
subtitle.pack()

score_frame = tk.Frame(root, bg=CARD, padx=20, pady=12)
score_frame.pack(pady=25, padx=35, fill="x")

player_label = tk.Label(score_frame, text="YOU\n0", font=("Arial", 13, "bold"), bg=CARD, fg=TEXT)
player_label.pack(side="left", expand=True)

draw_label = tk.Label(score_frame, text="DRAW\n0", font=("Arial", 13, "bold"), bg=CARD, fg=SECONDARY)
draw_label.pack(side="left", expand=True)

ai_label = tk.Label(score_frame, text="AI\n0", font=("Arial", 13, "bold"), bg=CARD, fg=TEXT)
ai_label.pack(side="left", expand=True)

status_label = tk.Label(
    root,
    text="Your turn - you are X",
    font=("Arial", 12),
    bg=BG,
    fg=TEXT,
)
status_label.pack(pady=(0, 15))

board_frame = tk.Frame(root, bg=BG)
board_frame.pack()
buttons = []


def create_board():
    for index in range(9):
        button = tk.Button(
            board_frame,
            text="",
            font=("Arial", 32, "bold"),
            width=4,
            height=2,
            bg=BUTTON,
            fg=TEXT,
            activebackground=ACCENT,
            activeforeground=TEXT,
            relief="flat",
            borderwidth=0,
            command=lambda move=index: player_move(move),
        )
        button.grid(row=index // 3, column=index % 3, padx=5, pady=5)
        buttons.append(button)


def update_score():
    player_label.config(text=f"YOU\n{player_score}")
    draw_label.config(text=f"DRAW\n{draw_score}")
    ai_label.config(text=f"AI\n{ai_score}")


def highlight_winner():
    for combination in winning_combinations:
        first, second, third = combination
        if board[first] and board[first] == board[second] == board[third]:
            for index in combination:
                buttons[index].config(bg=ACCENT)
            return


def finish_game(result):
    global game_over, player_score, ai_score, draw_score

    game_over = True
    if result == PLAYER:
        player_score += 1
        status_label.config(text="You won!")
        message = "You won!"
    elif result == AI:
        ai_score += 1
        status_label.config(text="AI wins!")
        message = "The AI wins!"
    else:
        draw_score += 1
        status_label.config(text="It's a draw!")
        message = "It's a draw!"

    update_score()
    highlight_winner()
    messagebox.showinfo("Game Over", message)


def player_move(index):
    global ai_job

    if game_over or board[index] != "":
        return

    board[index] = PLAYER
    buttons[index].config(text=PLAYER, fg=ACCENT)

    result = check_winner(board)
    if result:
        finish_game(result)
        return

    for button in buttons:
        button.config(state="disabled")
    status_label.config(text="AI is thinking...")
    ai_job = root.after(350, ai_turn)


def ai_turn():
    global ai_job

    ai_job = None
    if game_over:
        return

    move = get_ai_move()
    if move is not None:
        board[move] = AI
        buttons[move].config(text=AI, fg=TEXT)

    result = check_winner(board)
    if result:
        finish_game(result)
        return

    for index, button in enumerate(buttons):
        if board[index] == "":
            button.config(state="normal")
    status_label.config(text="Your turn - you are X")


def new_game():
    global board, game_over, ai_job

    if ai_job is not None:
        root.after_cancel(ai_job)
        ai_job = None

    board = [""] * 9
    game_over = False
    for button in buttons:
        button.config(text="", state="normal", bg=BUTTON, fg=TEXT)
    status_label.config(text="Your turn - you are X")


create_board()

new_game_button = tk.Button(
    root,
    text="NEW GAME",
    font=("Arial", 12, "bold"),
    bg=ACCENT,
    fg=TEXT,
    activebackground=ACCENT,
    activeforeground=TEXT,
    relief="flat",
    borderwidth=0,
    padx=30,
    pady=12,
    command=new_game,
)
new_game_button.pack(pady=30)

footer = tk.Label(root, text="Powered by Minimax AI", font=("Arial", 9), bg=BG, fg=SECONDARY)
footer.pack()

new_game()
root.mainloop()
