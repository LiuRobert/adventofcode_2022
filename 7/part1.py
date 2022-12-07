import os

current_folder = os.path.dirname(os.path.abspath(__file__))
with open(current_folder + "/input.txt", "r") as f:
    lines = f.read().splitlines()

class Dir:
    def __init__(self, name: str, parent):
        self.parent = parent
        self.name = name
        self.files = []
        self.dirs = []
        self.size = 0

class File:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size


def addDir(current_dir: Dir, name: str) -> Dir:
    if current_dir is None:
        current_dir = Dir(name, None)
        return current_dir
    for dir in current_dir.dirs:
        if dir.name == name:
            return dir
    new_dir = Dir(name, current_dir)
    current_dir.dirs.append(new_dir)
    return new_dir


def calculate_sizes(dir: Dir, all_dirs: list) -> int:
    size = 0
    for file in dir.files:
        size += file.size
    for d in dir.dirs:
        size += calculate_sizes(d, all_dirs)
    dir.size = size
    all_dirs.append(dir)
    return size


if __name__ == '__main__':
    root = None
    current_dir = None
    for line in lines:
        words = line.split(" ")
        if words[0] == "$" and words[1] == "cd":
            if words[2] == "..":
                current_dir = current_dir.parent
            else:
                current_dir = addDir(current_dir, words[2])
                if root is None:
                    root = current_dir
        elif words[0].isdigit():
            current_dir.files.append(File(words[1], int(words[0])))

    all_dirs = []
    calculate_sizes(root, all_dirs)
    total_size = 0
    for dir in all_dirs:
        if dir.size <= 100000:
            total_size += dir.size
    print(total_size)
    