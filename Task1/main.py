import os
import lief
import collections

import sys
import argparse

def get_shared_libraries(file_path):
    """
    Возвращает список общих библиотек, используемых файлом.

    Args:
        file_path (str): Путь к исполняемому файлу.

    Returns:
        list: Список общих библиотек.
    """
    binary = lief.parse(file_path)
    shared_libraries = []
    for library in binary.libraries:
        if library.name:
            shared_libraries.append(library.name)
    return shared_libraries

def bldd(folder_path):
    """
    Выводит все общие библиотеки, используемые исполняемыми файлами в папке,
    в отсортированном порядке.

    Args:
        folder_path (str): Путь к папке.

    Returns:
        None
    """
    all_shared_libraries = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            if lief.is_elf(file_path):
                shared_libraries = get_shared_libraries(file_path)
                all_shared_libraries.extend(shared_libraries)

    shared_libraries_counter = collections.Counter(all_shared_libraries)
    sorted_shared_libraries = sorted(shared_libraries_counter.items(), key=lambda x: (-x[1], x[0]))

    for shared_library, count in sorted_shared_libraries:
        print(f'{count:5} {shared_library}')



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="First task of AL")
    parser.add_argument('source', metavar='source', type=str,
        help='source directory')

    parser.add_argument(
    '--output', help='name file where output save')

    args = parser.parse_args()
    
    print(args.source)
    file_list = os.listdir(args.source)
    print(file_list)
    print(lief.is_elf(os.path.join(args.source, file_list[0])))
    bldd(args.source)