import os
from copy import deepcopy


def part_one() -> int:
    code: dict = {
        'A': ('Rock', 'Paper'), 'B': ('Paper', 'Scissor'), 'C': ('Scissor', 'Rock'),
        'X': ('Rock', 'Paper'), 'Y': ('Paper', 'Scissor'), 'Z': ('Scissor', 'Rock')
    }

    code_points: dict = {'Rock': 1, 'Paper': 2, 'Scissor': 3}

    score: int = 0

    with open(f'{os.path.dirname(__file__)}\\puzzle.txt', 'r') as file:
        for line in file:
            enemy, player = line.split()

            if code[enemy][0] == code[player][0]:
                score += (3 + code_points[code[player][0]])
            elif code[enemy][1] == code[player][0]:
                score += (6 + code_points[code[player][0]])
            else:
                score += (0 + code_points[code[player][0]])
    return score


def part_two() -> int:
    code: dict = {
        'A': ('Rock', 'Paper'), 'B': ('Paper', 'Scissor'), 'C': ('Scissor', 'Rock'),
        'X': 'Lose', 'Y': 'Draw', 'Z': 'Win'
    }

    code_points: dict = {'Rock': 1, 'Paper': 2, 'Scissor': 3}

    score: int = 0

    with open(f'{os.path.dirname(__file__)}\\puzzle.txt', 'r') as file:
        for line in file:
            enemy, player = line.split()

            if code[player] == 'Lose':
                temp = list(deepcopy(code_points))
                [temp.remove(x) for x in list(code[enemy])]
                score += (0 + code_points[temp[0]])
            elif code[player] == 'Draw':
                score += (3 + code_points[code[enemy][0]])
            elif code[player] == 'Win':
                score += (6 + code_points[code[enemy][1]])
    return score


def main():
    print(
        f'\N{File Folder}{os.path.dirname(__file__).split(chr(92))[-1]}:\n'
        f'\t\N{pushpin}{part_one()}\n'
        f'\t\N{pushpin}{part_two()}'
    )


if __name__ == '__main__':
    main()
