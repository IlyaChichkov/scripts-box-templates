
import os

def hello():
    print('Test started!')
    print(os.getcwd())
    print(os.listdir())
    print('Test done!')

if __name__ == '__main__':
    hello()