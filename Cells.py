from collections import namedtuple, defaultdict
import time

Cell = namedtuple('Cell', ['m', 'n'])


def getNeighbours(cell):
    for m in range(cell.m - 1, cell.m + 2):
        for n in range(cell.n - 1, cell.n + 2):
            if (m, n) != (cell.m, cell.n):
                yield Cell(m, n)


def getNeighbourCount(board):
    neighbour_counts = defaultdict(int)
    for cell in board:
        for neighbour in getNeighbours(cell):
            neighbour_counts[neighbour] += 1
    return neighbour_counts


def advanceBoard(board):
    new_board = set()
    for cell, count in getNeighbourCount(board).items():
        if count == 3 or (cell in board and count == 2):
            new_board.add(cell)
    return new_board


def generateBoard(desc):
    board = set()
    for row, line in enumerate(desc.split("\n")):
        for col, elem in enumerate(line):
            if elem == '#':
                board.add(Cell(int(col), int(row)))
    return board


def boardToString(board, pad=0):
    if not board:
        return "empty"
    board_str = ""
    ms = [m for (m, n) in board]
    ns = [n for (m, n) in board]
    for n in range(min(ns) - pad, max(ns) + 1 + pad):
        for m in range(min(ms) - pad, max(ms) + 1 + pad):
            board_str += '#' if Cell(m, n) in board else '.'
        board_str += '\n'
    return board_str.strip()


if __name__ == '__main__':
    f = generateBoard("......#.\n##......\n.#...###")
    for _ in range(130):
        f = advanceBoard(f)
        print("\033[2J\033[1;1H" + boardToString(f, 2))
        time.sleep(1)
