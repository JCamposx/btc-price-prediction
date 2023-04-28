import os
import glob


def main():
    path = os.path.join(os.path.dirname(__file__), '../cache/')

    cache_files = glob.glob(
        os.path.join(path, '**', '*pickle'),
        recursive=True
    )

    for file in cache_files:
        os.remove(file)


if __name__ == '__main__':
    main()
