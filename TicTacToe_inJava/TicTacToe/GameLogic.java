public class GameLogic {
  // Using 2d character array to keep track of gameboard
  private char[][] gameGrid;
  private char currentSymbol; // Track current player's symbol

  // Constructor method to initialize the gameboard
  public GameLogic() {
    gameGrid = new char[3][3];
    currentSymbol = 'X'; // Set the first player's symbol as X
    initializeBoard();
  }

  // Method that Gamelogic uses to initialize the cells to '-' indicating they're empty
  private void initializeBoard() {
    for (int i = 0; i < 3; i++)
    for (int j = 0; j < 3; j++)
    gameGrid[i][j] = '-';
  }

  // Places current symbol at the specified (row, col) location. returns true if successful
  public boolean move(int row, int col) {
    if (row < 0 || row > 3 || col < 0 || col > 3 || gameGrid[row][col] != '-')
    return false; // false implies invalid move

    gameGrid[row][col] = currentSymbol;
    return true;
  }

  // Win logic for checking if any player wins
  public boolean checkWin() {
    boolean win = false;
    // Win logic for '---' rows
    for (int i = 0; i < 3; i++) {
      if (gameGrid[i][0] == currentSymbol && gameGrid[i][1] == currentSymbol && gameGrid[i][2] == currentSymbol) {
        return true; // Row win
      }
    }

    // Win logic for '|||' columns
    for (int i = 0; i < 3; i++) {
      if (gameGrid[0][i] == currentSymbol && gameGrid[1][i] == currentSymbol && gameGrid[2][i] == currentSymbol) {
        return true; // Column win
      }
    }

    // Win logic for '\' diagonal
    if (gameGrid[0][0] == currentSymbol && gameGrid[1][1] == currentSymbol && gameGrid[2][2] == currentSymbol) {
      return true;
    }

    // Win logic for '/' diagonal
    if (gameGrid[0][2] == currentSymbol && gameGrid[1][1] == currentSymbol && gameGrid[2][0] == currentSymbol) {
      return true;
    }

    // No win
    return false;
  }

  // If the board gets full and nobody wins then it's a draw
  public boolean isGameGridFull() {
    for (int i = 0; i < 3; i++)
    for (int j = 0; j < 3; j++)
    if (gameGrid[i][j] == '-')
      return false;
    return true;
  }

  // Allows the classes outside this class to get the current symbol
  public char getCurrentPlayer() {
    return currentSymbol;
  }

  // Switching the player after every turn
  public void switchPlayer() {
    currentSymbol = (currentSymbol == 'X') ? 'O' : 'X';
  }

  // Resetting the game after either win or draw is achieved
  public void resetGame() {
    initializeBoard();
    currentSymbol = 'X';
  }
}
