import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Player:

    def __init__(self):
        self.name = ""
        self.symbol = ""

    def choose_name(self):
        while True:
            name = input("Enter your name (letters only): ")
            if name.isalpha():
                self.name = name
                break
            else:
                print("Invalid name. Please use letters only.")

    def choose_symbol(self):
        while True:
            symbol = input(f"{self.name}, enter your symbol (single letter): ")
            if symbol.isalpha() and len(symbol) == 1:
                self.symbol = symbol.upper()
                break
            else:
                print("Invalid symbol. Please choose a single letter only.")


class Menu:
    def display_main_menu(self):
        print("Welcome to my X-O game:")
        print("1. Start game")
        print("2. Quit game")

        while True:
            choice = input("Enter your choice (1 or 2): ")
            if choice == '1' or choice == '2':
                return int(choice)
            else:
                print("Invalid Input")

    def display_endgame_menu(self):
        menu_text = """
        Game Over!
        1. Restart game
        2. Quit game
        Enter your choice (1 or 2): 
        """
        while True:
            choice = input(menu_text)
            if choice == '1' or choice == '2':
                return int(choice)
            else:
                print("Invalid Input")


class Board:
    def __init__(self):
        self.board = [str(i) for i in range(1, 10)]

    def display_board(self):
        for i in range(0, 9, 3):
            print("|".join(self.board[i:i + 3]))
            if i < 6:
                print("-" * 5)

    def update_board(self, choice, symbol):
        if self.is_valid(choice):
            self.board[choice - 1] = symbol
            return True
        return False

    def is_valid(self, choice):
        return self.board[choice - 1].isdigit()

    def reset_board(self):
        self.board = [str(i) for i in range(1, 10)]


class Game:
    def __init__(self):
        self.players = [Player(), Player()]
        self.board = Board()
        self.menu = Menu()
        self.current_player_index = 0

    def start_game(self):
        choice = self.menu.display_main_menu()
        if choice == 1:
            self.setup_players()
            self.play_game()
        else:
            self.quit_game()

    def setup_players(self):
        for index, player in enumerate(self.players, start=1):
            print(f"Player {index}, Enter your details:")
            player.choose_name()
            player.choose_symbol()

    def play_game(self):
        while True:
            self.play_turn()
            if self.check_win() or self.check_draw():
                self.switch_turn()
                if self.check_win():
                    winner_name = self.players[self.current_player_index].name
                    print(f"Congratulations! {winner_name} wins!")
                else:
                    print("It's a draw!")
                choice = self.menu.display_endgame_menu()
                if choice == 1:
                    self.restart_game()
                else:
                    self.quit_game()
                    break

    def play_turn(self):
        player = self.players[self.current_player_index]
        print(f"{player.name}'s turn ({player.symbol})")
        while True:
            try:
                cell_choice = int(input("choose a cell (1-9) :"))
                if 1 <= cell_choice <= 9 and self.board.update_board(cell_choice, player.symbol):
                    break
                else:
                    print("Invalid move , try again")
            except ValueError:
                print("please Enter a number between 1 and 9")
        self.switch_turn()

    def switch_turn(self):
        self.current_player_index = 1 - self.current_player_index

    def check_win(self):
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]  # diagonals
        ]

        for combo in win_combinations:
            if self.board.board[combo[0]] == self.board.board[combo[1]] == self.board.board[combo[2]]:
                return True
        return False

    def check_draw(self):
        return all(cell.isdigit() for cell in self.board.board)

    def restart_game(self):
        self.board.reset_board()
        self.current_player_index = 0
        self.play_game()

    def quit_game(self):
        print("Thank you for playing!")

game = Game()
game.start_game()
