import pytest
from src.day03 import toboggan_part1


@pytest.fixture
def mock_get_map(mocker):
    mocker.patch.object(
        toboggan_part1, "get_map", return_value=[
            "..##.......",
            "#...#...#..",
            ".#....#..#.",
            "..#.#...#.#",
            ".#...##..#.",
            "..#.##.....",
            ".#.#.#....#",
            ".#........#",
            "#.##...#...",
            "#...##....#",
            ".#..#...#.#",
        ]
    )


def test_valid_solutions_found_with_sample_test(mock_get_map):
    result = toboggan_part1.count_number_of_trees()
    assert result == 7
