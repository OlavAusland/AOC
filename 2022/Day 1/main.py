from typing import List
import os
import argparse


class Reindeer:
    def __init__(self):
        self.calories = 0


reindeers: List[Reindeer] = [Reindeer()]


def part_one():
    global reindeers
    with open(f'{os.path.dirname(__file__)}\\puzzle.txt', 'r') as file:
        for line in file:
            if line == '\n':
                reindeers.append(Reindeer())
                continue
            reindeers[-1].calories += int(line)
    return max(reindeers, key=lambda x: x.calories).calories


def part_two():
    global reindeers
    with open(f'{os.path.dirname(__file__)}\\puzzle.txt', 'r') as file:
        for line in file:
            if line == '\n':
                reindeers.append(Reindeer())
                continue
            reindeers[-1].calories += int(line)
    reindeers = sorted(reindeers, key=lambda x: x.calories, reverse=True)
    return sum(reindeer.calories for reindeer in reindeers[0:3])


# You can quite easily use a single array of integers, but let's use a Reindeer object for the spirit :)
def main():
    print(
        f'\N{File Folder}{os.path.dirname(__file__).split(chr(92))[-1]}:\n'
        f'\t\N{pushpin}{part_one()}\n'
        f'\t\N{pushpin}{part_two()}'
    )


if __name__ == '__main__':
    main()
