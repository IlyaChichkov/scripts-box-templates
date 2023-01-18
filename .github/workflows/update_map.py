# change: map update
import os
from os import walk

root_path = ''

def hello():
    print('Test started!')
    root_path = os.getcwd()
    print(os.listdir())
    print('\n')
    f = []
    for (dirpath, dirnames, filenames) in walk(root_path):
        f.extend(filenames)
        print(f)
        print('\n')
        break
    print('Test done!')

if __name__ == '__main__':
    hello()