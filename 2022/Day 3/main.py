import copy
import os
from typing import List, Set
import numpy as np


class Rucksack:
    def __init__(self, content: str):
        self.content: str = content

        self.primary: dict = {}
        self.secondary: dict = {}

        self._split_content()
        self.common_item: chr = self._get_common_item()
        self.common_item_priority = self.get_item_priority(self.common_item)

        self.badge: chr

    def _split_content(self):
        first, second = self.content[0:len(self.content)//2], self.content[len(self.content)//2:].strip('\n')

        for item in first:
            if item in self.primary.keys():
                self.primary[item] += 1
            else:
                self.primary[item] = 1

        for item in second:
            if item in self.secondary.keys():
                self.secondary[item] += 1
            else:
                self.secondary[item] = 1

    def _get_common_item(self):
        for item in self.content:
            if item in self.primary.keys() and item in self.secondary.keys():
                return item

    @staticmethod
    def get_item_priority(item: chr):
        if str(item).islower():
            return ord(item) - 96
        else:
            return ord(item) - 64 + 26

    def __repr__(self):
        return f'Primary: {self.primary}\n' \
               f'Secondary: {self.secondary}\n' \
               f'Common Item: {self.common_item}'


rucksacks: List[Rucksack] = []


def part_one():
    global rucksacks

    with open(f'{os.path.dirname(__file__)}\\puzzle.txt', 'r') as file:
        for line in file:
            rucksacks.append(Rucksack(line))

        return sum([rucksack.common_item_priority for rucksack in rucksacks])


# slow as fuck
def part_two():
    global rucksacks

    answer: int = 0

    for index in range(0, len(rucksacks), 3):
        first, second, third = rucksacks[index:index+3]

        for char in first.content:
            if char in second.content and char in third.content:
                first.badge, second.badge, third.badge = char, char, char
                break
        answer += Rucksack.get_item_priority(first.badge)

    return answer


def main():
    print(
        f'\N{File Folder}{os.path.dirname(__file__).split(chr(92))[-1]}:\n'
        f'\t\N{pushpin}{part_one()}\n'
        f'\t\N{pushpin}{part_two()}'
    )


if __name__ == '__main__':
    main()
