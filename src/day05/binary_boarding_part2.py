def get_boarding_passes():
    boarding_passes = []
    with open("boarding_passes_input.txt", "r") as boarding_passes_file:
        for boarding_pass in boarding_passes_file.readlines():
            boarding_passes.append(boarding_pass.strip())

    return boarding_passes


def get_seat_id(rows, columns):
    boarding_passes = get_boarding_passes()
    seat_ids = []

    for boarding_pass in boarding_passes:
        row_min, row_max = 0, rows - 1
        column_min, column_max = 0, columns - 1

        for i in range(6):
            c = boarding_pass[i]
            if c == "F":
                row_max = (row_min + row_max + 1) / 2 - 1
            else:
                row_min = (row_min + row_max + 1) / 2

        if boarding_pass[6] == "F":
            row = (row_min + row_max + 1) / 2 - 1
        else:
            row = (row_min + row_max + 1) / 2

        for i in range(2):
            c = boarding_pass[7 + i]
            if c == "L":
                column_max = (column_min + column_max + 1) / 2 - 1
            else:
                column_min = (column_min + column_max + 1) / 2

        if boarding_pass[-1] == "L":
            column = (column_min + column_max + 1) / 2 - 1
        else:
            column = (column_min + column_max + 1) / 2

        seat_id = row * 8 + column
        seat_ids.append(seat_id)

    seat_ids.sort()
    for i in range(len(seat_ids) - 1):
        if seat_ids[i + 1] - seat_ids[i] == 2:
            return seat_ids[i + 1] - 1


def main():
    print(get_seat_id(128, 8))


if __name__ == "__main__":
    main()
