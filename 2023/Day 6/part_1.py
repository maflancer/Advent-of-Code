import re

# with open("./test.txt", "r") as f:
with open("./input.txt", "r") as f:
    data = [split for split in f.read().split("\n") if split != ""]
    times = [int(time) for time in re.findall(r"\d+", data[0])]
    records = [int(time) for time in re.findall(r"\d+", data[1])]

    total = 1
    for i, time in enumerate(times):
        record = records[i]
        num_ways = 0
        for hold_time in range(0, time + 1):
            move_time = time - hold_time
            distance = hold_time * move_time

            if distance > record:
                num_ways += 1

        total *= num_ways

    print(f"You can beat the record {total} number of ways!")
