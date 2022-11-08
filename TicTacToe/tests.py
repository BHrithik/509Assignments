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
        logic.print_board(board)
        self.assertEqual(logic.make_empty_board(),empty_board)
        self.assertEqual(logic.get_winner(board,"X"), "X")
        self.assertNotEqual(logic.get_winner(board,"O"), "O")
    # TODO: Test all functions from logic.py!


if __name__ == '__main__':
    unittest.main()