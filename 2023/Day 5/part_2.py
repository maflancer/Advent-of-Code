# with open("./test.txt", "r") as f:
with open("./input.txt", "r") as f:
    data = [split for split in f.read().split("\n") if split != ""]
    seed_data = [
        int(seed) for seed in (data[0].split(":"))[1].split(" ") if seed != ""
    ]

    def isSeed(curr):
        for i in range(0, len(seed_data), 2):
            range_start = seed_data[i]
            num_range = seed_data[i + 1]

            if range_start <= curr < range_start + num_range:
                return True
        return False

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

    # loop here until the part 1 answer (2282277027) since
    # this answer will be <= it
    for location_id in range(0, 282277027 + 1):
        curr = location_id
        for level in reversed(map):
            for group in level:
                destination_start = group["destination_start"]
                source_start = group["source_start"]
                num_range = group["num_range"]

                if destination_start <= curr < destination_start + num_range:
                    curr = source_start + (curr - destination_start)
                    break

        if isSeed(curr):
            print(
                "The lowest location number that corresponds to any of the"
                f" initial seed numbers is: {location_id}"
            )
            break
