nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def hasAdjacentStar(grid, x, y):
    # right
    if y + 1 < len(grid) and grid[x][y + 1] == "*":
        return True, x, y + 1
    # left
    if y - 1 >= 0 and grid[x][y - 1] == "*":
        return True, x, y - 1
    # up
    if x - 1 >= 0 and grid[x - 1][y] == "*":
        return True, x - 1, y
    #  down
    if x + 1 < len(grid) and grid[x + 1][y] == "*":
        return True, x + 1, y
    # up-right
    if x - 1 >= 0 and y + 1 < len(grid) and grid[x - 1][y + 1] == "*":
        return True, x - 1, y + 1
    # up-left
    if x - 1 >= 0 and y - 1 >= 0 and grid[x - 1][y - 1] == "*":
        return True, x - 1, y - 1
    # down-right
    if x + 1 < len(grid) and y + 1 < len(grid) and grid[x + 1][y + 1] == "*":
        return True, x + 1, y + 1
    # down-left
    if x + 1 < len(grid) and y - 1 >= 0 and grid[x + 1][y - 1] == "*":
        return True, x + 1, y - 1

    return False, -1, -1


# with open("./test.txt", "r") as f:
with open("./input.txt", "r") as f:
    grid = [
        [token for token in (line[:-1] if line[-1] == "\n" else line)]
        for line in f.readlines()
    ]

    stars = {}
    for x in range(len(grid)):
        full_num = ""
        star_list = []
        for y, tok in enumerate(grid[x]):
            try:
                num = int(tok)
                full_num += tok
                (hasStar, row, col) = hasAdjacentStar(grid, x, y)
                if hasStar:
                    star_list.append((row, col))
                    star_list = list(set(star_list))
                if y + 1 >= len(grid) or grid[x][y + 1] not in nums:
                    if star_list:
                        for row, col in star_list:
                            try:
                                stars[(row, col)]["count"] += 1
                                stars[(row, col)]["ratio"] *= int(full_num)
                            except KeyError:
                                stars[(row, col)] = {
                                    "count": 1,
                                    "ratio": int(full_num),
                                }
                    star_list = []
                    full_num = ""
            except (ValueError, IndexError):
                pass

    sum = 0
    for index, star in stars.items():
        if star["count"] >= 2:
            sum += star["ratio"]
    print(f"The sum of all gear ratios in the engine schematic is: {sum}")
