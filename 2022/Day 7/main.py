import os
import re
from typing import Union, List


class Base:
    def __init__(self, name: str, path: str):
        self.name: str = name
        self.path: str = f'{path}/{name}'


class File(Base):
    def __init__(self, name: str, size: int, path: str, parent):
        super().__init__(name, path)
        self.parent: Directory = parent
        self.visual_depth = 0
        self.size = size
        self.extension = name.split('.')[-1]

    def get_size(self):
        return self.size

    def __repr__(self):
        return f'{self.name} (file, size={self.size})'


class Directory(Base):
    def __init__(self, name: str, path: str, depth: 0, parent):
        super().__init__(name, path)
        self.parent: Directory = parent
        self.name: str
        self.depth = depth
        self.visual_depth = 0
        self.children: List[Union[File, Directory]] = []
        self.size = self.get_size()

    def get_size(self) -> int:
        total_size: int = 0
        for child in self.children:
            total_size += child.get_size()
        return total_size

    def __repr__(self):
        self.visual_depth = self.parent.visual_depth + 1 if self.parent is not None else 0
        output: str = f'\N{File Folder} - {self.name}\n'
        for child in self.children:
            output += f'{"    " * self.visual_depth}└── {child}\n'
        return output[:-1]


class Explorer:
    def __init__(self):
        self.root: Directory = Directory('root', '/', 0, None)
        self.current: Directory = self.root
        self.directories: List[Directory] = [] # to easily sum up directory size
        self.disk_memory = 70_000_000
        self.used_memory = 0

    def touch(self, command: str):
        initial_folder = self.current

        path, file = command.split('/')[1:-1], command.split('/')[-1]

        if len(path) <= 0:
            self.current.children.append(File(file, -1, self.current.path, self.current))
            self.used_memory += self.current.children[-1].size
            return

        for directory in path:
            if any(folder.name == directory for folder in self.current.children):
                for child in self.current.children:
                    if child.name == directory:
                        self.current = child
            else:
                self.current.children.append(
                    Directory(directory, self.current.path, self.current.depth + 1, self.current))
                self.current = self.current.children[-1]

        self.current.children.append(File(file, -1, self.current.path, self.current))
        self.current = initial_folder

    def mkdir(self, command: str):
        initial_folder = self.current

        if bool(re.search('[.]+[a-zA-Z]+', command)):
            return

        path = command.split('/')
        path.remove('')

        for directory in path:
            if any(folder.name == directory for folder in self.current.children):
                for child in self.current.children:
                    if child.name == directory:
                        self.current = child
            else:
                self.current.children.append(
                    Directory(directory, self.current.path, self.current.depth + 1, self.current))
                self.directories.append(self.current.children[-1])
                self.current = self.current.children[-1]

        self.current = initial_folder

    def navigate(self, command: str):
        if command == '/':
            self.current = self.root
            self.current.visual_depth = -1
            return
        elif command == '..':
            if self.current.parent is not None:
                self.current = self.current.parent
                return
        command = list(command.split('/'))
        if '' in command:
            command.remove('')

        for directory in command:
            if directory == '..':
                self.current = self.current.parent if self.current.parent is not None else self.current
            if any(folder.name == directory for folder in self.current.children):
                for child in self.current.children:
                    if child.name == directory:
                        self.current = child
        self.current.visual_depth = -1

    def cwd(self):
        return self.current.path

    def command(self, prefix, command: str):
        if prefix == 'cd':
            self.navigate(command)
        elif prefix == 'ls':
            print(self.list())
        elif prefix == 'mkdir':
            self.mkdir(command)
        elif prefix == 'clear':
            self.clear()
        elif prefix == 'touch':
            self.touch(command)
        elif prefix == 'size':
            print(self.current.get_size())
        elif prefix == 'memsize':
            if command == '--free':
                print(self.disk_memory - self.used_memory)
            elif command == '--used':
                print(self.used_memory)

    def get_folder_depth(self, directory: Directory):
        pass

    def list(self):
        return self.current

    def remove(self):
        pass

    def has_child(self, name):
        for child in self.current.children:
            if child.name == name:
                return True
        return False

    @staticmethod
    def clear():
        os.system('CLS')

    @staticmethod
    def is_file(name) -> bool:
        return bool(re.search('[.]+[a-zA-Z]+', name))

    def create_file(self, name: str, size: int):
        self.current.children.append(File(name=name, size=size, path=self.current.path, parent=self.current))
        self.used_memory += self.current.children[-1].get_size()


explorer = Explorer()


def part_one():
    global explorer

    with open(f'{os.path.dirname(__file__)}\\puzzle.txt', 'r') as file:
        for line in file:
            command = line.strip('\n').split(' ')[0:]
            if re.search('\\$', line):
                if command[1] == 'cd':
                    explorer.navigate(command[2])
                elif command[1] == 'ls':
                    explorer.list()
            elif re.search('dir', command[0]):
                explorer.mkdir(f'/{command[1]}')
            elif command[0].isnumeric():
                explorer.create_file(command[-1], int(command[0]))

    explorer.navigate('/')

    answer: int = 0

    for child in explorer.directories:
        if child.get_size() <= 100000:
            answer += child.get_size()

    return answer


def part_two():
    global explorer

    explorer.directories = sorted(explorer.directories, key=lambda x: x.get_size())
    print(explorer.directories[0].get_size(), explorer.directories[-1].get_size())

    for directory in explorer.directories:
        if explorer.disk_memory - (explorer.used_memory - directory.get_size()) > 30000000:
            return directory.get_size()


def main():
    print(
        f'\N{File Folder}{os.path.dirname(__file__).split(chr(92))[-1]}:\n'
        f'\t\N{pushpin}{part_one()}\n'
        f'\t\N{pushpin}{part_two()}'
    )


if __name__ == '__main__':
    main()
