sum = 0

# with open("./test_1.txt", "r") as f:
with open("./input.txt", "r") as f:
    for line in f.readlines():
        for letter in line:
            try:
                first = int(letter)
                break
            except ValueError:
                pass

        for letter in reversed(line):
            try:
                last = int(letter)
                break
            except ValueError:
                pass

        sum += int(str(first) + str(last))

print(f"The sum of all calibration values is: {sum}")
