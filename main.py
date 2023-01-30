import argparse
import shutil
from pathlib import Path
from shutil import copyfile
from threading import Thread
import logging

"""
py main.py --sourse - s for_test
py main.py --output -o sorted
"""


parser = argparse.ArgumentParser(description='Sorting folder by extensions')
parser.add_argument('-s', '--source', required=True)
parser.add_argument('-o', '--output', default='sorted')
args = vars(parser.parse_args())
source = args.get('source')
output = args.get('output')

folders = []

def sorting(path: Path) -> None:
    for el in path.iterdir():
        if el.is_file():
            extension = el.suffix[1:]
            new_path = sorted / extension
            try:
                new_path.mkdir(exist_ok=True, parents=True)
                copyfile(el, new_path / el.name)
            except OSError as e:
                logging.error(e)

def grabs_folders(path: Path) -> None:
    for el in path.iterdir():
        if el.is_dir():
            folders.append(el)
            grabs_folders(el)



if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")
    to_sort = Path(source)
    sorted = Path(output)

    folders.append(to_sort)
    grabs_folders(to_sort)
    threads = []
    for folder in folders:
        th = Thread(target=sorting, args=(folder,))
        th.start()
        threads.append(th)

    [th.join() for th in threads]
    print(f'Folder {to_sort.name} sorted to {sorted.name} folder')
    shutil.rmtree(to_sort)

