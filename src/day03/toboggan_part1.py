def get_map():
    toboggan_map = []
    with open("toboggan_input.txt", "r") as toboggan_map_description:
        for line in toboggan_map_description.readlines():
            toboggan_map.append(line.strip())

    return toboggan_map


def count_number_of_trees():
    toboggan_map = get_map()
    line_len = len(toboggan_map[0])
    tree_count = 0
    i, j = 0, 0

    while i < len(toboggan_map):
        if toboggan_map[i][j] == "#":
            tree_count += 1

        if j + 3 >= line_len:
            j = j + 3 - line_len
        else:
            j += 3

        i += 1

    return tree_count


def main():
    print(count_number_of_trees())


if __name__ == "__main__":
    main()
