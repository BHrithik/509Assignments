import unittest
from logic import TicTacToe
from easy import Easy


class TestLogic(unittest.TestCase):

    def test_get_winner(self):
        difficulty = Easy()
        testGame = TicTacToe(difficulty)
        testGame.print_board() # Checking if the print function is working properly
        newBoard = [[" "," "," "],
                    [" "," "," "],
                    [" "," "," "],]
        #board = testGame.board()
        self.assertEqual(testGame.board,newBoard) # Should always return empty board
        testGame.board = [["X", None, "O"],
                        [None, "X", None],
                        [None, "O", "X"],]
        self.assertEqual(testGame.get_winner("X"), "X") # In the given board the X wins
        testGame.board = [["X", None, "O"],
                        ["O", "O", "O"],
                        ["X", "O", "X"],]
        self.assertEqual(testGame.get_winner("O"), "O") # In the given board O is the winner so it should return O
        testGame.board = [["X","X", "O"],
                        ["O", "O", "X"],
                        ["X", "O", "X"],]
        self.assertEqual(testGame.get_winner("O"),None) # Checking when no one is a winner

if __name__ == '__main__':
    unittest.main()
