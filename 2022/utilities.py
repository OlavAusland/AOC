from datetime import datetime

import requests
import os


def display_day(part_one: callable, part_two: callable):
    print(
        f'\N{File Folder}{os.getcwd().split(chr(92))[-1]}:\n'
        f'\t{part_one()}\n'
        f'\t{part_two()}'
    )


def get_puzzle(session_id: str, day: int = datetime.now().day, year: int = datetime.now().year) -> str:
    url = f'https://adventofcode.com/{year}/day/{day}/input'
    cookies = {'session': session_id}
    return requests.get(url=url, cookies=cookies).text
