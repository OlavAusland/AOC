import os
import re
import numpy as np
from typing import TextIO, List


def load_puzzle() -> list:
    with open(f'{os.path.dirname(__file__)}\\puzzle.txt', 'r') as file:
        pattern = re.compile('[a-zA-Z]')
        stacks = [[] for _ in range(9)]

        for i, line in enumerate(file):

            if str(line[1]).isnumeric():
                next(file)
                break
            for char in range(1, len(line), 4):
                if len(re.findall('[a-zA-Z]', line)) > len(stacks):
                    stacks = [[] for i in range(len(re.findall('[a-zA-Z]', line)))]
                if bool(re.search(pattern, line[char])):
                    stacks[(char // 4)].insert(0, line[char])
    return stacks


def skip_initial_stack(file: TextIO):
    for line in file:
        if str(line[1]).isnumeric():
            next(file)
            break


def part_one():
    result: str = ''
    with open(f'{os.path.dirname(__file__)}\\puzzle.txt', 'r') as file:
        stacks = load_puzzle()
        skip_initial_stack(file)

        for line in file:
            command = np.asarray(re.findall('[0-9]+', line), dtype=int)
            for i in range(command[0]):
                crate = stacks[command[1] - 1].pop()
                stacks[command[2] - 1].append(crate)
        for stack in stacks:
            if len(stack) > 0:
                result += stack.pop()

    return result


def part_two():
    result: str = ''
    with open(f'{os.path.dirname(__file__)}\\puzzle.txt', 'r') as file:
        stacks: List[List] = load_puzzle()
        skip_initial_stack(file)

        for line in file:
            command = np.asarray(re.findall('[0-9]+', line), dtype=int)
            crates = []

            for i in range(command[0]):
                crates.append(stacks[command[1]-1].pop())

            for crate in reversed(crates):
                stacks[command[2] - 1].append(crate)

        for stack in stacks:
            if len(stack) > 0:
                result += stack.pop()
    return result


def main():
    print(
        f'\N{File Folder}{os.path.dirname(__file__).split(chr(92))[-1]}:\n'
        f'\t\N{pushpin}{part_one()}\n'
        f'\t\N{pushpin}{part_two()}'
    )


if __name__ == '__main__':
    main()
