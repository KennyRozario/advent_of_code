import pytest
from src.day06 import custom_customs_part2


@pytest.fixture
def mock_get_customs_forms(mocker):
    mocker.patch.object(
        custom_customs_part2, "get_customs_forms", return_value=[
            ["abc"],
            ["a", "b", "c"],
            ["ab", "ac"],
            ["a", "a", "a", "a"],
            ["b"],
        ]
    )


def test_valid_solutions_found_with_sample_test(mock_get_customs_forms):
    result = custom_customs_part2.total_number_of_yes_responses()
    assert result == 6
