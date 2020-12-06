import pytest
from src.day05 import binary_boarding_part1


@pytest.fixture
def mock_get_boarding_passes(mocker):
    mocker.patch.object(
        binary_boarding_part1, "get_boarding_passes", return_value=[
            "BFFFBBFRRR",
            "FFFBBBFRRR",
            "BBFFBBFRLL",
        ]
    )


def test_valid_solutions_found_with_sample_test(mock_get_boarding_passes):
    result = binary_boarding_part1.get_highest_seat_id(128, 8)
    assert result == 820
