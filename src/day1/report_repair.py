def get_expenses_from_report():
    expenses = []
    with open("report_repair_input.txt", "r") as expense_report:
        for expense in expense_report.readlines():
            expenses.append(int(expense.strip()))

    return expenses


def repair_expense_report_s1():
    expenses = get_expenses_from_report()
    expenses.sort()

    i = 0
    j = len(expenses) - 1
    while i < j:
        num1 = expenses[i]
        num2 = expenses[j]
        total = num1 + num2

        if total == 2020:
            return num1 * num2
        elif total < 2020:
            i += 1
        else:
            j -= 1

    return -1


def repair_expense_report_s2():
    expenses = get_expenses_from_report()
    expense_pairings = dict()

    for expense in expenses:
        expense_pairings[2020 - expense] = expense

    for expense in expenses:
        try:
            other_expense = expense_pairings[expense]
        except KeyError:
            continue
        else:
            return expense * other_expense


print(repair_expense_report_s1())
print(repair_expense_report_s2())
