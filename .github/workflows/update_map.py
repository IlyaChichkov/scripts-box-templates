# change: map update
import json
import os
from os import walk

root_path = ''

def get_map():
    map = { 'name': '123'}
    map = json.dump(map)
    print(map)

def hello():
    print('Test started!')
    root_path = os.getcwd()
    print(os.listdir())
    print('\n')
    f = []
    for (dirpath, dirnames, filenames) in walk(root_path):
        f.extend(filenames)
        f.extend(dirnames)
        print(f)
        print('\n')
        break
    print('Test done!')

if __name__ == '__main__':
    hello()
    get_map()