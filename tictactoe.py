class TicTacToe:
  BLANK_SQUARE = '_'
  DEFAULT_MIN_BOARD_SIZE = 3
  MAX_BOARD_SIZE = 10

  def __init__(self):
    self.board_size = self.get_board_size()
    self.board = [self.BLANK_SQUARE] * (self.board_size ** 2)
    self.current_player = 'X'

  def get_board_size(self):
    while True:
      try:
        board_size_input = input(f'Enter the size of the board ({self.DEFAULT_MIN_BOARD_SIZE} for a minimum {self.DEFAULT_MIN_BOARD_SIZE}x{self.DEFAULT_MIN_BOARD_SIZE} board and {self.MAX_BOARD_SIZE} for a maximum {self.MAX_BOARD_SIZE}x{self.MAX_BOARD_SIZE} board), or press Enter for the default {self.DEFAULT_MIN_BOARD_SIZE}x{self.DEFAULT_MIN_BOARD_SIZE} board: ')
        if not board_size_input:
          return self.DEFAULT_MIN_BOARD_SIZE

        board_size = int(board_size_input)

        if self.DEFAULT_MIN_BOARD_SIZE <= board_size <= self.MAX_BOARD_SIZE:
          return board_size
        else:
          print(f'Board size must be between {self.DEFAULT_MIN_BOARD_SIZE} and {self.MAX_BOARD_SIZE}.')
      except ValueError:
          print('Invalid input. Please enter a valid board size.')

  def print_board(self):
    print()
    for row in range(self.board_size):
      for col in range(self.board_size):
        print(self.board[row * self.board_size + col], end='  ')
      print()
    print()

  def make_move(self, position):
    if not (1 <= position <= self.board_size ** 2):
      print('Invalid move!')
      return

    user_position = position - 1

    if self.board[user_position] != self.BLANK_SQUARE:
      print('Invalid move!')
      return

    self.board[user_position] = self.current_player
    winner = self.check_winner()

    if winner:
      self.print_board()
      print(f'{winner} wins!')
      return

    self.current_player = '0' if self.current_player == 'X' else 'X'

  def check_winner(self):
    for i in range(self.board_size):
      row = [self.board[i * self.board_size + j] for j in range(self.board_size)]
      col = [self.board[j * self.board_size + i] for j in range(self.board_size)]

      if all(cell == self.current_player for cell in row) or all(cell == self.current_player for cell in col):
        return self.current_player

      diag1 = [self.board[i * self.board_size + i] for i in range(self.board_size)]
      diag2 = [self.board[i * self.board_size + (self.board_size - 1 - i)] for i in range(self.board_size)]

      if all(cell == self.current_player for cell in diag1) or all(cell == self.current_player for cell in diag2):
        return self.current_player

    return None

  def check_draw(self):
    return self.BLANK_SQUARE not in self.board

  def reset(self):
    self.board = [self.BLANK_SQUARE] * (self.board_size ** 2)
    self.current_player = 'X'

  def initialize_game(self):
    while True:
      self.reset()
      while self.check_winner() is None and not self.check_draw():
          self.print_board()
          position_input = input(f'Enter position (1 - {self.board_size ** 2}), "exit" to quit: ')
          
          if position_input.lower() == 'exit':
            return

          try:
            position = int(position_input)
            self.make_move(position)
          except ValueError:
            print('Invalid input. Please enter a valid position or type "exit" to quit.')

      self.print_board()
      winner = self.check_winner()

      if winner:
        print(f'{winner} wins!')
      else:
        print('It\'s a draw!')

      play_again = input('Play again? (yes/no): ').lower()

      if play_again != 'yes':
        return

      print("Thanks for playing Tic-Tac-Toe!")

if __name__ == "__main__":
  game = TicTacToe()
  game.initialize_game()
  game.print_board()
