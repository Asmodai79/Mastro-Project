import os
import sys
from csvparser import readcsvFile

def do_stuff():
    if len(sys.argv) < 2:
        print('Missing <dirname> parameter', file=sys.stderr)
        sys.exit(1)
    dir_name = sys.argv[1]
    files_list = os.listdir(dir_name)
    for f in files_list:
        if f.lower().endswith('.csv'):
            readcsvFile(os.path.join(dir_name, f))


if __name__ == "__main__":
    try:
        do_stuff()
    except Exception as ex:
        print(f'An error occurred: {ex}', file=sys.stderr)
