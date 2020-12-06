def get_boarding_passes():
    boarding_passes = []
    with open("boarding_passes_input.txt", "r") as boarding_passes_file:
        for boarding_pass in boarding_passes_file.readlines():
            boarding_passes.append(boarding_pass.strip())

    return boarding_passes


def get_highest_seat_id(rows, columns):
    boarding_passes = get_boarding_passes()
    max_seat_id = -1

    for boarding_pass in boarding_passes:
        row_min, row_max = 0, rows - 1
        column_min, column_max = 0, columns - 1
        count = 1
        row = -1
        column = -1

        # To make this cleaner I would split it into two loops that stop at length of section - 1, then compute the
        # last value outside the loop and save that information into row or column
        for c in boarding_pass:
            if c == "F":
                row_max = (row_min + row_max + 1) / 2 - 1
                if count == 7:
                    row = row_max
                    count = 1
                else:
                    count += 1
            elif c == "B":
                row_min = (row_min + row_max + 1) / 2
                if count == 7:
                    row = row_min
                    count = 1
                else:
                    count += 1
            elif c == "L":
                column_max = (column_min + column_max + 1) / 2 - 1
                if count == 3:
                    column = column_max
                    count = 1
                else:
                    count += 1
            else:
                column_min = (column_min + column_max + 1) / 2
                if count == 3:
                    column = column_min
                    count = 1
                else:
                    count += 1

        seat_id = row * 8 + column
        if seat_id > max_seat_id:
            max_seat_id = seat_id

    return max_seat_id


def main():
    print(get_highest_seat_id(128, 8))


if __name__ == "__main__":
    main()
