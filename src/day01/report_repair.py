def get_expenses_from_report():
    expenses = []
    with open("report_repair_input.txt", "r") as expense_report:
        for expense in expense_report.readlines():
            expenses.append(int(expense.strip()))

    return expenses


def repair_expense_report_s1(expected_value):
    expenses = get_expenses_from_report()
    expenses.sort()

    i = 0
    j = len(expenses) - 1
    while i < j:
        num1 = expenses[i]
        num2 = expenses[j]
        total = num1 + num2

        if total == expected_value:
            return num1 * num2
        elif total < expected_value:
            i += 1
        else:
            j -= 1

    return -1


def repair_expense_report_s2(expected_value, provided_expenses=None):
    if not provided_expenses:
        expenses = get_expenses_from_report()
    else:
        expenses = provided_expenses
    expense_pairings = dict()

    for expense in expenses:
        try:
            other_expense = expense_pairings[expense]
        except KeyError:
            expense_pairings[expected_value - expense] = expense
        else:
            return expense * other_expense

    return -1


def repair_expense_report_part2(expected_value):
    expenses = get_expenses_from_report()
    expenses_set = set(expenses)

    for expense in expenses:
        expenses_set.remove(expense)
        result = repair_expense_report_s2(expected_value - expense, expenses_set)

        if result == -1:
            expenses_set.add(expense)
            continue

        return result * expense


def main():
    print(repair_expense_report_s1(2020))
    print(repair_expense_report_s2(2020))
    print(repair_expense_report_part2(2020))


if __name__ == "__main__":
    main()
