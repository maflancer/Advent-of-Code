# with open("./test.txt", "r") as f:
with open("./input.txt", "r") as f:
    data = [split for split in f.read().split("\n") if split != ""]
    seeds = [
        int(seed) for seed in (data[0].split(":"))[1].split(" ") if seed != ""
    ]
    map = [[] for _ in range(7)]
    level = -1
    for line in data[1:]:
        if "map" in line:
            level += 1
        else:
            line_data = line.split(" ")
            map[level].append(
                {
                    "destination_start": int(line_data[0]),
                    "source_start": int(line_data[1]),
                    "num_range": int(line_data[2]),
                }
            )
    lowest_location = -1
    for seed in seeds:
        curr = seed
        for level in map:
            for group in level:
                destination_start = group["destination_start"]
                source_start = group["source_start"]
                num_range = group["num_range"]

                if source_start <= curr < source_start + num_range:
                    curr = destination_start + (curr - source_start)
                    break

        if lowest_location == -1 or curr < lowest_location:
            lowest_location = curr

    print(
        "The lowest location number that corresponds to any of the initial"
        f" seed numbers is {lowest_location}"
    )
