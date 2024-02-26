import chess
import random

def main():
    board = chess.Board()
    print_board(board)
    while not board.is_game_over():
        if board.turn == chess.WHITE:
            player_move = input("Enter your move (in algebraic notation): ")
            try:
                board.push_san(player_move)
            except ValueError:
                print("Invalid move, try again.")
                continue
        else:
            computer_move = get_computer_move(board)
            print("Computer's Move:", computer_move)
            board.push(computer_move)
        
        print_board(board)
        
    result = board.result()
    if result == "1-0":
        print("White wins!")
    elif result == "0-1":
        print("Black wins!")
    else:
        print("It's a draw!")

def print_board(board):
    print("\n" + board.__str__() + "\n")

def get_computer_move(board):
    # Choose difficulty level
    difficulty = input("Choose difficulty level (easy, medium, hard): ")
    if difficulty == "easy":
        return get_random_move(board)
    elif difficulty == "medium":
        return get_medium_move(board)
    elif difficulty == "hard":
        return get_hard_move(board)
    else:
        print("Invalid difficulty level. Please choose again.")
        return get_computer_move(board)

def get_random_move(board):
    legal_moves = list(board.legal_moves)
    return random.choice(legal_moves)

def get_medium_move(board):
    # For medium difficulty, just choose a random move
    return get_random_move(board)

def get_hard_move(board):
    # For hard difficulty, use minimax with alpha-beta pruning
    _, best_move = minimax(board, 3, True, -float('inf'), float('inf'))
    return best_move

def minimax(board, depth, maximizing_player, alpha, beta):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board), None

    if maximizing_player:
        max_eval = -float('inf')
        best_move = None
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, False, alpha, beta)[0]
            board.pop()
            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = float('inf')
        best_move = None
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, True, alpha, beta)[0]
            board.pop()
            if eval < min_eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, best_move

def evaluate_board(board):
    # Simple evaluation function: just count material
    evaluation = 0
    for piece in board.piece_map().values():
        if piece.color == chess.WHITE:
            evaluation += piece_value(piece.piece_type)
        else:
            evaluation -= piece_value(piece.piece_type)
    return evaluation

def piece_value(piece_type):
    values = {chess.PAWN: 1, chess.KNIGHT: 3, chess.BISHOP: 3, chess.ROOK: 5, chess.QUEEN: 9}
    return values.get(piece_type, 0)

if __name__ == "__main__":
    main()

