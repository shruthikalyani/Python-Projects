import math


def get_best_move(board):
    best_score = -math.inf
    best_move = None

    for index in range(9):
        if board[index] == " ":
            board[index] = "O"
            score = minimax(board, False)
            board[index] = " "

            if score > best_score:
                best_score = score
                best_move = index

    return best_move


def minimax(board, maximizing):
    result = get_result(board)

    if result == "O":
        return 1
    if result == "X":
        return -1
    if result == "draw":
        return 0

    if maximizing:
        best_score = -math.inf
        for index in range(9):
            if board[index] == " ":
                board[index] = "O"
                score = minimax(board, False)
                board[index] = " "
                best_score = max(best_score, score)
        return best_score

    best_score = math.inf
    for index in range(9):
        if board[index] == " ":
            board[index] = "X"
            score = minimax(board, True)
            board[index] = " "
            best_score = min(best_score, score)
    return best_score


def get_result(board):
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

    for a, b, c in winning_combinations:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]

    if " " not in board:
        return "draw"

    return None
