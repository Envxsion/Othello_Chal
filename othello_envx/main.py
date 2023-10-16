from board import OthelloBoard
from colorama import Fore, Back, Style, init

init(autoreset=True)  # Initialize colorama

def print_board(board):
    # Display the current state of the board with colors
    print(Back.BLUE + '   A  B  C  D  E  F  G  H ', end='\n')
    for i, row in enumerate(board):
        print(Fore.BLUE + str(i + 1), end=' ')
        for cell in row:
            if cell == 'B':
                print(Back.BLACK + Fore.WHITE + ' B ', end='')
            elif cell == 'W':
                print(Back.WHITE + Fore.BLACK + ' W ', end='')
            else:
                print(Back.GREEN + Fore.GREEN + ' . ', end='')
        print()
    print()


def main():
    board = OthelloBoard()
    player_turn = 'B'  

    while not board.is_game_over():
        print_board(board.board)
        print(f"Player {player_turn}'s turn")
        move = input("Enter your move (e.g., 'D3'): ").strip().upper()

        if len(move) != 2 or not ('A' <= move[0] <= 'H') or not ('1' <= move[1] <= '8'):
            print("Invalid input. Please enter a valid move.")
            continue

        col = ord(move[0]) - ord('A')
        row = ord(move[1]) - ord('1')

        if board.is_valid_move(row, col, player_turn):
            board.make_move(row, col, player_turn)
            player_turn = 'B' if player_turn == 'W' else 'W'
        else:
            print("Invalid move. Try again.")

    winner = board.get_winner()
    print_board(board.board)

    if winner == 'Tie':
        print("It's a tie!")
    else:
        print(f"Player {winner} wins!")

if __name__ == '__main__':
    main()
