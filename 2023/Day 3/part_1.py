nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
non_symbols = nums + ["."]


def hasAdjacentSymbol(grid, x, y):
    # right
    if y + 1 < len(grid) and grid[x][y + 1] not in non_symbols:
        return True
    # left
    if y - 1 >= 0 and grid[x][y - 1] not in non_symbols:
        return True
    # up
    if x - 1 >= 0 and grid[x - 1][y] not in non_symbols:
        return True
    #  down
    if x + 1 < len(grid) and grid[x + 1][y] not in non_symbols:
        return True
    # up-right
    if (
        x - 1 >= 0
        and y + 1 < len(grid)
        and grid[x - 1][y + 1] not in non_symbols
    ):
        return True
    # up-left
    if x - 1 >= 0 and y - 1 >= 0 and grid[x - 1][y - 1] not in non_symbols:
        return True
    # down-right
    if (
        x + 1 < len(grid)
        and y + 1 < len(grid)
        and grid[x + 1][y + 1] not in non_symbols
    ):
        return True
    # down-left
    if (
        x + 1 < len(grid)
        and y - 1 >= 0
        and grid[x + 1][y - 1] not in non_symbols
    ):
        return True


# with open("./test.txt", "r") as f:
with open("./input.txt", "r") as f:
    grid = [
        [token for token in (line[:-1] if line[-1] == "\n" else line)]
        for line in f.readlines()
    ]

    sum = 0
    for x in range(len(grid)):
        is_valid = False
        full_num = ""
        for y, tok in enumerate(grid[x]):
            try:
                num = int(tok)
                full_num += tok
                if hasAdjacentSymbol(grid, x, y):
                    is_valid = True
                if y + 1 >= len(grid) or grid[x][y + 1] not in nums:
                    if is_valid:
                        sum += int(full_num)
                    is_valid = False
                    full_num = ""
            except (ValueError, IndexError):
                pass

    print(f"The sum of all part numbers in the engine schematic is: {sum}")
