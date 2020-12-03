import pytest
from src.day2 import pwd_philosophy_part2


@pytest.fixture
def mock_get_and_format_input(mocker):
    mocker.patch.object(
        pwd_philosophy_part2, "get_and_format_input", return_value=[
            ("1", "3", "a", "abcde",),
            ("1", "3", "b", "cdefg",),
            ("2", "9", "c", "ccccccccc")
        ]
    )


def test_valid_solutions_found_with_sample_test(mock_get_and_format_input):
    result = pwd_philosophy_part2.count_valid_passwords()
    assert result == 1
