from typing import TextIO


class Solution:

    def __init__(self, input: TextIO):
        self.input = input

    def star_one(self):
        digits = [[0,0] for _ in range(len(self.input.readline().strip()))]
        for line in self.input:
            line = line.strip()
            for i, s in enumerate(line):
                digits[i][int(s)] += 1

        x, y = 0,0
        power = len(digits) - 1
        for d in digits:
            if d[0] > d[1]:
                x += 2**power
            else:
                y += 2**power
            power -= 1
        return x * y

    def star_two(self):
        discard_set = []
        digits = [0,0]
        power = 11
        power2 = power

        oxygen = set([line.strip() for line in self.input.readlines()])

        co2 = oxygen.copy()
        i = 0

        while len(oxygen) > 1:

            for ox in oxygen:
                digits[int(ox[i])] += 1

            if digits[1] >= digits[0]:
                for ox in oxygen:
                    if ox[i] == "0":
                        discard_set.append(ox)
            else:
                for ox in oxygen:
                    if ox[i] == "1":
                        discard_set.append(ox)
            for dis in discard_set:
                oxygen.discard(dis)

            discard_set.clear()
            digits = [0,0]
            i += 1

        i = 0
        digits = [0, 0]
        discard_set.clear()

        print(co2)

        while len(co2) > 1:
            for c in co2:
                digits[int(c[i])] += 1

            if digits[1] >= digits[0]:
                for c in co2:
                    if c[i] == "1":
                        discard_set.append(c)
            else:
                for c in co2:
                    if c[i] == "0":
                        discard_set.append(c)

            for dis in discard_set:
                co2.discard(dis)

            discard_set.clear()
            digits = [0,0]
            i += 1

        x, y = 0,0

        for n in oxygen.pop():

            if n == "1":
                x += 2**power
            power -= 1

        for n in co2.pop():
            if n == "1":
                y += 2**power2
            power2 -= 1

        print(x, y)
        return x*y


if __name__ == '__main__':
    with open("/Users/aabodagovskiy/advent_of_code_2021/input/day3/input.txt") as input:
        # print(Solution(input).star_one())
        print(Solution(input).star_two())