class OthelloBoard:
    def __init__(self):
        # 8x8 grid
        self.board = [['.' for _ in range(8)] for _ in range(8)]
        # Default start pos
        self.board[3][3] = self.board[4][4] = 'W'
        self.board[3][4] = self.board[4][3] = 'B'

    def print_board(self):
        for row in self.board:
            print(" ".join(row))
        print()

    def is_valid_move(self, row, col, player_color):
        if self.board[row][col] != '.':
            return False
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            found_opponent = False
            while 0 <= r < 8 and 0 <= c < 8:
                if self.board[r][c] == '.':
                    break
                if self.board[r][c] == player_color:
                    if found_opponent:
                        return True
                    break
                else:
                    found_opponent = True
                r, c = r + dr, c + dc
        return False

    def make_move(self, row, col, player_color):
        if not self.is_valid_move(row, col, player_color):
            return False

        self.board[row][col] = player_color
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

        for dr, dc in directions:
            r, c = row + dr, col + dc #modify values to check specified direction
            found_opponent = False
            flip_list = []
            while 0 <= r < 8 and 0 <= c < 8: #check 8x8 bounds
                if self.board[r][c] == '.':
                    break
                if self.board[r][c] == player_color:
                    if found_opponent:
                        for flip_row, flip_col in flip_list:
                            self.board[flip_row][flip_col] = player_color
                    break
                else:
                    found_opponent = True
                    flip_list.append((r, c))
                r, c = r + dr, c + dc

        return True

    def get_winner(self):
        black_count = sum(row.count('B') for row in self.board)
        white_count = sum(row.count('W') for row in self.board)
        if black_count > white_count:
            return 'Black'
        elif white_count > black_count:
            return 'White'
        else:
            return 'Tie'

    def is_game_over(self):
        for row in self.board:
            if '.' in row:
                return False
        return True
