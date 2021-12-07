import math
from typing import TextIO


def count(n: int, days: int):

    if n <= 6:
        div, mod = divmod(days, 7)
        amount = div
        if mod > n:
            amount += 1

    else:
        d = days - (n - 6)
        n = 6
        div, mod = divmod(d, 7)
        amount = div
        if mod > n:
            amount += 1
    if mod == 0:
        days -= 7
    return amount, days - mod


class Solution:

    def __init__(self, input: TextIO):
        self.input = input

    def star_one(self):
        fish = [[int(n), 18] for n in self.input.readline().strip().split(",")]
        total = len(fish)

        while fish:
            f = fish[0]
            fish = fish[1:]

            children, days = count(f[0], f[1])
            total += children

            for _ in range(children):
                fish.append([8, days])
                days -= 7

        print(total)
        return total


if __name__ == '__main__':
    with open("/Users/aabodagovskiy/advent_of_code_2021/input/day6/test_input.txt") as input:
        Solution(input).star_one()






