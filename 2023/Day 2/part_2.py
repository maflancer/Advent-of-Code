sum = 0

# with open("./test.txt", "r") as f:
with open("./input.txt", "r") as f:
    for game in f.readlines():
        game_split = game.split(" ")[2:]

        max_colors = {"red": -1, "green": -1, "blue": -1}
        for idx, token in enumerate(game_split):
            try:
                count = int(token)
                color = (
                    game_split[idx + 1][:-1]
                    if game_split[idx + 1][-1] in [";", ",", "\n"]
                    else game_split[idx + 1]
                )
                if max_colors[color] == -1 or count > max_colors[color]:
                    max_colors[color] = count
            except ValueError:
                pass
        sum += max_colors["red"] * max_colors["green"] * max_colors["blue"]

    print(f"The sum of the powers of these sets is: {sum}")
