import math
from typing import TextIO


def count(n: int, days: int):
    if days < n:
        return 0,0

    if n <= 6:
        div, mod = divmod(days, 7)
        amount = div
        if mod > n:
            amount += 1

    else:
        d = days - (n - 6)
        x = 6
        div, mod = divmod(d, 7)
        amount = div
        if mod > x:
            amount += 1

    return amount, days - (n+1)


class Solution:

    def __init__(self, input: TextIO):
        self.input = input
        self.counted = {}

    def star_one(self):
        fish = [[int(n), 80] for n in self.input.readline().strip().split(",")]
        total = len(fish)

        for f in fish:
            if f[0] in self.counted:
                total += self.counted[f]
                continue

            fish_array = [f]
            tmp_total = 0

            while fish_array:
                f = fish_array.pop()

                children, days = count(f[0], f[1])

                tmp_total += children

                for _ in range(children):
                    fish_array.append([8, days])
                    days -= 7
            total += tmp_total
            self.counted[f[0]] = total
        print(total)
        return total


if __name__ == '__main__':
    with open("/Users/aabodagovskiy/advent_of_code_2021/input/day6/input.txt") as input:
        Solution(input).star_one()






