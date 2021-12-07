from typing import TextIO


class Solution:

    def star_one(self):
        prev = int(self.input.readline()[0])
        counter = 0
        for line in self.input:
            if int(line) > prev:
                counter += 1
            prev = int(line)
        return counter

    def star_two(self):
        lines = self.input.readlines()
        prev = sum([int(x) for x in lines[0:3]])
        counter = 0
        for i in range(2, len(lines)-1):
            curr = sum([int(x) for x in lines[i-1:i+2]])
            if curr > prev:
                counter += 1
            prev = curr
        return counter

    def __init__(self, input: TextIO):
        self.input = input


if __name__ == '__main__':
    with open("/Users/aabodagovskiy/advent_of_code_2021/input/day1/input_2.txt") as input:
        print(Solution(input).star_two())
