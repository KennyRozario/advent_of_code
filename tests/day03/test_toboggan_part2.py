import pytest
from src.day03 import toboggan_part2


@pytest.fixture
def mock_get_map(mocker):
    mocker.patch.object(
        toboggan_part2, "get_map", return_value=[
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
    result = toboggan_part2.count_number_of_trees()
    assert result == 336
