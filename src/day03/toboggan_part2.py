def get_map():
    toboggan_map = []
    with open("toboggan_input.txt", "r") as toboggan_map_description:
        for line in toboggan_map_description.readlines():
            toboggan_map.append(line.strip())

    return toboggan_map


def count_number_of_trees():
    toboggan_map = get_map()
    line_len = len(toboggan_map[0])
    movements = [(1, 1,), (3, 1,), (5, 1,), (7, 1,), (1, 2,)]
    tree_product = 1

    for movement in movements:
        right, down = movement
        tree_count = 0
        i, j = 0, 0
        while i < len(toboggan_map):
            if toboggan_map[i][j] == "#":
                tree_count += 1

            if j + right >= line_len:
                j = j + right - line_len
            else:
                j += right

            i += down

        tree_product *= tree_count

    return tree_product


def main():
    print(count_number_of_trees())


if __name__ == "__main__":
    main()
