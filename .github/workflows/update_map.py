import json
import os
from os import walk

class Map:
    folders = []

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

root_path = ''

def get_map():
    map = Map()
    map.folders = get_folders(root_path)
    return map.toJSON()

def os_walk_folders(path):
    f = []
    for (dirpath, dirnames, filenames) in walk(path):
        f.extend(dirnames)
        break
    return f

def get_folders(path):
    result = []

    for dir in os_walk_folders(path):
        if '.' not in dir[0]:
            group_folders = os_walk_folders(path + '/' + dir)
            result.append({ 'name': dir, 'folders': group_folders })
        print(dir)

    return result

def init():
    print('----------Map update started!-----------')
    global root_path
    root_path = os.getcwd()
    map = get_map()
    map_file = open(root_path + '/map.json', 'w')
    map_file.write(map)
    map_file.close()

if __name__ == '__main__':
    init()