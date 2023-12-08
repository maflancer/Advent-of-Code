# with open("./test.txt", "r") as f:
with open("./input.txt", "r") as f:
    total = 0
    copies = {}
    games = 0
    for id, card in enumerate(f.readlines()):
        games += 1
        card = card.split(":")[1]
        num_split = card.split("|")
        winning_numbers = [num for num in num_split[0].split(" ") if num != ""]
        my_numbers = [
            num.replace("\n", "")
            for num in num_split[1].split(" ")
            if num != ""
        ]
        matching_numbers = len(
            [num for num in my_numbers if num in winning_numbers]
        )

        for i in range(id + 2, id + 2 + matching_numbers):
            try:
                copies[i] += 1 * (copies[id + 1] + 1)
            except KeyError:
                try:
                    copies[i] = 1 * (copies[id + 1] + 1)
                except KeyError:
                    copies[i] = 1

    total = sum([count for _, count in copies.items()]) + games
    print(f"There are a total of {total} scratchcards.")
