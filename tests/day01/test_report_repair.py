import pytest
from src.day01 import report_repair


@pytest.fixture
def mock_get_expenses_from_report(mocker):
    mocker.patch.object(
        report_repair, "get_expenses_from_report", return_value=[1721, 979, 366, 299, 675, 1456]
    )


def test_solution1_succeeds_against_sample(mock_get_expenses_from_report):
    result = report_repair.repair_expense_report_s1(2020)
    assert result == 514579


def test_solution2_succeeds_against_sample(mock_get_expenses_from_report):
    result = report_repair.repair_expense_report_s2(2020)
    assert result == 514579


def test_part2_solution_succeeds_against_sample(mock_get_expenses_from_report):
    result = report_repair.repair_expense_report_part2(2020)
    assert result == 241861950
