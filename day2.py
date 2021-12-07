from typing import TextIO


class Solution:

    def __init__(self, input: TextIO):
        self.input = input

    def star_one(self):
        depth = 0
        x_position = 0
        for line in self.input:
            direction, amount = line.split()
            if direction == "forward":
                x_position += int(amount)
            elif direction == "up":
                depth -= int(amount)
            elif direction == "down":
                depth += int(amount)
        return depth * x_position

    def star_two(self):
        depth = 0
        x_position = 0
        aim = 0
        for line in self.input:
            direction, amount = line.split()
            if direction == "forward":
                x_position += int(amount)
                depth += aim * int(amount)
            elif direction == "up":
                aim -= int(amount)
            elif direction == "down":
                aim += int(amount)
        return depth * x_position


if __name__ == '__main__':
    with open("/Users/aabodagovskiy/advent_of_code_2021/input/day2/input.txt") as input:
        # print(Solution(input).star_one())
        print(Solution(input).star_two())