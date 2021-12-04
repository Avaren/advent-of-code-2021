from typing import List


class BingoBoard:
    cols = 5

    def __init__(self, board_data):
        self.winning_lines: List[set] = []
        coords = {}
        for y, row in enumerate(board_data.splitlines()):
            for x, n in enumerate(row.strip().split()):
                coords[(x, y)] = int(n)
        for x in range(self.cols):
            self.winning_lines.append({coords[(x, y)] for y in range(self.cols)})
        for y in range(self.cols):
            self.winning_lines.append({coords[(x, y)] for x in range(self.cols)})

    def win(self, numbers: set):
        for line in self.winning_lines:
            if line.issubset(numbers):
                return True
        return False

    def score(self, past_numbers):
        numbers = set()
        for line in self.winning_lines:
            numbers |= line
        unused = numbers - past_numbers
        return sum(unused)


def parse_file(file_name):
    bingo_boards = []
    with open(f"advent-of-code-2021/day_4/{file_name}") as f:
        data = f.read().split("\n\n")

    numbers = [int(n) for n in data[0].split(",")]

    for board_data in data[1:]:
        bingo_boards.append(BingoBoard(board_data))

    return numbers, bingo_boards


def part_1(numbers, bingo_boards):
    past_numbers = set()
    for i in numbers:
        past_numbers.add(i)
        for bb in bingo_boards:
            if bb.win(past_numbers):
                return bb.score(past_numbers) * i


def part_2(numbers, bingo_boards):
    past_numbers = set()
    last_winner = None
    for i in numbers:
        past_numbers.add(i)
        boards_remaining = [bb for bb in bingo_boards if not bb.win(past_numbers)]

        if len(boards_remaining) == 0:
            return last_winner.score(past_numbers) * i
        else:
            last_winner = boards_remaining[0]
