import os
import numpy as np


def process_input() -> np.ndarray:
    tree_map: list = []
    with open(f'{os.path.dirname(__file__)}\\puzzle.txt', 'r') as file:
        for line in file:
            tree_map.append(np.asarray([*line.strip('\n')], dtype=int))
        return np.asarray(tree_map)


def part_one():
    result: int = 0
    tree_map = process_input()

    for y in range(1, len(tree_map) - 1):
        for x in range(1, len(tree_map[0]) - 1):
            height = tree_map[y][x]
            left, right = tree_map[y, :x], tree_map[y, x + 1:]
            up, down = tree_map[:y, x], tree_map[y + 1:, x]

            if (
                    all(height > h for h in left)
                    or all(height > h for h in right)
                    or all(height > h for h in up)
                    or all(height > h for h in down)
            ):
                result += 1

    return f'Visible: {result + (len(tree_map) * 2 + len(tree_map[0]) * 2) - 4}'


def scenic_score(tree_map: np.ndarray, x, y):
    table: np.array = np.array([0, 0, 0, 0])  # up, down, left, right

    left, right = tree_map[y, :x], tree_map[y, x + 1:]
    up, down = tree_map[:y, x], tree_map[y + 1:, x]

    directions = [reversed(up), down, reversed(left), right]

    for i, direction in enumerate(directions):
        for step in direction:
            table[i] += 1
            if step >= tree_map[y][x]:
                break

    return table.prod(), table


def part_two():
    tree_map = process_input()
    result = (-1, -1, -1)

    for y in range(1, len(tree_map) - 1):
        for x in range(1, len(tree_map[0]) - 1):
            score, table = scenic_score(tree_map, x, y)
            if score >= result[0]:
                result = (score, x, y)

    return f'Score: {result[0]}  | (x: {result[1]}, y: {result[2]})'


def main():
    print(
        f'\N{File Folder}{os.path.dirname(__file__).split(chr(92))[-1]}:\n'
        f'\t\N{pushpin}{part_one()}\n'
        f'\t\N{pushpin}{part_two()}'
    )


if __name__ == '__main__':
    main()
