from typing import TextIO


def create_tables():
    """
    creates series if dicts
    cols: dict where key - board column index(0..4) value - length if corresponding column
    rows : same dict as for cols, but for rows
    diagonals: same dict for diagonals

    """
    cols = {k: v for k in range(5) for v in [5 for _ in range(5)]}
    rows = {k: v for k in range(5) for v in [5 for _ in range(5)]}

    return rows, cols


class Board:

    def __init__(self, board: list):
        self.board = board
        self.positions = self.create_positions()
        self.tables = create_tables()
        self.won = False

    def create_positions(self):
        """
        Creates dict where keys - board values , values - position of value in board
        1: [0,1]
        2: [0,3]
        ...
        :return:
        """
        pos = {}
        for irow, row in enumerate(self.board):
            for icol, cell in enumerate(row):
                pos[cell] = [irow, icol]
        return pos

    def mark_number(self, n) -> int:
        if self.won:
            return -1

        if n not in self.positions:
            return -1

        position = self.positions[n]

        self.board[position[0]][position[1]] = -1

        self.tables[0][position[0]] -= 1
        self.tables[1][position[1]] -= 1

        if self.tables[0][position[0]] == 0 or self.tables[1][position[1]] == 0:
            return self.count_score(n)

        return -1

    def count_score(self, n) -> int:
        score = 0
        for irow, row in enumerate(self.board):
            for cell in row:
                if cell == -1:
                    continue
                score += cell
        self.won = True
        return score * n


class Solution:

    def __init__(self, input: TextIO):
        self.input = input

    def star_one(self):
        numbers = [int(num) for num in self.input.readline().split(",")]
        self.input.readline()
        _next = 5
        boards = []
        board = []
        lines = self.input.readlines()
        for line in lines:
            if _next == 0:
                _next = 5
                boards.append(board)
                board = []
                continue
            row = [int(n) for n in line.split()]
            board.append(row)
            _next -= 1
        items = set()
        boards.append(board)
        for brd in boards:
            b = Board(brd)
            items.add(b)

        last = 0
        for n in numbers:
            for item in items:
                score = item.mark_number(n)
                if score != -1:
                    last = score
        return last

    def star_two(self):
        pass


class NumberNotFound(Exception):

    def __init__(self, number, message="number not found in board"):
        self.number = number
        self.message = message
        super().__init__(message)

    def __str__(self):
        return f'{self.number}: {self.message}'


if __name__ == '__main__':
    with open("/Users/aabodagovskiy/advent_of_code_2021/input/day4/input.txt") as input:
        print(Solution(input).star_one())
        # print(Solution(input).star_two())
