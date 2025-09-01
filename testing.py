import unittest
from unittest.mock import patch
import number_guessing_game  # Import your game file


class TestNumberGuessingGame(unittest.TestCase):

    @patch("builtins.input", side_effect=["easy", "5", "7", "10"])
    def test_correct_guess(self, mock_input):
        """Test if the game correctly detects the right guess."""
        with patch("builtins.print") as mock_print:
            number_guessing_game.random_number = 10  # Set the random number
            number_guessing_game.calculate(10, 10)  # Simulate playing

            mock_print.assert_any_call("you had 10 lives left")  # Check win condition

    @patch("builtins.input", side_effect=["hard", "2", "3", "4", "5", "6"])
    def test_out_of_attempts(self, mock_input):
        """Test if the game correctly handles running out of attempts."""
        with patch("builtins.print") as mock_print:
            number_guessing_game.random_number = 10  # Set a high number
            number_guessing_game.calculate(10, 5)

            mock_print.assert_any_call("you have 0 lives left")
            mock_print.assert_any_call(number_guessing_game.art.logo3)  # Losing logo

    @patch("builtins.input", side_effect=["demon", "2"])
    def test_demon_mode_losing(self, mock_input):
        """Test if the game immediately ends when losing in demon mode."""
        with patch("builtins.print") as mock_print:
            number_guessing_game.random_number = 10
            number_guessing_game.calculate(10, 1)

            mock_print.assert_any_call("you have 0 lives left")

    @patch("builtins.input", side_effect=["hard", "hello", "5", "10"])
    def test_invalid_input_handling(self, mock_input):
        """Test if invalid input is properly handled."""
        with patch("builtins.print") as mock_print:
            number_guessing_game.random_number = 10
            number_guessing_game.calculate(10, 5)

            mock_print.assert_any_call("Invalid input! Please enter a number.")


if __name__ == "__main__":
    unittest.main()
