from typing import TextIO


class Sequence:

    def __init__(self, sequence: list):
        self.sequence = sequence
        self.sequence.sort()
        self.direction = self.define_direction()

    def define_direction(self) -> str:
        start = self.sequence[0]
        end = self.sequence[1]

        if start[0] == end[0]:
            return "vertical"
        elif start[1] == end[1]:
            return "horizontal"
        else:
            return "diagonal"

    def covers_spot(self, spot: tuple) -> bool:
        if self.direction == "horizontal":
            return spot[1] == self.sequence[0][1] and self.sequence[0][0] <= spot[0] <= self.sequence[1][0]

        if self.direction == "vertical":
            return spot[0] == self.sequence[0][0] and self.sequence[0][1] <= spot[1] <= self.sequence[1][1]

        if self.direction == "diagonal":
            return False

    def get_direction(self):
        return self.direction

    def get_coords(self):
        return self.sequence


class Solution:

    def __init__(self, input: TextIO):
        self.input = input

    def star_one(self):
        global i
        ranges = []
        lines = self.input.readlines()
        min_x, min_y = float('Inf'), float('Inf')
        max_x, max_y = float('-Inf'), float('-Inf')

        for line in lines:
            line = line.strip()
            start, end = [el.strip() for el in line.split("->")]
            start = [int(n) for n in start.split(",")]
            end = [int(n) for n in end.split(",")]
            seq = [start, end]
            r = Sequence(seq)

            if min(start[0], end[0]) < min_x:
                min_x = min(start[0], end[0])
            if min(start[1], end[1]) < min_y:
                min_y = min(start[1], end[1])
            if max(start[0], end[0]) > max_x:
                max_x = max(start[0], end[0])
            if max(start[1], end[1]) > max_y:
                max_y = max(start[1], end[1])
            ranges.append(r)

        field = [[0 for _ in range(0, max_x+1)] for _ in range(0, max_y+1)]
        counter = 0

        for r in ranges:
            start, end = r.get_coords()

            if r.get_direction() == "diagonal":
                x, y = start[0], start[1]
                while x <= end[0] and y <= end[1]:
                    field[y][x] += 1
                    if field[y][x] == 2:
                        counter += 1
                    x += 1
                    y += 1
                while x <= end[0] and y >= end[1]:
                    field[y][x] += 1
                    if field[y][x] == 2:
                        counter += 1
                    x += 1
                    y -= 1

            if r.get_direction() == "horizontal":
                for i in range(start[0], end[0] + 1):
                    field[start[1]][i] += 1
                    if field[start[1]][i] == 2:
                        counter += 1
            if r.get_direction() == "vertical":
                for i in range(start[1], end[1] + 1):
                    field[i][start[0]] += 1
                    if field[i][start[0]] == 2:
                        counter += 1
        return counter


if __name__ == '__main__':
    with open("/Users/aabodagovskiy/advent_of_code_2021/input/day5/input.txt") as input:
        print(Solution(input).star_one())