# change: map update
import json
import os
from os import walk

root_path = ''

def get_map():
    map = { 'folders': '123' }
    map = json.dumps(map)
    f = get_folders(root_path)
    for folder in f:
        f.extend(get_folders(root_path + '/' + folder))
    print(f)
    print('\n')
    print(map)

def get_folders(path):
    f = []
    for (dirpath, dirnames, filenames) in walk(path):
        print(dirnames)
        f.extend(dirnames)
        break
    print(f)
    print('\n')

def init():
    print('Map update started!')
    root_path = os.getcwd()

if __name__ == '__main__':
    init()
    get_map()