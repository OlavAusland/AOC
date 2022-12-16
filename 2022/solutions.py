import os
import re
from utilities import get_puzzle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--id', type=str, help='AoC session_id (cookie) to get your solutions🎊')


def main():
    folders = [folder for folder in os.listdir('.') if os.path.isdir(os.path.join('.', folder))]
    folders = list(filter(re.compile('Day *[0-9]+').match, folders))
    args = parser.parse_args()

    for folder in folders:

        if args.id is not None:
            with open(f'{os.path.dirname(__file__)}\\{folder}\\puzzle.txt', 'w+') as file:
                puzzle = get_puzzle(session_id=args.id, day=int(folder.split(' ')[-1]))
                file.write(puzzle)

        file = f'"{os.path.dirname(__file__)}\\{folder}\\main.py"'
        os.system(f'python {file}')


if __name__ == '__main__':
    main()
