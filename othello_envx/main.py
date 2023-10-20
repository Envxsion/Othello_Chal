import os
import time
from board import OthelloBoard
from colorama import Fore, Back, init, Style
from screens import intro_screen, end_screen
from ai import ai_move  

init(autoreset=True)  # Initialize colorama

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(board, valid_moves, black_count, white_count, timer):
    clear_screen()
    # Print a border around the UI
    print(Back.GREEN + Fore.RED + Style.BRIGHT + ' ' * 6 + ' Othello 8x8 by Envxsion ' + ' ' * 6)
    print(Back.BLUE + '   A  B  C  D  E  F  G  H  ')
    for i, row in enumerate(board):
        print(Fore.BLUE + str(i + 1), end=' ')
        for j, cell in enumerate(row):
            if cell == 'B':
                print(Back.BLACK + Fore.WHITE + ' B ', end='')
            elif cell == 'W':
                print(Back.WHITE + Fore.BLACK + ' W ', end='')
            elif (i, j) in valid_moves:
                print(Back.RED + Fore.WHITE + ' . ', end='')  # Valid moves in red
            else:
                print(Back.LIGHTWHITE_EX + Fore.LIGHTWHITE_EX + ' . ', end='')
        print(Back.CYAN + ' ', end=' ')
        print()
    print()
    print(Fore.RED + f'Black Count: {black_count}  White Count: {white_count}')
    print(Fore.YELLOW + f'Timer: {timer} seconds')

def main():
    intro_screen()
    board = OthelloBoard()
    timer = 0
    start_time = time.time()
    black_count = 2
    white_count = 2

    # Ask the user whether they want to play against human or AI
    player_vs_ai = input("Do you want to play against the AI? (yes/no): ").strip().lower()
    if player_vs_ai == 'yes':
        player_turn = 'B'  # Player goes first
    else:
        player_turn = 'B'  # Player vs Player mode

    while not board.game_over():
        valid_moves = []

        for row in range(8):
            for col in range(8):
                if board.is_valid_move(row, col, player_turn):
                    valid_moves.append((row, col))

        elapsed_time = int(time.time() - start_time)
        print_board(board.board, valid_moves, black_count, white_count, elapsed_time)
        print(f"Player {player_turn}'s turn")

        if not valid_moves:
            print(Fore.RED + Style.BRIGHT + "No valid moves. Pass.")
            time.sleep(2)
            player_turn = 'B' if player_turn == 'W' else 'W'
            continue

        if player_turn == 'B':
            move = input("Enter your move (e.g., 'D3'): ").strip().upper()
            
            if len(move) != 2 or not ('A' <= move[0] <= 'H') or not ('1' <= move[1] <= '8'):
                print(Fore.RED + Style.BRIGHT + "Invalid input. Please enter a valid move.")
                time.sleep(2)
                continue

            col = ord(move[0]) - ord('A')
            row = ord(move[1]) - ord('1')
        else:
            if player_vs_ai == 'yes':
                # AI's turn
                ai_move_result = ai_move(board, player_turn)
                if ai_move_result:
                    row, col = ai_move_result
                    print(f"AI plays: {chr(col + ord('A'))}{row + 1}")
                else:
                    print(Fore.RED + "AI passes. No valid moves for the AI.")
                    time.sleep(2)
            else:
                # Player 2's turn in Player vs Player mode
                move = input("Enter your move (e.g., 'D3'): ").strip().upper()
                
                if len(move) != 2 or not ('A' <= move[0] <= 'H') or not ('1' <= move[1] <= '8'):
                    print(Fore.RED + Style.BRIGHT + "Invalid input. Please enter a valid move.")
                    time.sleep(2)
                    continue

                col = ord(move[0]) - ord('A')
                row = ord(move[1]) - ord('1')

        if (row, col) in valid_moves:
            board.make_move(row, col, player_turn)
            player_turn = 'B' if player_turn == 'W' else 'W'

            # Update the disc count
            black_count = sum(row.count('B') for row in board.board)
            white_count = sum(row.count('W') for row in board.board)
        else:
            print(Fore.RED + Style.BRIGHT + "Invalid move. Try again.")
            time.sleep(2)

        timer = elapsed_time

    winner = board.get_winner()
    print_board(board.board, [], black_count, white_count, timer)
    end_screen(winner, black_count, white_count)

if __name__ == '__main__':
    main()
