from tictactoe_ai import TicTacToe


def play_game():
    game = TicTacToe()

    print("Welcome to Tic-Tac-Toe AI!")
    print("You are 'X', and the AI is 'O'.")

    while True:
        game.print_board()

        if not game.is_board_full():
            player_move = int(input("Enter your move (0-8): "))
            if game.make_move(player_move):
                if game.check_winner() == 'X':
                    game.print_board()
                    print("Congratulations! You win!")
                    break
                if game.is_board_full():
                    game.print_board()
                    print("It's a draw!")
                    break

                ai_move = game.find_best_move()
                game.make_move(ai_move)
                if game.check_winner() == 'O':
                    game.print_board()
                    print("AI wins! Better luck next time.")
                    break
        else:
            game.print_board()
            print("It's a draw!")
            break


if __name__ == "__main__":
    play_game()
