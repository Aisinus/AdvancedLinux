import os
import lief
import collections

import sys
import argparse

shared_libraries = {}

def get_shared_libraries(file_path):
    binary = lief.parse(file_path)
    for library in binary.libraries:
        try:
            if library:
                if library not in shared_libraries:
                    shared_libraries[library] = []
                shared_libraries[library].append(file_path)
        except Exception as e:
            continue


def bldd(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            if lief.is_elf(file_path):
                get_shared_libraries(file_path)
        for dir in dirs:
            bldd(dir)
    names = map(lambda x: (x, len(shared_libraries[x])), shared_libraries)
    sorted_shared_libraries = sorted(names, key=lambda x: x[1], reverse=True)
    return sorted_shared_libraries


def print_libraries(sorted_libraries, output):
    if output is not None:
        f = open(output, "w")
    for lib, count in sorted_libraries:
        if output is None:
            print(f"{lib} ({count} execs)")
        else:
            f.write(f"\n{lib} ({count} execs)\n")
        for path in shared_libraries[lib]:
            if output is None:
                print(f"-> {path}")
            else:
                f.write(f"-> {path}\n")
    if output is not None:
        f.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="First task of AL")
    parser.add_argument('source', metavar='source', type=str,
        help='source directory')

    parser.add_argument(
    '--output', help='name file where output save, empty if write to console')

    args = parser.parse_args()
    file_list = os.listdir(args.source)
    sorted_libraries = bldd(args.source)

    print_libraries(sorted_libraries, args.output)
