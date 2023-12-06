color_limits = {"red": 12, "green": 13, "blue": 14}

sum = 0

with open("./input.txt", "r") as f:
    for game in f.readlines():
        game_split = game.split(" ")
        id = int((game_split[1])[:-1])

        game_split = game_split[2:]
        is_valid = True
        for idx, token in enumerate(game_split):
            try:
                count = int(token)
                color = game_split[idx + 1][:-1]
                if count > color_limits[color]:
                    is_valid = False
                    break
            except ValueError:
                pass

        if is_valid:
            sum += id

    print(f"The sum of the IDs of the games is: {sum}")
