import unittest
import logic


class TestLogic(unittest.TestCase):

    def test_get_winner(self):
        board = [
            ["X", None, "O"],
            [None, "X", None],
            [None, "O", "X"],
        ]
        empty_board = [
        [" "," "," "],
        [" "," "," "],
        [" "," "," "],]
        logic.print_board(board) # Checking if the print function is working properly
        self.assertEqual(logic.make_empty_board(),empty_board) # Should always return empty board
        self.assertEqual(logic.get_winner(board,"X"), "X") # In the given board the X wins
        self.assertEqual(logic.get_winner(board,"O"), None) # In the given board O is not the winner so it should return none


if __name__ == '__main__':
    unittest.main()