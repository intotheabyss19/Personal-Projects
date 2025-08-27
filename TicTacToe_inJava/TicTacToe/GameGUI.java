import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

// Main class to manage the GUI of the game
public class GameGUI {
  private JFrame gameFrame;
  private JButton[][] Cells;
  private JLabel statusLabel;
  private GameLogic Game;

  // Constructor to initialize the game and setup the GUI
  public GameGUI() {
    Game = new GameLogic();
    createGUI();
  }

  // Method to configure the GUI components
  private void createGUI() {
    // Create the main window
    gameFrame = new JFrame("TIC-TAC-TOE");
    // Allows the program to terminate on closing the instance
    gameFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    // Setting up size and position of the GUI window
    gameFrame.setSize(600, 600);
    gameFrame.setLocationRelativeTo(null);
    // Optional to turn of resizeability of the window
    gameFrame.setResizable(false);

    // background color
    gameFrame.getContentPane().setBackground(new Color(200, 200, 200));

    JPanel gamePanel = new JPanel(new GridLayout(3, 3));
    Cells = new JButton[3][3];

    for (int i = 0; i < 3; i++) {
      for (int j = 0; j < 3; j++) {
        // Setting up each cell of the Tic Tac Toe Board
        Cells[i][j] = new JButton("");
        Cells[i][j].setFont(new Font("Arial", Font.BOLD, 60));
        Cells[i][j].addActionListener(new ButtonClickListener(i, j));
        Cells[i][j].setBackground(new Color(50, 50, 100));
        Cells[i][j].setForeground(new Color(0, 200, 200));
        Cells[i][j].setBorder(BorderFactory.createLineBorder(new Color(0, 0, 0), 1));
        // Finally add the cell onto the panel
        gamePanel.add(Cells[i][j]);
      }
    }

    // Add a Label for indicating player's turn
    statusLabel = new JLabel("Player X's turn");

    // Add Both game panels and status label to the frame
    gameFrame.add(gamePanel, BorderLayout.CENTER);
    gameFrame.add(statusLabel, BorderLayout.SOUTH);

    // Make the frame visible when ready
    gameFrame.setVisible(true);
  }

  // Setting up actions for clicking the tic tac toe buttons
  private class ButtonClickListener implements ActionListener {
    private int row, col;

    public ButtonClickListener(int row, int col) {
      this.row = row;
      this.col = col;
    }

    @Override
    public void actionPerformed(ActionEvent e) {
      if (Game.move(row, col)) {
        Cells[row][col].setText(String.valueOf(Game.getCurrentPlayer()));
        if (Game.checkWin()) {
          statusLabel.setText("Player " + Game.getCurrentPlayer() + " wins!");
          showPopup("Player " + Game.getCurrentPlayer() + " wins!");
        } else if (Game.isGameGridFull()) {
          statusLabel.setText("It's a draw!");
          showPopup("Draw!!!");
        } else {
          Game.switchPlayer();
          statusLabel.setText("Player " + Game.getCurrentPlayer() + "'s turn");
        }
      }
    }
  }

  private void showPopup(String message) {
    int response = JOptionPane.showOptionDialog(gameFrame, message + "\nWould you like to play again?", "Game Over",
      JOptionPane.YES_NO_OPTION, JOptionPane.INFORMATION_MESSAGE, null, null, null);
    if (response == JOptionPane.YES_OPTION) {
      Game.resetGame();
      resetBoard();
      statusLabel.setText("Player X's turn");
    } else {
      System.exit(0);
    }
  }

  private void resetBoard() {
    for (int i = 0; i < 3; i++) {
      for (int j = 0; j < 3; j++) {
        Cells[i][j].setText("");
      }
    }
  }
} 