import os
import re
from utilities import get_puzzle


def main():
    folders = [folder for folder in os.listdir('.') if os.path.isdir(os.path.join('.', folder))]
    folders = list(filter(re.compile('Day *[0-9]+').match, folders))

    for folder in folders:
        file = f'"{os.path.dirname(__file__)}\\{folder}\\main.py"'
        os.system(f'python {file}')


if __name__ == '__main__':
    main()
