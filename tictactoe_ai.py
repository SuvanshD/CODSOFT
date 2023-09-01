class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'

    def print_board(self):
        print(f"{self.board[0]} | {self.board[1]} | {self.board[2]}")
        print("--+---+--")
        print(f"{self.board[3]} | {self.board[4]} | {self.board[5]}")
        print("--+---+--")
        print(f"{self.board[6]} | {self.board[7]} | {self.board[8]}")

    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            self.current_player = 'X' if self.current_player == 'O' else 'O'
            return True
        return False

    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
            (0, 4, 8), (2, 4, 6)  # Diagonals
        ]

        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                return self.board[combo[0]]
        return None

    def is_board_full(self):
        return all(cell != ' ' for cell in self.board)

    def minimax(self, depth, is_maximizing):
        if self.check_winner() == 'X':
            return -10 + depth
        elif self.check_winner() == 'O':
            return 10 - depth
        elif self.is_board_full():
            return 0

        if is_maximizing:
            max_eval = -float('inf')
            for i in range(9):
                if self.board[i] == ' ':
                    self.board[i] = 'O'
                    eval = self.minimax(depth + 1, False)
                    self.board[i] = ' '
                    max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for i in range(9):
                if self.board[i] == ' ':
                    self.board[i] = 'X'
                    eval = self.minimax(depth + 1, True)
                    self.board[i] = ' '
                    min_eval = min(min_eval, eval)
            return min_eval

    def find_best_move(self):
        best_eval = -float('inf')
        best_move = -1
        for i in range(9):
            if self.board[i] == ' ':
                self.board[i] = 'O'
                eval = self.minimax(0, False)
                self.board[i] = ' '
                if eval > best_eval:
                    best_eval = eval
                    best_move = i
        return best_move


if __name__ == "__main__":
    game = TicTacToe()
    while True:
        game.print_board()
        if not game.is_board_full():
            player_move = int(input("Enter your move (0-8): "))
            if game.make_move(player_move):
                if game.check_winner():
                    game.print_board()
                    print("You win!")
                    break
                if game.is_board_full():
                    game.print_board()
                    print("It's a draw!")
                    break

                ai_move = game.find_best_move()
                game.make_move(ai_move)
                if game.check_winner():
                    game.print_board()
                    print("AI wins!")
                    break
        else:
            game.print_board()
            print("It's a draw!")
            break
