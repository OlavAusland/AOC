import requests
from typing import List


class Reindeer:
    def __init__(self):
        self.calories = 0


# You can quite easily use a single array of integers, but let's use a Reindeer object for the spirit :)
def main():
    reindeers: List[Reindeer] = [Reindeer()]

    with open('./data.txt', 'r') as file:
        for line in file:
            if line == '\n':
                reindeers.append(Reindeer())
                continue
            reindeers[-1].calories += int(line)
    reindeers = sorted(reindeers, key=lambda x: x.calories, reverse=True)
    print(sum(reindeer.calories for reindeer in reindeers[0:3]))


if __name__ == '__main__':
    main()
