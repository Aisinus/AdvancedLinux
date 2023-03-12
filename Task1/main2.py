import os
import sys
import argparse

import lief


def get_all_exe_files(dir):
    try:
        ans = []
        for filename in os.listdir(dir):
            fullpath = os.path.join(dir, filename)
            binary = lief.parse(fullpath)
            if binary != None:
                print(type(binary.header))
    except Exception as ex:
        print(ex)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="First task of AL")
    parser.add_argument('source', metavar='source', type=str,
                    help='source directory')

    parser.add_argument(
        '--output', help='name file where output save')
    
    args = parser.parse_args()
    get_all_exe_files(args.source)
