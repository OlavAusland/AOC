import os


def load_puzzle() -> str:
    with open(f'{os.path.dirname(__file__)}\\puzzle.txt', 'r') as file:
        return file.read()


def part_one():
    buffer = load_puzzle()

    for i in range(0, len(buffer)-4):
        if len(set(buffer[i:i+4])) == 4:
            return i+4


def part_two():
    buffer = load_puzzle()

    for i in range(0, len(buffer)-14):
        if len(set(buffer[i:i+14])) == 14:
            return i+14


def main():
    print(
        f'\N{File Folder}{os.path.dirname(__file__).split(chr(92))[-1]}:\n'
        f'\t\N{pushpin}{part_one()}\n'
        f'\t\N{pushpin}{part_two()}'
    )


if __name__ == '__main__':
    main()
