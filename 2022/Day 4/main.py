import os
import numpy as np


pairs: list = []


def part_one():
    global pairs

    answer: int = 0
    with open(f'{os.path.dirname(__file__)}\\puzzle.txt', 'r') as file:
        for line in file:
            first, second = line.split(',')
            pairs.append([tuple(np.asarray(first.split('-'), dtype=int)),
                          tuple(np.asarray(second.strip('\n').split('-'), dtype=int))])

        for pair in pairs:
            first, second = pair
            if (first[0] <= second[0] and first[1] >= second[1]) or (second[0] <= first[0] and second[1] >= first[1]):
                answer += 1

    return answer


def part_two():
    global pairs

    answer: int = 0

    for pair in pairs:
        first, second = pair

        first_arr = set(np.arange(first[0], first[1] + 1))
        second_arr = set(np.arange(second[0], second[1] + 1))

        if first_arr & second_arr:
            answer += 1

    return answer


def main():
    print(
        f'\N{File Folder}{os.path.dirname(__file__).split(chr(92))[-1]}:\n'
        f'\t\N{pushpin}{part_one()}\n'
        f'\t\N{pushpin}{part_two()}'
    )


if __name__ == '__main__':
    main()
