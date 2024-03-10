"""Test module for the Bowling Kata"""

# Standard Library

# 3rd-party Library
import pytest

# Project Library
from game.bowling import BowlingGame, BowlingFrame

class TestBowlingFrame:
    def test_constructor_bowling_frame(self):
        """"""
        # Arrange
        # Act
        frame = BowlingFrame()

        # Assert
        assert frame.score() == 0

    @pytest.mark.parametrize(
        "num_pins",
        [
            8, 9, 10
        ]
    )
    def test_one_roll(self, num_pins):
        "Roll"
        frame = BowlingFrame()

        frame.roll(num_pins)

        assert frame.score() == num_pins

    @pytest.mark.parametrize(
        "num_pin_1, num_pin_2, expected_score",
        [
            (1, 5, 6),
            (3, 7, 10),
            (4, 2, 6),
        ]
    )
    def test_two_roll(self, num_pin_1, num_pin_2, expected_score):
        "Roll"
        frame = BowlingFrame()

        frame.roll(num_pin_1)
        frame.roll(num_pin_2)

        assert frame.score() == expected_score  
    

def test_constructor():
    """Construct a BowlingGame object.
    
    Given:
    When: Construct a BowlingGame object.
    Then: The initial score must be 0
    
    """

    # Arrange
    expected_initial_score = 0

    # Act
    game = BowlingGame()

    # Assert
    result = game.score()
    assert result == expected_initial_score

@pytest.mark.parametrize(
    "list_of_rolls, expected_score",
    [
        ([], 0),
        ([8], 8),
        ([8, 1], 9), # Turn 1
        ([8, 1, 5], 14),
        ([8, 1, 5, 3], 17), # Turn 2
        ([8, 1, 5, 3, 8], 25),
        ([8, 1, 5, 3, 8, 0], 25), # Turn 3
        ([8, 1, 5, 3, 8, 0, 2], 27),
        ([8, 1, 5, 3, 8, 0, 2, 3], 30), # Turn 4
        ([8, 1, 5, 3, 8, 0, 2, 3, 5], 35),
        ([8, 1, 5, 3, 8, 0, 2, 3, 5, 4], 39), # Turn 5

        # spare
        ([], 0),
        ([2, 4], 6), # Turn 1
        ([2, 4, 3, 7, 7], 23), # Turn 2
        ([2, 4, 3, 7, 7, 2], 32), # Turn 3

        # strike
        ([], 0),
        ([0, 10, 2, 6], 26), # Turn 2
    ]
)

def test_given_rolls_return_score(list_of_rolls, expected_score):
    """Given a list of rolls, return total scores."""
    # Arrange
    game = BowlingGame()
    
    for pins in list_of_rolls:
        game.roll(pins)
    
    # Act
    result = game.score()

    # Assert
    assert result == expected_score
