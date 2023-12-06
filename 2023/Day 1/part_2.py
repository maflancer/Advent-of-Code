import re

digits = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

sum = 0

# with open("./test_2.txt", "r") as f:
with open("./input.txt", "r") as f:
    for line in f.readlines():
        first_idx = -1
        last_idx = -1
        for index, letter in enumerate(line):
            try:
                first = int(letter)
                first_idx = index
                break
            except ValueError:
                pass

        for index, letter in enumerate(reversed(line)):
            try:
                last = int(letter)
                last_idx = len(line) - index - 1
                break
            except ValueError:
                pass

        for word, num in digits.items():
            for idx in re.finditer(word, line):
                idx = idx.start()
                if (idx != -1 and idx < first_idx) or (first_idx == -1):
                    first = num
                    first_idx = idx
                if (idx != -1 and idx > last_idx) or (last_idx == -1):
                    last = num
                    last_idx = idx

        sum += int(str(first) + str(last))

print(f"The sum of all calibration values is: {sum}")
