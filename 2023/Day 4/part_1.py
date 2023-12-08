# with open("./test.txt", "r") as f:
with open("./input.txt", "r") as f:
    sum = 0
    for card in f.readlines():
        points = 0
        card = card.split(":")[1]
        num_split = card.split("|")
        winning_numbers = [num for num in num_split[0].split(" ") if num != ""]
        my_numbers = [
            num.replace("\n", "")
            for num in num_split[1].split(" ")
            if num != ""
        ]

        for number in my_numbers:
            if number in winning_numbers:
                if points == 0:
                    points = 1
                else:
                    points *= 2
        sum += points

    print(f"The cards are worth {sum} points in total")
