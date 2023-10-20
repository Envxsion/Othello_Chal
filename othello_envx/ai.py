import random

def ai_move(board, player_color):
    valid_moves = []
    for row in range(8):
        for col in range(8):
            if board.is_valid_move(row, col, player_color):
                valid_moves.append((row, col))
    
    if valid_moves:
        return random.choice(valid_moves)
    else:
        return None  
